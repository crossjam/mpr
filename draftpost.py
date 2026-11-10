#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "rich>=13.0.0",
#     "pypandoc>=1.13",
#     "python-slugify>=8.0.0",
#     "click>=8.0.0",
# ]
# ///
"""
draftpost.py - Create a new blog post draft with YAML metadata header.

This script starts a draft/<slug> branch from main, writes the post to
content/<slug>.md with proper YAML metadata formatting, commits it, and
pushes the branch to the private drafts remote. It provides interactive
prompts for post metadata and can optionally grab content from the
clipboard on macOS.
"""

import argparse
import os
import shlex
import sys
import subprocess
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Optional

import click
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from slugify import slugify

console = Console()

REPO_ROOT = Path(__file__).parent

# Branch drafts start from, and the private remote they are pushed to
BASE_BRANCH = "main"
DRAFTS_REMOTE = "drafts"

# Default Lorem Ipsum content for new posts
LOREM_IPSUM = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""


def get_clipboard_content() -> Optional[tuple[str, str]]:
    """
    Attempt to get clipboard content on macOS using pbpaste.

    Returns:
        Optional tuple of (content, format) where format is 'txt', 'rtf', or None
    """
    if sys.platform != "darwin":
        return None

    try:
        # First try to get RTF format
        result = subprocess.run(
            ["pbpaste", "-Prefer", "rtf"], capture_output=True, text=False, timeout=5
        )

        if result.returncode == 0 and result.stdout:
            # Check if it's actually RTF by looking for RTF header
            if result.stdout.startswith(b"{\\rtf"):
                return (result.stdout.decode("utf-8", errors="ignore"), "rtf")

        # Fall back to plain text
        result = subprocess.run(["pbpaste"], capture_output=True, text=True, timeout=5)

        if result.returncode == 0 and result.stdout.strip():
            return (result.stdout, "txt")

    except (subprocess.TimeoutExpired, FileNotFoundError, Exception) as e:
        console.print(f"[yellow]Could not access clipboard: {e}[/yellow]")

    return None


def convert_rtf_to_markdown(rtf_content: str) -> str:
    """
    Convert RTF content to Markdown using pandoc.

    Args:
        rtf_content: RTF formatted string

    Returns:
        Markdown formatted string
    """
    try:
        import pypandoc

        # Write RTF to a temporary file
        with tempfile.NamedTemporaryFile(mode="w", suffix=".rtf", delete=False) as f:
            f.write(rtf_content)
            rtf_file = f.name

        try:
            # Convert RTF to Markdown
            markdown = pypandoc.convert_file(rtf_file, "markdown", format="rtf")
            return markdown
        finally:
            # Clean up temp file
            os.unlink(rtf_file)

    except ImportError:
        console.print("[yellow]pypandoc not available, returning RTF as-is[/yellow]")
        return rtf_content
    except Exception as e:
        console.print(f"[yellow]Could not convert RTF: {e}[/yellow]")
        return rtf_content


def format_as_blockquote(text: str) -> str:
    """
    Format text as a markdown blockquote by prefixing each line with '> '.

    Args:
        text: The text to format as a blockquote

    Returns:
        Blockquoted text
    """
    lines = text.split("\n")
    return "\n".join(f"> {line}" if line else ">" for line in lines)


def get_post_content(
    use_clipboard: bool = True, file_path: Optional[str] = None, quote: bool = False
) -> str:
    """
    Get post content from file, clipboard, or use Lorem Ipsum placeholder.

    Args:
        use_clipboard: Whether to attempt clipboard access
        file_path: Path to file to read content from (or '-' for stdin)
        quote: Whether to format content as a markdown blockquote

    Returns:
        Post content as a string (from file, clipboard, or Lorem Ipsum fallback)
    """
    content = ""

    # First priority: read from file if specified
    if file_path:
        try:
            if file_path == "-":
                # Read from stdin
                console.print("[cyan]Reading content from standard input...[/cyan]")
                content = sys.stdin.buffer.read().decode("utf-8", errors="replace")
                console.print("[green]✓[/green] Content read from stdin")
            else:
                # Read from file
                file_path_obj = Path(file_path)
                if not file_path_obj.exists():
                    console.print(f"[red]Error: File not found: {file_path}[/red]")
                    sys.exit(1)
                content = file_path_obj.read_text(encoding="utf-8", errors="replace")
                console.print(f"[green]✓[/green] Content read from file: {file_path}")
        except Exception as e:
            console.print(f"[red]Error reading file: {e}[/red]")
            sys.exit(1)

    # Second priority: try clipboard if enabled
    elif use_clipboard and sys.platform == "darwin":
        clipboard_data = get_clipboard_content()

        if clipboard_data:
            clipboard_content, clipboard_format = clipboard_data

            if clipboard_format == "rtf":
                console.print(
                    "[cyan]RTF content detected in clipboard, converting to Markdown...[/cyan]"
                )
                content = convert_rtf_to_markdown(clipboard_content)
                console.print("[green]✓[/green] RTF converted to Markdown")
            else:
                content = clipboard_content
                console.print(
                    "[green]✓[/green] Plain text content grabbed from clipboard"
                )

    # Third priority: use Lorem Ipsum fallback
    if not content:
        console.print(
            "[yellow]No content source available, using Lorem Ipsum placeholder.[/yellow]"
        )
        content = LOREM_IPSUM

    # Apply blockquote formatting if requested
    content = content.strip()
    if quote:
        content = format_as_blockquote(content)

    return content


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    """Run a git command in the repository root, capturing its output."""
    return subprocess.run(
        ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True, check=check
    )


def fail(message: str) -> None:
    """Print an error and exit."""
    console.print(f"[red]Error: {message}[/red]")
    sys.exit(1)


def check_git_ready(branch: str) -> None:
    """
    Verify the repository can start a new draft branch.

    Refreshes the draft-branch hook guards first, since another tool may
    have rewritten the hooks since they were installed.
    """
    hooks = subprocess.run(
        [str(REPO_ROOT / "install-draft-hooks.sh")], cwd=REPO_ROOT, check=False
    )
    if hooks.returncode != 0:
        fail("could not install the draft-branch hook guards")

    if git("diff", "--quiet", check=False).returncode or git(
        "diff", "--cached", "--quiet", check=False
    ).returncode:
        fail("the working tree has uncommitted changes; commit or stash them first")

    for ref in (f"refs/heads/{branch}", f"refs/remotes/{DRAFTS_REMOTE}/{branch}"):
        exists = git("rev-parse", "--verify", "--quiet", ref, check=False)
        if exists.returncode == 0:
            fail(f"{ref} already exists; to resume it: git switch {branch}")

    if git("remote", "get-url", DRAFTS_REMOTE, check=False).returncode:
        fail(
            f"no '{DRAFTS_REMOTE}' remote; add it with: "
            f"git remote add {DRAFTS_REMOTE} git@github.com:crossjam/mpr.drafts.git"
        )


def start_draft_branch(branch: str, filepath: Path, title: str) -> None:
    """Commit the new post on its own branch and push it to the drafts remote."""
    git("add", str(filepath.relative_to(REPO_ROOT)))
    git("commit", "-q", "-m", f"Start draft: {title}")

    push = git("push", "-q", "-u", DRAFTS_REMOTE, branch, check=False)
    if push.returncode:
        console.print(
            f"[yellow]Could not push {branch} to {DRAFTS_REMOTE}; "
            f"push it later with: git push -u {DRAFTS_REMOTE} {branch}[/yellow]"
        )
        console.print(f"[dim]{push.stderr.strip()}[/dim]")
    else:
        console.print(f"[green]✓[/green] Pushed {branch} to {DRAFTS_REMOTE}")


def create_post(
    title: str,
    author: str,
    content: str,
    slug: str,
) -> Path:
    """
    Create a new post file with YAML frontmatter in content/.

    Args:
        title: Post title
        author: Post author
        content: Post content (markdown)
        slug: URL slug for the filename

    Returns:
        Path to the created post file
    """
    filepath = REPO_ROOT / "content" / f"{slug}.md"

    # The branch starts from main, so an existing file is a published post
    if filepath.exists():
        fail(f"{filepath.relative_to(REPO_ROOT)} already exists on {BASE_BRANCH}")

    # Get current date and time in the format YYYY-MM-DD HH:MM
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Build the post content with proper YAML frontmatter
    post_content = f"""---
title: "{title}"
date: {date_str}
author: "{author}"
status: draft
---

{content}
"""

    # Write to file
    filepath.write_text(post_content)

    return filepath


def print_help():
    """Print help information and exit."""
    help_text = """
[bold cyan]draftpost.py - Create a new blog post draft[/bold cyan]

[bold]Usage:[/bold]
  ./draftpost.py [options]
  ./draftpost.py --help
  ./draftpost.py --file <filename>
  cat content.txt | ./draftpost.py --file -

[bold]Description:[/bold]
  Starts a draft/<slug> branch from main, writes the post to
  content/<slug>.md with YAML metadata (status: draft), commits it, and
  pushes the branch to the private drafts remote. The script provides
  interactive prompts for post metadata and can obtain content from
  multiple sources. The working tree must be clean.

[bold]Options:[/bold]
  -h, --help            Show this help message and exit
  -f, --file FILE       Read post content from FILE (use '-' for stdin)
                        If not specified, tries clipboard on macOS, then
                        falls back to Lorem Ipsum placeholder
  -q, --quote           Format content as a markdown blockquote
                        Prefixes each line with '> ' per markdown syntax
  -e, --edit            Open the draft post in the default editor after creation
                        Uses $EDITOR environment variable or system default

[bold]Content Sources (in priority order):[/bold]
  1. File specified with --file option (or stdin with --file -)
  2. Clipboard content on macOS (via pbpaste)
     - Supports plain text and RTF formats
     - RTF is automatically converted to Markdown
  3. Lorem Ipsum placeholder text

[bold]Examples:[/bold]
  # Interactive mode with clipboard
  ./draftpost.py

  # Read content from a file
  ./draftpost.py --file my-post-content.md

  # Read content from stdin
  cat my-content.txt | ./draftpost.py --file -
  echo "Post content" | ./draftpost.py --file -

  # Format content as blockquote
  ./draftpost.py --quote --file my-content.txt
  echo "Quote text" | ./draftpost.py --quote --file -

  # Create and immediately edit the post
  ./draftpost.py --edit
  ./draftpost.py --file my-content.txt --edit

[bold]Output:[/bold]
  Branch: draft/<slug>, pushed to the drafts remote
  File:   content/<slug>.md (YAML metadata header + Markdown content)

[bold]Next Steps:[/bold]
  Edit and commit on the branch; git push sends it to the drafts remote.
  When ready, publish it from main:
  ./publishpost.py <slug>
"""
    console.print(help_text)
    sys.exit(0)


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Create a new blog post draft with YAML metadata header",
        add_help=False,  # We'll handle --help ourselves for rich formatting
    )
    parser.add_argument(
        "-h", "--help", action="store_true", help="Show help message and exit"
    )
    parser.add_argument(
        "-f",
        "--file",
        type=str,
        metavar="FILE",
        help='Read post content from FILE (use "-" for stdin)',
    )
    parser.add_argument(
        "-q",
        "--quote",
        action="store_true",
        default=False,
        help="Format content as a markdown blockquote",
    )
    parser.add_argument(
        "-e",
        "--edit",
        action="store_true",
        default=False,
        help="Open the draft post in the default editor after creation",
    )

    args = parser.parse_args()

    # Handle help flag
    if args.help:
        print_help()

    return args


def main():
    """Main entry point for the draftpost script."""
    # Parse command line arguments
    args = parse_args()

    console.print(
        Panel.fit(
            "[bold cyan]Draft Post Creator[/bold cyan]\n"
            "Start a new blog post on its own draft branch",
            border_style="cyan",
        )
    )

    # Check if we can use clipboard on macOS
    can_use_clipboard = sys.platform == "darwin"

    # Prompt for metadata
    console.print("\n[bold]Post Metadata[/bold]")

    title = Prompt.ask("[cyan]Title[/cyan]")
    author = Prompt.ask("[cyan]Author[/cyan]", default="C. Ross Jam")

    # Optional: custom slug
    default_slug = slugify(title)
    use_custom_slug = Confirm.ask(
        f"[cyan]Use custom slug?[/cyan] (default: [dim]{default_slug}[/dim])",
        default=False,
    )

    slug = default_slug
    if use_custom_slug:
        slug = slugify(Prompt.ask("[cyan]Custom slug[/cyan]", default=default_slug))

    branch = f"draft/{slug}"
    check_git_ready(branch)

    # Get content
    console.print("\n[bold]Post Content[/bold]")

    # If --file is specified, use that; otherwise ask about clipboard
    use_clipboard = False
    if args.file:
        # Content will be read from file
        pass
    elif can_use_clipboard:
        use_clipboard = Confirm.ask(
            "[cyan]Use content from clipboard?[/cyan]", default=False
        )

    content = get_post_content(use_clipboard, args.file, args.quote)

    # Show preview
    console.print("\n[bold]Preview[/bold]")
    console.print(
        Panel(
            f"[bold]Title:[/bold] {title}\n"
            f"[bold]Author:[/bold] {author}\n"
            f"[bold]Slug:[/bold] {slug}\n"
            f"[bold]Branch:[/bold] {branch} (from {BASE_BRANCH})\n"
            f"[bold]Content:[/bold] {content[:100]}{'...' if len(content) > 100 else ''}",
            border_style="cyan",
        )
    )

    # Confirm creation
    if not Confirm.ask("\n[cyan]Create this post?[/cyan]", default=True):
        console.print("[red]Aborted.[/red]")
        sys.exit(1)

    # Create the post on its own branch
    try:
        git("switch", "-q", "-c", branch, BASE_BRANCH)
        console.print(f"[green]✓[/green] Switched to new branch {branch}")

        filepath = create_post(
            title=title,
            author=author,
            content=content,
            slug=slug,
        )
        console.print(f"\n[bold green]✓[/bold green] Post created successfully!")
        console.print(f"[cyan]Location:[/cyan] {filepath}")

        # Open in editor if --edit flag is set
        if args.edit:
            console.print(f"\n[cyan]Opening in editor...[/cyan]")
            try:
                click.edit(filename=str(filepath))
                console.print(f"[green]✓[/green] Editor session completed")
            except Exception as e:
                console.print(f"[yellow]Could not open editor: {e}[/yellow]")
                console.print(
                    f"[dim]Tip: Set the EDITOR environment variable or check file permissions[/dim]"
                )

        start_draft_branch(branch, filepath, title)

        console.print(f"\n[dim]Next steps:[/dim]")
        console.print(
            f"  1. Edit [cyan]{filepath.relative_to(REPO_ROOT)}[/cyan], commit, "
            f"and [cyan]git push[/cyan] (goes to {DRAFTS_REMOTE})"
        )
        console.print(
            f"  2. When ready to publish, from {BASE_BRANCH}: "
            f"[cyan]./publishpost.py {shlex.quote(slug)}[/cyan]"
        )

    except subprocess.CalledProcessError as e:
        console.print(f"[bold red]git {e.cmd[1]} failed:[/bold red] {e.stderr.strip()}")
        sys.exit(1)
    except Exception as e:
        console.print(f"[bold red]Error creating post:[/bold red] {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
