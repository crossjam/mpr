"""Drive both post commands against a throwaway repository."""

import shutil
import subprocess
from pathlib import Path

import click
import pytest
from click.testing import CliRunner

from mpr import metadata
from mpr.cli import cli

HOOKS_SCRIPT = Path(__file__).parents[1] / "install-draft-hooks.sh"


def run(*args: str, cwd: Path) -> str:
    return subprocess.run(args, cwd=cwd, check=True, capture_output=True, text=True).stdout


@pytest.fixture
def blog(tmp_path, monkeypatch):
    """A clone with main, a bare origin, and a bare drafts remote."""
    # The pre-push guard only lets draft branches go to a URL like this one
    drafts = tmp_path / "crossjam" / "mpr.drafts.git"
    origin = tmp_path / "origin.git"
    for bare in (drafts, origin):
        run("git", "init", "-q", "--bare", "-b", "main", str(bare), cwd=tmp_path)

    work = tmp_path / "work"
    run("git", "init", "-q", "-b", "main", str(work), cwd=tmp_path)
    for key, value in [
        ("user.name", "Test"),
        ("user.email", "test@example.com"),
        ("commit.gpgsign", "false"),
    ]:
        run("git", "config", key, value, cwd=work)
    shutil.copy(HOOKS_SCRIPT, work)
    (work / "content").mkdir()
    (work / "content" / "old.md").write_text("Title: Old\nStatus: published\n\nOld post.\n")
    run("git", "add", ".", cwd=work)
    run("git", "commit", "-q", "-m", "Initial", cwd=work)
    run("git", "remote", "add", "origin", str(origin), cwd=work)
    run("git", "remote", "add", "drafts", str(drafts), cwd=work)
    run("git", "push", "-q", "origin", "main", cwd=work)

    monkeypatch.chdir(work)
    return work


def test_draft_then_publish(blog):
    runner = CliRunner()
    new = runner.invoke(
        cli,
        ["draft", "new", "--title", "Hello, World", "--file", "-", "--yes"],
        input="First draft.\n",
    )
    assert new.exit_code == 0, new.output
    assert run("git", "branch", "--show-current", cwd=blog).strip() == "draft/hello-world"
    assert "draft/hello-world" in run("git", "ls-remote", "--heads", "drafts", cwd=blog)

    post = blog / "content" / "hello-world.md"
    assert metadata.get_field(post.read_text(), "status") == "draft"
    assert post.read_text().rstrip().endswith("First draft.")

    run("git", "switch", "-q", "main", cwd=blog)
    published = runner.invoke(cli, ["publish", "draft", "hello-world", "--push"])
    assert published.exit_code == 0, published.output

    assert run("git", "log", "-1", "--format=%s", cwd=blog).strip() == "Publish Hello, World"
    assert metadata.get_field(post.read_text(), "status") == "published"
    assert run("git", "rev-parse", "main", cwd=blog) == run(
        "git", "rev-parse", "origin/main", cwd=blog
    )
    assert run("git", "ls-remote", "--heads", "drafts", cwd=blog) == ""
    assert run("git", "branch", "--list", "draft/*", cwd=blog) == ""


def test_draft_refuses_a_published_slug(blog):
    result = CliRunner().invoke(cli, ["draft", "new", "--title", "Old", "--yes"])
    assert result.exit_code == 1
    assert "already a published post" in result.output
    assert run("git", "branch", "--show-current", cwd=blog).strip() == "main"


def test_publish_switches_to_main_from_the_draft(blog):
    start_draft("From Draft")
    result = CliRunner().invoke(cli, ["publish", "draft", "from-draft"])
    assert result.exit_code == 0, result.output
    assert run("git", "branch", "--show-current", cwd=blog).strip() == "main"
    assert run("git", "log", "-1", "--format=%s", cwd=blog).strip() == "Publish From Draft"


def test_publish_refuses_uncommitted_changes(blog):
    start_draft("Dirty")
    (blog / "content" / "dirty.md").write_text("unsaved\n")
    result = CliRunner().invoke(cli, ["publish", "draft", "dirty"])
    assert result.exit_code == 1
    assert "uncommitted changes" in result.output
    assert run("git", "branch", "--show-current", cwd=blog).strip() == "draft/dirty"


def start_draft(title: str) -> None:
    result = CliRunner().invoke(cli, ["draft", "new", "--title", title, "--yes"])
    assert result.exit_code == 0, result.output


def commit_on_main(blog: Path, name: str, text: str) -> None:
    run("git", "switch", "-q", "main", cwd=blog)
    (blog / "content" / name).write_text(text)
    run("git", "commit", "-q", "-am", f"Change {name}", cwd=blog)


def test_publish_merges_onto_a_main_that_moved_on(blog):
    start_draft("Later")
    commit_on_main(blog, "old.md", "Title: Old\nStatus: published\n\nOld post, edited.\n")

    result = CliRunner().invoke(cli, ["publish", "draft", "later"])
    assert result.exit_code == 0, result.output
    assert "edited" in (blog / "content" / "old.md").read_text()
    assert metadata.get_field((blog / "content" / "later.md").read_text(), "status") == "published"
    assert run("git", "status", "--porcelain", cwd=blog) == ""
    # A squash merge: one parent, so no draft history on main
    assert len(run("git", "log", "-1", "--format=%P", cwd=blog).split()) == 1


def test_publish_conflict_changes_nothing(blog):
    start_draft("Clash")
    (blog / "content" / "old.md").write_text("Title: Old\n\nDraft side.\n")
    run("git", "commit", "-q", "-am", "Draft edit", cwd=blog)
    commit_on_main(blog, "old.md", "Title: Old\n\nMain side.\n")
    head = run("git", "rev-parse", "HEAD", cwd=blog)

    result = CliRunner().invoke(cli, ["publish", "draft", "clash"])
    assert result.exit_code == 1
    assert "conflicts with main in content/old.md" in result.output
    assert run("git", "rev-parse", "HEAD", cwd=blog) == head
    assert run("git", "status", "--porcelain", cwd=blog) == ""


def test_push_refuses_draft_branches_outside_drafts(blog):
    from mpr import repo

    run("git", "switch", "-q", "-c", "draft/leak", cwd=blog)
    with repo.open_repo() as r, pytest.raises(click.ClickException, match="refusing to push"):
        repo.push(r, "origin", "draft/leak")
    assert run("git", "ls-remote", "--heads", "origin", cwd=blog).count("draft/") == 0


def test_save_commits_and_pushes(blog):
    start_draft("Saved")
    post = blog / "content" / "saved.md"
    post.write_text(post.read_text() + "\nMore words.\n")
    (blog / "content" / "saved-figure.md").write_text("A new file.\n")

    result = CliRunner().invoke(cli, ["draft", "save", "-m", "Add words"])
    assert result.exit_code == 0, result.output
    assert run("git", "status", "--porcelain", cwd=blog) == ""
    assert run("git", "log", "-1", "--format=%s", cwd=blog).strip() == "Add words"
    remote_tip = run("git", "ls-remote", "drafts", "refs/heads/draft/saved", cwd=blog).split()[0]
    assert remote_tip == run("git", "rev-parse", "HEAD", cwd=blog).strip()


def test_switch_fetches_a_draft_started_elsewhere(blog):
    start_draft("Elsewhere")
    run("git", "switch", "-q", "main", cwd=blog)
    run("git", "branch", "-q", "-D", "draft/elsewhere", cwd=blog)
    run("git", "update-ref", "-d", "refs/remotes/drafts/draft/elsewhere", cwd=blog)

    listed = CliRunner().invoke(cli, ["draft", "list"])
    assert "elsewhere  (drafts)" in listed.output

    result = CliRunner().invoke(cli, ["draft", "switch", "elsewhere"])
    assert result.exit_code == 0, result.output
    assert run("git", "branch", "--show-current", cwd=blog).strip() == "draft/elsewhere"
    assert (
        run("git", "rev-parse", "--abbrev-ref", "@{upstream}", cwd=blog).strip()
        == "drafts/draft/elsewhere"
    )


def test_finish_refuses_an_unpublished_draft(blog):
    start_draft("Not Yet")
    run("git", "switch", "-q", "main", cwd=blog)

    result = CliRunner().invoke(cli, ["publish", "finish", "not-yet"])
    assert result.exit_code == 1
    assert "does not have content/not-yet.md published" in result.output
    assert "draft/not-yet" in run("git", "branch", "--list", "draft/*", cwd=blog)


def test_publish_then_finish(blog):
    start_draft("Two Step")
    run("git", "switch", "-q", "main", cwd=blog)
    runner = CliRunner()
    published = runner.invoke(cli, ["publish", "draft", "two-step"])
    assert published.exit_code == 0, published.output
    assert "post publish finish two-step" in published.output
    assert "git " not in published.output

    finished = runner.invoke(cli, ["publish", "finish", "two-step"])
    assert finished.exit_code == 0, finished.output
    assert run("git", "ls-remote", "--heads", "drafts", cwd=blog) == ""
    assert run("git", "rev-parse", "main", cwd=blog) == run(
        "git", "rev-parse", "origin/main", cwd=blog
    )


def test_publish_refuses_to_overwrite_an_untracked_file(blog):
    start_draft("Collide")
    run("git", "switch", "-q", "main", cwd=blog)
    notes = blog / "content" / "collide.md"
    notes.write_text("Local notes, never committed.\n")

    result = CliRunner().invoke(cli, ["publish", "draft", "collide"])
    assert result.exit_code == 1
    assert "content/collide.md" in result.output
    assert notes.read_text() == "Local notes, never committed.\n"
    assert run("git", "log", "-1", "--format=%s", cwd=blog).strip() == "Initial"


def test_publish_commits_only_the_merged_paths(blog):
    start_draft("Tidy")
    run("git", "switch", "-q", "main", cwd=blog)
    (blog / "content" / "half-written.md").write_text("Not ready.\n")

    result = CliRunner().invoke(cli, ["publish", "draft", "tidy"])
    assert result.exit_code == 0, result.output
    committed = run("git", "show", "--name-only", "--format=", "HEAD", cwd=blog).split()
    assert committed == ["content/tidy.md"]
    assert run("git", "status", "--porcelain", cwd=blog) == "?? content/half-written.md\n"
