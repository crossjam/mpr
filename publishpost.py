#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "rich>=13.0.0",
# ]
# ///
"""
publishpost.py - Publish a draft branch onto main.

Squash-merges draft/<slug> into main, so the draft's private revision
history never reaches the public repository. In each post the merge
adds, it flips status: draft to status: published and adds a date if
the post has none, then commits. With --push it also pushes main and
deletes the draft branch locally and on the drafts remote.
"""

import argparse
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

from rich.console import Console

console = Console()

REPO_ROOT = Path(__file__).parent

BASE_BRANCH = "main"
PUBLIC_REMOTE = "origin"
DRAFTS_REMOTE = "drafts"

# A Pelican metadata line: "Key: value"
META_LINE = re.compile(r"^([A-Za-z][\w-]*):(.*)$")


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    """Run a git command in the repository root, capturing its output."""
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True, check=check
    )


def fail(message: str) -> None:
    """Print an error and exit."""
    console.print(f"[red]Error: {message}[/red]")
    sys.exit(1)


def header_bounds(lines: list[str]) -> tuple[int, int, bool]:
    """
    Locate the metadata header of a post.

    Returns (start, end, is_yaml): the header's lines are lines[start:end].
    YAML front matter sits between '---' fences; Pelican's Markdown
    metadata is the run of "Key: value" lines before the first blank line.
    """
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return 1, i, True
        raise ValueError("unterminated YAML front matter")

    end = 0
    while end < len(lines) and META_LINE.match(lines[end]):
        end += 1
    return 0, end, False


def get_field(text: str, key: str) -> str | None:
    """Return a header field's raw value, or None when it is absent."""
    lines = text.splitlines()
    start, end, _ = header_bounds(lines)
    for line in lines[start:end]:
        m = META_LINE.match(line)
        if m and m.group(1).lower() == key:
            return m.group(2).strip()
    return None


def set_field(text: str, key: str, value: str) -> str:
    """Set a header field, replacing it in place or appending it."""
    lines = text.splitlines()
    start, end, is_yaml = header_bounds(lines)

    for i in range(start, end):
        m = META_LINE.match(lines[i])
        if m and m.group(1).lower() == key:
            lines[i] = f"{m.group(1)}: {value}"
            break
    else:
        # Match the header's style: lowercase keys in YAML, Title case otherwise
        name = key if is_yaml else key.capitalize()
        lines.insert(end, f"{name}: {value}")

    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def publish_text(text: str, redate: bool) -> str:
    """Mark a post published, dating it now if undated or if asked to."""
    text = set_field(text, "status", "published")
    if redate or get_field(text, "date") is None:
        text = set_field(text, "date", datetime.now().strftime("%Y-%m-%d %H:%M"))
    return text


def check_ready(branch: str) -> None:
    """Verify main is checked out and clean, and the draft branch exists."""
    current = git("symbolic-ref", "--short", "-q", "HEAD", check=False).stdout.strip()
    if current != BASE_BRANCH:
        fail(f"check out {BASE_BRANCH} first (currently on {current or 'a detached HEAD'})")

    if git("diff", "--quiet", check=False).returncode or git(
        "diff", "--cached", "--quiet", check=False
    ).returncode:
        fail("the working tree has uncommitted changes; commit or stash them first")

    exists = git("rev-parse", "--verify", "--quiet", f"refs/heads/{branch}", check=False)
    if exists.returncode:
        fail(f"no local branch {branch}")


def squash_merge(branch: str) -> list[Path]:
    """Squash-merge the branch and return the draft posts it adds or changes."""
    merge = git("merge", "--squash", branch, check=False)
    if merge.returncode:
        git("reset", "--merge", check=False)
        fail(f"merging {branch} failed and was rolled back:\n{merge.stdout}{merge.stderr}")

    changed = git(
        "diff", "--cached", "--name-only", "--diff-filter=AM", "--", "content/"
    ).stdout.split()
    posts = []
    for name in changed:
        path = REPO_ROOT / name
        if path.suffix == ".md" and (get_field(path.read_text(), "status") or "").lower() == "draft":
            posts.append(path)

    if not posts:
        git("reset", "--merge", check=False)
        fail(f"{branch} has no post marked status: draft under content/")
    return posts


def parse_args():
    parser = argparse.ArgumentParser(
        description="Publish a draft/<slug> branch onto main.",
    )
    parser.add_argument("draft", help="draft slug, or the full draft/<slug> branch name")
    parser.add_argument(
        "--redate",
        action="store_true",
        help="set the post's date to now, even if it already has one",
    )
    parser.add_argument(
        "--push",
        action="store_true",
        help=f"also push {BASE_BRANCH} to {PUBLIC_REMOTE} and delete the draft branch "
        f"locally and on {DRAFTS_REMOTE}",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    branch = args.draft if args.draft.startswith("draft/") else f"draft/{args.draft}"

    check_ready(branch)
    posts = squash_merge(branch)

    titles = []
    for path in posts:
        text = publish_text(path.read_text(), args.redate)
        path.write_text(text)
        git("add", str(path.relative_to(REPO_ROOT)))
        titles.append((get_field(text, "title") or "").strip("\"'") or path.stem)
        console.print(f"[green]✓[/green] Published {path.relative_to(REPO_ROOT)}")

    git("commit", "-q", "-m", f"Publish {', '.join(titles)}")
    console.print(f"[green]✓[/green] Committed on {BASE_BRANCH}: {git('log', '-1', '--format=%h %s').stdout.strip()}")

    finish = [
        ["push", PUBLIC_REMOTE, BASE_BRANCH],
        ["push", DRAFTS_REMOTE, "--delete", branch],
        ["branch", "-D", branch],
    ]
    if args.push:
        for cmd in finish:
            result = git(*cmd, check=False)
            if result.returncode:
                fail(f"git {' '.join(cmd)} failed:\n{result.stderr.strip()}")
            console.print(f"[green]✓[/green] git {' '.join(cmd)}")
        console.print("\nNext: deploy with [cyan]uv run poe rsync_upload[/cyan]")
    else:
        console.print("\n[dim]Next steps:[/dim]")
        for cmd in finish:
            console.print(f"  [cyan]git {' '.join(cmd)}[/cyan]")
        console.print("  [cyan]uv run poe rsync_upload[/cyan]")
        console.print(f"\n[dim]To undo before pushing:[/dim] [cyan]git reset --hard HEAD~1[/cyan]")


if __name__ == "__main__":
    main()
