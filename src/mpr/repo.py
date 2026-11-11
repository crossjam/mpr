"""Repository access for the post commands, through dulwich.

Each post is written on its own draft/<slug> branch, started from main
and pushed only to the private drafts remote, since origin is public.
"""

import io
import subprocess
from collections.abc import Generator
from contextlib import contextmanager
from pathlib import Path

import click
from dulwich import porcelain
from dulwich.errors import NotGitRepository
from dulwich.object_store import tree_lookup_path
from dulwich.objects import Blob, Commit, ObjectID
from dulwich.refs import HEADREF, Ref
from dulwich.repo import Repo

from . import metadata

BASE_BRANCH = "main"
PUBLIC_REMOTE = "origin"
DRAFTS_REMOTE = "drafts"
DRAFTS_URL = "git@github.com:crossjam/mpr.drafts.git"
# Substring that identifies the drafts repository's URL, as in install-draft-hooks.sh
DRAFTS_URL_PATTERN = "crossjam/mpr.drafts"
DRAFT_PREFIX = "draft/"


def to_ref(name: str) -> Ref:
    return Ref(name.encode())


def head_ref(branch: str) -> Ref:
    return to_ref(f"refs/heads/{branch}")


def commit_at(repo: Repo, sha: ObjectID) -> Commit:
    obj = repo[sha]
    if not isinstance(obj, Commit):
        raise click.ClickException(f"{sha.decode()} is not a commit")
    return obj


def branch_commit(repo: Repo, branch: str) -> Commit:
    """The tip of branch; for main, origin's copy when there is no local one yet."""
    ref = head_ref(branch)
    if branch == BASE_BRANCH and ref not in repo.refs:
        ref = to_ref(f"refs/remotes/{PUBLIC_REMOTE}/{BASE_BRANCH}")
    if ref not in repo.refs:
        raise click.ClickException(f"no branch {branch}")
    return commit_at(repo, repo.refs[ref])


def merge_base(repo: Repo, a: Commit, b: Commit) -> Commit | None:
    bases = porcelain.merge_base(repo, [a.id.decode(), b.id.decode()])
    return commit_at(repo, bases[0]) if bases else None


def blob_data(repo: Repo, sha: ObjectID) -> bytes:
    obj = repo[sha]
    if not isinstance(obj, Blob):
        raise click.ClickException(f"{sha.decode()} is not a file")
    return obj.data


def is_post(path: bytes) -> bool:
    return path.startswith(b"content/") and path.endswith(b".md")


def post_status(repo: Repo, sha: ObjectID) -> str:
    """A post blob's status field, lowercased; empty when it has none."""
    return (metadata.get_field(blob_data(repo, sha).decode(), "status") or "").lower()


@contextmanager
def open_repo() -> Generator[Repo]:
    """The repository or worktree containing the current directory."""
    try:
        repo = Repo.discover()
    except NotGitRepository:
        raise click.ClickException("not inside a git repository") from None
    with repo:
        yield repo


def root(repo: Repo) -> Path:
    return Path(repo.path)


def current_branch(repo: Repo) -> str:
    """The checked-out branch, or an empty string on a detached HEAD."""
    head = repo.refs.read_ref(HEADREF) or b""
    prefix = b"ref: refs/heads/"
    return head.removeprefix(prefix).decode() if head.startswith(prefix) else ""


def ref_exists(repo: Repo, ref: str) -> bool:
    return to_ref(ref) in repo.refs


def require_clean(repo: Repo) -> None:
    """Refuse to continue with uncommitted changes to tracked files."""
    status = porcelain.status(repo, untracked_files="no")
    if any(status.staged.values()) or status.unstaged:
        raise click.ClickException(
            "the working tree has uncommitted changes; commit or stash them first"
        )


def in_tree(repo: Repo, tree: ObjectID, path: str) -> bool:
    try:
        tree_lookup_path(repo.__getitem__, tree, path.encode())
    except KeyError:
        return False
    return True


def on_branch(repo: Repo, branch: str, path: str) -> bool:
    """Whether path exists in the tip of branch."""
    return in_tree(repo, branch_commit(repo, branch).tree, path)


def in_head(repo: Repo, path: str) -> bool:
    """Whether path is tracked in the checked-out commit."""
    return in_tree(repo, commit_at(repo, repo.head()).tree, path)


def remote_url(repo: Repo, remote: str) -> str | None:
    try:
        return repo.get_config().get((b"remote", remote.encode()), b"url").decode()
    except KeyError:
        return None


def fetch(repo: Repo, remote: str) -> None:
    try:
        porcelain.fetch(repo, remote, outstream=io.StringIO(), errstream=io.BytesIO(), quiet=True)
    except Exception as e:
        raise click.ClickException(f"fetching {remote} failed: {e}") from e


def add_remote(repo: Repo, remote: str, url: str) -> None:
    """Add a remote with git's default fetch refspec, which dulwich's remote_add leaves out."""
    porcelain.remote_add(repo, remote, url)
    config = repo.get_config()
    config.set(
        (b"remote", remote.encode()), b"fetch", f"+refs/heads/*:refs/remotes/{remote}/*".encode()
    )
    config.write_to_path()


def track(repo: Repo, branch: str, remote: str) -> None:
    """Set branch's upstream, so a plain pull or push goes to remote."""
    config = repo.get_config()
    section = (b"branch", branch.encode())
    config.set(section, b"remote", remote.encode())
    config.set(section, b"merge", head_ref(branch))
    config.write_to_path()


def base_branch_source(repo: Repo) -> str | None:
    """origin's main when there is no local main yet, to create it from; else None."""
    if ref_exists(repo, f"refs/heads/{BASE_BRANCH}"):
        return None
    tracking = f"refs/remotes/{PUBLIC_REMOTE}/{BASE_BRANCH}"
    if not ref_exists(repo, tracking):
        raise click.ClickException(f"no {BASE_BRANCH} branch here or on {PUBLIC_REMOTE}")
    return tracking


def create_branch(repo: Repo, branch: str, start: str, remote: str) -> None:
    """Create branch at start, tracking remote, as git switch does for a remote branch."""
    porcelain.branch_create(repo, branch, start)
    track(repo, branch, remote)


def draft_branch(name: str) -> str:
    """Accept either a slug or a full draft/<slug> branch name."""
    return name if name.startswith(DRAFT_PREFIX) else DRAFT_PREFIX + name


def draft_slugs(repo: Repo, remote: str | None = None) -> set[str]:
    """Slugs of the local draft branches, or of remote's as last fetched."""
    base = to_ref(f"refs/remotes/{remote}/{DRAFT_PREFIX}") if remote else head_ref(DRAFT_PREFIX)
    return {name.decode() for name in repo.refs.keys(base=base)}


def all_draft_slugs() -> list[str]:
    """Local and drafts-remote slugs, for shell completion; none outside a repository."""
    try:
        with open_repo() as repo:
            return sorted(draft_slugs(repo) | draft_slugs(repo, DRAFTS_REMOTE))
    except click.ClickException:
        return []


def push(repo: Repo, remote: str, branch: str, *, delete: bool = False) -> None:
    """
    Push a branch, or delete it from the remote.

    dulwich does not run the pre-push hook, so its draft guard is
    enforced here: draft branches only ever go to the drafts repository.
    """
    url = remote_url(repo, remote)
    if url is None:
        raise click.ClickException(f"no '{remote}' remote")
    if branch.startswith(DRAFT_PREFIX) and DRAFTS_URL_PATTERN not in url:
        raise click.ClickException(f"refusing to push {branch} to {remote} ({url})")

    errors = io.BytesIO()
    try:
        porcelain.push(
            repo,
            remote,
            [head_ref(branch)],
            outstream=io.BytesIO(),
            errstream=errors,
            delete=delete,
            set_upstream=not delete,
        )
    # dulwich's transports raise many unrelated exception types
    except Exception as e:  # noqa: BLE001
        detail = errors.getvalue().decode(errors="replace").strip()
        raise click.ClickException(f"pushing {branch} to {remote} failed: {e}\n{detail}".rstrip())

    # Keep the remote-tracking ref in step, as git push does
    tracking = to_ref(f"refs/remotes/{remote}/{branch}")
    if delete:
        repo.refs.remove_if_equals(tracking, None)
    else:
        repo.refs[tracking] = repo.refs[head_ref(branch)]


def install_hooks(repo: Repo) -> None:
    """Refresh the draft-branch hook guards, in case another tool rewrote a hook."""
    script = root(repo) / "install-draft-hooks.sh"
    if subprocess.run([str(script)], check=False, cwd=root(repo)).returncode:
        raise click.ClickException("could not install the draft-branch hook guards")
