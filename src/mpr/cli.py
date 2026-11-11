"""post: start draft branches and publish them onto main."""

import shlex
from datetime import datetime
from pathlib import Path

import click
from dulwich import porcelain
from dulwich.diff_tree import CHANGE_DELETE, tree_changes
from dulwich.merge import three_way_merge
from dulwich.object_store import tree_lookup_path
from dulwich.repo import Repo
from slugify import slugify

from . import metadata, repo
from .content import post_body, warn
from .repo import BASE_BRANCH, DRAFT_PREFIX, DRAFTS_REMOTE, PUBLIC_REMOTE


def done(message: str) -> None:
    click.echo(click.style("✓ ", fg="green") + message)


def complete_drafts(ctx, param, incomplete: str) -> list[str]:
    """Shell completion for draft slugs."""
    return [slug for slug in repo.all_draft_slugs() if slug.startswith(incomplete)]


def require_drafts_remote(r: Repo) -> None:
    if repo.remote_url(r, DRAFTS_REMOTE) is None:
        raise click.ClickException(f"no '{DRAFTS_REMOTE}' remote; run: post setup")


def slug_argument(f):
    return click.argument("name", metavar="SLUG", shell_complete=complete_drafts)(f)


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
def cli():
    """Write and publish Mass Programming Resistance posts.

    Each post is written on its own draft/<slug> branch, pushed only to
    the private drafts remote, then squash-merged onto main to publish.
    """


@cli.command()
def setup():
    """Prepare this clone: add the drafts remote, fetch it, install the hook guards."""
    with repo.open_repo() as r:
        if repo.remote_url(r, DRAFTS_REMOTE) is None:
            porcelain.remote_add(r, DRAFTS_REMOTE, repo.DRAFTS_URL)
            done(f"Added remote {DRAFTS_REMOTE} ({repo.DRAFTS_URL})")
        repo.fetch(r, DRAFTS_REMOTE)
        done(f"Fetched {DRAFTS_REMOTE}")
        repo.install_hooks(r)
        done("Installed the draft-branch hook guards")


@cli.group()
def draft():
    """Start, resume, and save draft branches."""


@draft.command("new")
@click.option("-t", "--title", prompt=True, help="Post title (prompted if omitted).")
@click.option("-a", "--author", default="C. Ross Jam", show_default=True, help="Post author.")
@click.option("-s", "--slug", help="URL slug  [default: the slugified title]")
@click.option(
    "-f",
    "--file",
    "source",
    metavar="FILE",
    type=click.File(encoding="utf-8", errors="replace"),
    help="Read the post body from FILE ('-' for stdin).",
)
@click.option(
    "-c", "--clipboard", is_flag=True, help="Take the post body from the macOS clipboard."
)
@click.option("-q", "--quote", is_flag=True, help="Format the body as a Markdown blockquote.")
@click.option(
    "-e", "--edit", is_flag=True, help="Open the post in $EDITOR before the first commit."
)
@click.option("-y", "--yes", is_flag=True, help="Create the post without asking to confirm.")
def draft_new(title, author, slug, source, clipboard, quote, edit, yes):
    """Start a post on a new draft/<slug> branch.

    Creates the branch from main, writes content/<slug>.md marked
    status: draft, commits it, and pushes the branch to the drafts remote.
    The body comes from --file or --clipboard, or is Lorem Ipsum
    placeholder text. When the body comes from stdin, pass --title and
    --yes so no prompt competes for it.
    """
    if source is not None and clipboard:
        raise click.UsageError("use --file or --clipboard, not both")

    slug = slugify(slug or title)
    if not slug:
        raise click.ClickException("the slug is empty after slugify; use letters or digits")
    branch = repo.draft_branch(slug)
    relpath = f"content/{slug}.md"

    with repo.open_repo() as r:
        repo.install_hooks(r)
        repo.require_clean(r)
        for ref in (f"refs/heads/{branch}", f"refs/remotes/{DRAFTS_REMOTE}/{branch}"):
            if repo.ref_exists(r, ref):
                raise click.ClickException(
                    f"{ref} already exists; to resume it: post draft switch {shlex.quote(slug)}"
                )
        if repo.on_branch(r, BASE_BRANCH, relpath):
            raise click.ClickException(f"{relpath} is already a published post on {BASE_BRANCH}")
        require_drafts_remote(r)

        body = post_body(source, clipboard, quote)

        preview = body[:100] + ("..." if len(body) > 100 else "")
        click.echo(f"\nTitle:   {title}\nAuthor:  {author}\nBranch:  {branch} (from {BASE_BRANCH})")
        click.echo(f"File:    {relpath}\nContent: {preview}\n")
        if not yes:
            click.confirm("Create this post?", default=True, abort=True)

        porcelain.checkout(r, BASE_BRANCH, new_branch=branch)
        done(f"Switched to new branch {branch}")

        path = repo.root(r) / relpath
        path.write_text(metadata.new_post(title, author, body, datetime.now()))
        done(f"Created {relpath}")

        if edit:
            try:
                click.edit(filename=str(path))
            except click.ClickException as e:
                warn(f"Could not open an editor ({e.message}); set $EDITOR to choose one")

        porcelain.add(r, [str(path)])
        porcelain.commit(r, message=f"Start draft: {title}".encode())
        push_draft(r, branch)

    click.echo(
        f"\nNext: edit {relpath}, then save it with: post draft save\n"
        f"To publish, from {BASE_BRANCH}: post publish draft {shlex.quote(slug)}"
    )


def push_draft(r: Repo, branch: str) -> None:
    """Push a draft branch, warning rather than failing, since the commit is safe locally."""
    try:
        repo.push(r, DRAFTS_REMOTE, branch)
    except click.ClickException as e:
        warn(f"{e.message}\nThe commit is saved locally; push it later with: post draft save")
    else:
        done(f"Pushed {branch} to {DRAFTS_REMOTE}")


@draft.command("list")
@click.option(
    "--fetch/--no-fetch", default=True, show_default=True, help=f"Fetch {DRAFTS_REMOTE} first."
)
def draft_list(fetch):
    """List drafts, here and on the drafts remote."""
    with repo.open_repo() as r:
        if fetch:
            require_drafts_remote(r)
            repo.fetch(r, DRAFTS_REMOTE)
        local, remote = repo.draft_slugs(r), repo.draft_slugs(r, DRAFTS_REMOTE)
        current = repo.current_branch(r).removeprefix(DRAFT_PREFIX)
        for slug in sorted(local | remote):
            where = ", ".join(
                label
                for label, present in (("local", slug in local), (DRAFTS_REMOTE, slug in remote))
                if present
            )
            marker = "*" if slug == current and slug in local else " "
            click.echo(f"{marker} {slug}  ({where})")


@draft.command("switch")
@slug_argument
def draft_switch(name):
    """Check out draft/SLUG, fetching it from the drafts remote if it is not here yet."""
    branch = repo.draft_branch(name)
    with repo.open_repo() as r:
        repo.require_clean(r)
        if not repo.ref_exists(r, f"refs/heads/{branch}"):
            require_drafts_remote(r)
            repo.fetch(r, DRAFTS_REMOTE)
            tracking = f"refs/remotes/{DRAFTS_REMOTE}/{branch}"
            if not repo.ref_exists(r, tracking):
                raise click.ClickException(f"no draft {branch} here or on {DRAFTS_REMOTE}")
            porcelain.branch_create(r, branch, tracking)
            repo.track(r, branch, DRAFTS_REMOTE)
            done(f"Created {branch} from {DRAFTS_REMOTE}")
        porcelain.checkout(r, branch)
        done(f"Switched to {branch}")


@draft.command("save")
@click.option("-m", "--message", default="Update draft", show_default=True, help="Commit message.")
def draft_save(message):
    """Commit the current draft's changes and push it to the drafts remote.

    Commits changes to tracked files and any new files under content/,
    then pushes, even when there is nothing new to commit, so this also
    retries a push that failed earlier.
    """
    with repo.open_repo() as r:
        branch = repo.current_branch(r)
        if not branch.startswith(DRAFT_PREFIX):
            raise click.ClickException(
                f"not on a draft branch (on {branch or 'a detached HEAD'}); "
                "switch to one with: post draft switch SLUG"
            )
        require_drafts_remote(r)

        top = repo.root(r)
        status = porcelain.status(r)
        changed = [p.decode() for p in status.unstaged]
        changed += [p.decode() for p in status.untracked if p.startswith(b"content/")]
        present = [str(top / p) for p in changed if (top / p).exists()]
        missing = [str(top / p) for p in changed if not (top / p).exists()]
        if present:
            porcelain.add(r, present)
        if missing:
            porcelain.remove(r, missing, cached=True)

        status = porcelain.status(r, untracked_files="no")
        if any(status.staged.values()):
            sha = porcelain.commit(r, message=message.encode())
            done(f"Committed {sha[:7].decode()} {message}")
        else:
            click.echo("Nothing new to commit")
        push_draft(r, branch)


@cli.group()
def publish():
    """Publish draft branches onto main."""


def squash_merge(r: Repo, branch: str) -> list[Path]:
    """
    Squash-merge the branch into the working tree and index, without committing.

    The merge is computed in memory first, so a conflict leaves everything
    untouched. Returns the draft posts the merge adds or changes.
    """
    ours = repo.branch_commit(r, BASE_BRANCH)
    theirs = repo.branch_commit(r, branch)
    bases = porcelain.merge_base(r, [BASE_BRANCH, branch])
    base = repo.commit_at(r, bases[0]) if bases else None
    merged, conflicts = three_way_merge(r.object_store, base, ours, theirs)
    if conflicts:
        names = ", ".join(path.decode() for path in conflicts)
        raise click.ClickException(
            f"{branch} conflicts with {BASE_BRANCH} in {names}; nothing was changed"
        )
    # The merge stores the subtrees it builds, but not the root tree
    r.object_store.add_object(merged)

    # Added or modified files are (path, sha, mode); deleted ones just a path
    updated, deleted = [], []
    for change in tree_changes(r.object_store, ours.tree, merged.id):
        new, old = change.new, change.old
        if change.type == CHANGE_DELETE or new is None:
            if old is not None:
                deleted.append(old.path)
        else:
            updated.append((new.path, new.sha, new.mode))

    posts = [
        path.decode()
        for path, sha, _ in updated
        if repo.is_post(path) and repo.post_status(r, sha) == "draft"
    ]
    if not posts:
        raise click.ClickException(f"{branch} has no post marked status: draft under content/")

    top = repo.root(r)
    written = []
    for path, sha, mode in updated:
        dest = top / path.decode()
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(repo.blob_data(r, sha))
        dest.chmod(0o755 if mode & 0o100 else 0o644)
        written.append(str(dest))
    removed = [str(top / path.decode()) for path in deleted]
    if written:
        porcelain.add(r, written)
    if removed:
        porcelain.remove(r, removed)

    return [top / post for post in posts]


def unpublished_posts(r: Repo, branch: str) -> list[str]:
    """Posts the branch adds or changes that main does not carry as published."""
    tip = repo.branch_commit(r, branch)
    bases = porcelain.merge_base(r, [BASE_BRANCH, branch])
    base_tree = repo.commit_at(r, bases[0]).tree if bases else None
    main_tree = repo.branch_commit(r, BASE_BRANCH).tree
    missing = []
    for change in tree_changes(r.object_store, base_tree, tip.tree):
        new = change.new
        if change.type == CHANGE_DELETE or new is None or not repo.is_post(new.path):
            continue
        try:
            _, sha = tree_lookup_path(r.__getitem__, main_tree, new.path)
        except KeyError:
            missing.append(new.path.decode())
            continue
        if repo.post_status(r, sha) != "published":
            missing.append(new.path.decode())
    return missing


def finish(r: Repo, branch: str) -> None:
    """Push main, then delete the published draft branch on the drafts remote and here."""
    if unpublished := unpublished_posts(r, branch):
        raise click.ClickException(
            f"{BASE_BRANCH} does not have {', '.join(unpublished)} published yet; "
            f"publish it first with: post publish draft {branch.removeprefix(DRAFT_PREFIX)}"
        )
    repo.push(r, PUBLIC_REMOTE, BASE_BRANCH)
    done(f"Pushed {BASE_BRANCH} to {PUBLIC_REMOTE}")
    if repo.ref_exists(r, f"refs/remotes/{DRAFTS_REMOTE}/{branch}"):
        repo.push(r, DRAFTS_REMOTE, branch, delete=True)
        done(f"Deleted {branch} on {DRAFTS_REMOTE}")
    porcelain.branch_delete(r, branch)
    done(f"Deleted local branch {branch}")
    click.echo("\nNext: deploy with uv run poe rsync_upload")


def switch_to_main(r: Repo) -> None:
    """Check out main, which publishing works on; the working tree must be clean."""
    repo.require_clean(r)
    if repo.current_branch(r) != BASE_BRANCH:
        porcelain.checkout(r, BASE_BRANCH)
        done(f"Switched to {BASE_BRANCH}")


@publish.command("draft")
@slug_argument
@click.option("--redate", is_flag=True, help="Date the post now, replacing any date it has.")
@click.option("--push", is_flag=True, help="Also finish: push main and delete the draft branch.")
def publish_draft(name, redate, push):
    """Publish draft/SLUG onto main, switching to main first.

    Squash-merges the branch, so the draft's revision history never
    reaches the public repository. Each draft post it adds is marked
    status: published and dated now if it has no date, then the result
    is committed as "Publish <title>". With --push, it then finishes as
    `post publish finish` does.
    """
    branch = repo.draft_branch(name)
    with repo.open_repo() as r:
        switch_to_main(r)
        if not repo.ref_exists(r, f"refs/heads/{branch}"):
            raise click.ClickException(
                f"no local branch {branch}; get it with: post draft switch {name}"
            )

        top = repo.root(r)
        now = datetime.now()
        titles = []
        for path in squash_merge(r, branch):
            text = metadata.publish_text(path.read_text(), redate, now)
            path.write_text(text)
            titles.append(metadata.title_of(text) or path.stem)
            done(f"Published {path.relative_to(top)}")
        porcelain.add(r, [str(top / "content")])

        message = f"Publish {', '.join(titles)}"
        sha = porcelain.commit(r, message=message.encode())
        done(f"Committed on {BASE_BRANCH}: {sha[:7].decode()} {message}")

        if push:
            finish(r, branch)
        else:
            slug = shlex.quote(branch.removeprefix(DRAFT_PREFIX))
            click.echo(f"\nNext: post publish finish {slug}")


@publish.command("finish")
@slug_argument
def publish_finish(name):
    """Push main and delete the published draft/SLUG, here and on the drafts remote.

    Refuses unless main already carries the draft's posts as published,
    so an unpublished draft is never deleted.
    """
    branch = repo.draft_branch(name)
    with repo.open_repo() as r:
        switch_to_main(r)
        if not repo.ref_exists(r, f"refs/heads/{branch}"):
            raise click.ClickException(f"no local branch {branch}")
        finish(r, branch)
