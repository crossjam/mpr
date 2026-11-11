"""post: start draft branches and publish them onto main."""

import os
import shlex
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import datetime

import click
from dulwich import porcelain
from dulwich.diff_tree import CHANGE_DELETE, tree_changes
from dulwich.merge import three_way_merge
from dulwich.object_store import tree_lookup_path
from dulwich.objects import Commit, ObjectID
from dulwich.repo import Repo
from slugify import slugify

from . import metadata, repo
from .content import post_body, warn
from .repo import BASE_BRANCH, DRAFT_PREFIX, DRAFTS_REMOTE, PUBLIC_REMOTE


class Plan:
    """
    The operations a command performs, each run and reported as it is reached.

    Under --dry-run each one is listed instead. The checks around them still
    run, so a dry run also shows whether the real command would refuse.
    """

    def __init__(self, dry_run: bool):
        self.dry_run = dry_run

    def __call__(self, description: str, action: Callable[[], object]) -> None:
        if self.dry_run:
            click.echo(click.style("would ", fg="cyan") + description)
        else:
            action()
            click.echo(click.style("✓ ", fg="green") + description)

    def fetch(self, r: Repo, remote: str) -> None:
        if self.dry_run:
            click.echo(f"would fetch {remote} (listing what follows as of the last fetch)")
        else:
            self(f"Fetch {remote}", lambda: repo.fetch(r, remote))


def dry_run_option(f):
    return click.option(
        "-n", "--dry-run", is_flag=True, help="List the operations without performing them."
    )(f)


def complete_drafts(ctx, param, incomplete: str) -> list[str]:
    """Shell completion for draft slugs."""
    return [slug for slug in repo.all_draft_slugs() if slug.startswith(incomplete)]


def require_drafts_remote(r: Repo) -> None:
    if repo.remote_url(r, DRAFTS_REMOTE) is None:
        raise click.ClickException(f"no '{DRAFTS_REMOTE}' remote; run: post setup")


def require_draft_branch(r: Repo) -> str:
    """The checked-out branch, which must be a draft."""
    branch = repo.current_branch(r)
    if not branch.startswith(DRAFT_PREFIX):
        raise click.ClickException(
            f"not on a draft branch (on {branch or 'a detached HEAD'}); "
            "switch to one with: post draft switch SLUG"
        )
    return branch


def slug_argument(f):
    return click.argument("name", metavar="SLUG", shell_complete=complete_drafts)(f)


def ensure_main(plan: Plan, r: Repo) -> None:
    """Create a local main from origin's when it is missing, as git switch main would."""
    if source := repo.base_branch_source(r):
        plan(
            f"Create {BASE_BRANCH} from {source.removeprefix('refs/remotes/')}",
            lambda: repo.create_branch(r, BASE_BRANCH, source, PUBLIC_REMOTE),
        )


def switch_to_main(plan: Plan, r: Repo) -> None:
    """Check out main, which publishing works on; the working tree must be clean."""
    repo.require_clean(r)
    ensure_main(plan, r)
    if repo.current_branch(r) != BASE_BRANCH:
        plan(f"Switch to {BASE_BRANCH}", lambda: porcelain.checkout(r, BASE_BRANCH))


def push_draft(plan: Plan, r: Repo, branch: str) -> None:
    """Push a draft branch, warning rather than failing, since the commit is safe locally."""
    try:
        plan(f"Push {branch} to {DRAFTS_REMOTE}", lambda: repo.push(r, DRAFTS_REMOTE, branch))
    except click.ClickException as e:
        warn(f"{e.message}\nThe commit is saved locally; push it later with: post draft save")


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
def cli():
    """Write and publish Mass Programming Resistance posts.

    Each post is written on its own draft/<slug> branch, pushed only to
    the private drafts remote, then squash-merged onto main to publish.
    Every command that changes anything takes --dry-run.
    """


@cli.command()
@dry_run_option
def setup(dry_run):
    """Prepare this clone: add the drafts remote, fetch it, install the hook guards."""
    plan = Plan(dry_run)
    with repo.open_repo() as r:
        if repo.remote_url(r, DRAFTS_REMOTE) is None:
            plan(
                f"Add remote {DRAFTS_REMOTE} ({repo.DRAFTS_URL})",
                lambda: repo.add_remote(r, DRAFTS_REMOTE, repo.DRAFTS_URL),
            )
        plan.fetch(r, DRAFTS_REMOTE)
        plan("Install the draft-branch hook guards", lambda: repo.install_hooks(r))


@cli.group()
def draft():
    """Start, resume, save, and drop draft branches."""


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
@dry_run_option
def draft_new(title, author, slug, source, clipboard, quote, edit, yes, dry_run):
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

    plan = Plan(dry_run)
    with repo.open_repo() as r:
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
        if not (yes or dry_run):
            click.confirm("Create this post?", default=True, abort=True)

        path = repo.root(r) / relpath
        message = f"Start draft: {title}"
        plan("Install the draft-branch hook guards", lambda: repo.install_hooks(r))
        ensure_main(plan, r)
        plan(
            f"Switch to new branch {branch} from {BASE_BRANCH}",
            lambda: porcelain.checkout(r, BASE_BRANCH, new_branch=branch),
        )
        plan(
            f"Write {relpath}",
            lambda: path.write_text(metadata.new_post(title, author, body, datetime.now())),
        )
        if edit:
            plan(f"Open {relpath} in $EDITOR", lambda: open_editor(path))
        plan(f'Commit "{message}"', lambda: commit(r, [str(path)], message))
        push_draft(plan, r, branch)

    if not dry_run:
        click.echo(
            f"\nNext: edit {relpath}, then save it with: post draft save\n"
            f"To publish: post publish draft {shlex.quote(slug)}"
        )


def open_editor(path) -> None:
    try:
        click.edit(filename=str(path))
    except click.ClickException as e:
        warn(f"Could not open an editor ({e.message}); set $EDITOR to choose one")


def commit(r: Repo, paths: list[str], message: str) -> None:
    if paths:
        porcelain.add(r, paths)
    porcelain.commit(r, message=message.encode())


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
@click.option(
    "--update/--no-update",
    default=True,
    show_default=True,
    help=f"Merge {BASE_BRANCH} into the draft after switching.",
)
@dry_run_option
def draft_switch(name, update, dry_run):
    """Check out draft/SLUG, fetching it from the drafts remote if it is not here yet.

    Then, unless --no-update is given, merges main into it as
    `post draft update` does, so the draft builds with the current
    templates and plugins. A conflict leaves the draft as it was.
    """
    branch = repo.draft_branch(name)
    plan = Plan(dry_run)
    with repo.open_repo() as r:
        repo.require_clean(r)
        # Files tracked here are the checkout's to deal with, not untracked ones in the way
        before = repo.commit_at(r, r.head()).tree
        tip = f"refs/heads/{branch}"
        if not repo.ref_exists(r, tip):
            require_drafts_remote(r)
            plan.fetch(r, DRAFTS_REMOTE)
            tip = f"refs/remotes/{DRAFTS_REMOTE}/{branch}"
            if not repo.ref_exists(r, tip):
                raise click.ClickException(f"no draft {branch} here or on {DRAFTS_REMOTE}")
            plan(
                f"Create {branch} from {DRAFTS_REMOTE}",
                lambda: repo.create_branch(r, branch, tip, DRAFTS_REMOTE),
            )
        plan(f"Switch to {branch}", lambda: porcelain.checkout(r, branch))
        if update:
            tip_commit = repo.commit_at(r, r.refs[repo.to_ref(tip)])
            try:
                update_draft(plan, r, branch, tip_commit, [before])
            except click.ClickException as e:
                switched = "Would switch" if dry_run else "Switched"
                warn(f"{e.message}\n{switched} to {branch} without updating it")


def update_draft(
    plan: Plan, r: Repo, branch: str, tip: Commit, tracked: list[ObjectID] | None = None
) -> None:
    """
    Merge main into the checked-out draft, then push it; tip is the draft's commit.

    The merge is worked out in memory first, so a conflict changes nothing.
    Paths in the tracked trees, besides the draft's own, may be written over.
    """
    warn_if_main_behind(plan, r)
    main = repo.branch_commit(r, BASE_BRANCH)
    base = repo.merge_base(r, tip, main)
    if base is not None and base.id == main.id:
        click.echo(f"{branch} is up to date with {BASE_BRANCH}")
        return
    merged, conflicts = three_way_merge(r.object_store, base, tip, main)
    if conflicts:
        names = ", ".join(path.decode() for path in conflicts)
        raise click.ClickException(
            f"{BASE_BRANCH} conflicts with {branch} in {names}; nothing was changed"
        )
    # The merge stores the subtrees it builds, but not the root tree
    r.object_store.add_object(merged)

    writes, removes = {}, []
    for change in tree_changes(r.object_store, tip.tree, merged.id):
        new, old = change.new, change.old
        if change.type == CHANGE_DELETE or new is None:
            if old is not None:
                removes.append(old.path.decode())
        else:
            writes[new.path.decode()] = (repo.blob_data(r, new.sha), new.mode)
    refuse_blocked_writes(r, list(writes), f"merging {BASE_BRANCH}", [tip.tree, *(tracked or [])])

    for path, (data, mode) in writes.items():
        plan(f"Write {path}", lambda p=path, d=data, m=mode: write_file(r, p, d, m))
    for path in removes:
        plan(f"Remove {path}", lambda p=path: porcelain.remove(r, [str(repo.root(r) / p)]))
    message = f"Merge {BASE_BRANCH} into {branch}"
    plan(
        f'Commit "{message}"',
        lambda: r.get_worktree().commit(message=message.encode(), merge_heads=[main.id]),
    )
    push_draft(plan, r, branch)


def warn_if_main_behind(plan: Plan, r: Repo) -> None:
    """Fetch origin, then warn when its main has commits the local main lacks."""
    try:
        plan.fetch(r, PUBLIC_REMOTE)
    except click.ClickException as e:
        warn(f"{e.message}\nChecking {BASE_BRANCH} against {PUBLIC_REMOTE} as last fetched")
    tracking = f"refs/remotes/{PUBLIC_REMOTE}/{BASE_BRANCH}"
    if behind := repo.commits_missing(r, tracking, f"refs/heads/{BASE_BRANCH}"):
        commits = "commit" if behind == 1 else "commits"
        warn(
            f"WARNING: {PUBLIC_REMOTE}/{BASE_BRANCH} has {behind} {commits} that local "
            f"{BASE_BRANCH} does not; pull them into {BASE_BRANCH} first, "
            "or the draft will not get them"
        )


@draft.command("update")
@dry_run_option
def draft_update(dry_run):
    """Merge main into the current draft and push it to the drafts remote.

    Keeps the draft building with main's current templates, plugins, and
    dependencies. The merge is worked out in memory first, so a conflict
    changes nothing.
    """
    plan = Plan(dry_run)
    with repo.open_repo() as r:
        branch = require_draft_branch(r)
        require_drafts_remote(r)
        repo.require_clean(r)
        update_draft(plan, r, branch, repo.commit_at(r, r.head()))


@draft.command("save")
@click.option("-m", "--message", default="Update draft", show_default=True, help="Commit message.")
@dry_run_option
def draft_save(message, dry_run):
    """Commit the current draft's changes and push it to the drafts remote.

    Commits changes to tracked files and any new files under content/,
    then pushes, even when there is nothing new to commit, so this also
    retries a push that failed earlier.
    """
    plan = Plan(dry_run)
    with repo.open_repo() as r:
        branch = require_draft_branch(r)
        require_drafts_remote(r)

        top = repo.root(r)
        status = porcelain.status(r)
        changed = [p.decode() for p in status.unstaged]
        # dulwich lists a tracked symlink to a directory as an untracked "dir/"; skip those
        changed += [
            name
            for name in (p.decode() for p in status.untracked if p.startswith(b"content/"))
            if not repo.in_head(r, name.rstrip("/"))
        ]
        present = [p for p in changed if (top / p).exists()]
        missing = [p for p in changed if not (top / p).exists()]

        if any(status.staged.values()) or changed:
            for p in present:
                plan(f"Stage {p}", lambda p=p: porcelain.add(r, [str(top / p)]))
            for p in missing:
                plan(
                    f"Stage the removal of {p}",
                    lambda p=p: porcelain.remove(r, [str(top / p)], cached=True),
                )
            plan(f'Commit "{message}"', lambda: commit(r, [], message))
        else:
            click.echo("Nothing new to commit")
        push_draft(plan, r, branch)


def is_pushed(r: Repo, branch: str) -> bool:
    """Whether every commit on the local branch is on the drafts remote, as last fetched."""
    tracking = f"refs/remotes/{DRAFTS_REMOTE}/{branch}"
    if not repo.ref_exists(r, tracking):
        return False
    tip = r.refs[repo.head_ref(branch)]
    return porcelain.merge_base(r, [tip.decode(), r.refs[repo.to_ref(tracking)].decode()]) == [tip]


@draft.command("drop")
@slug_argument
@click.option("--force", is_flag=True, help=f"Drop even with commits not on {DRAFTS_REMOTE}.")
@click.option("-y", "--yes", is_flag=True, help="Drop without asking to confirm.")
@dry_run_option
def draft_drop(name, force, yes, dry_run):
    """Delete draft/SLUG here and on the drafts remote, abandoning the post.

    Refuses when the local branch has commits that were never pushed,
    unless --force is given. On the draft itself, it switches to main
    first, so the working tree must be clean.
    """
    branch = repo.draft_branch(name)
    plan = Plan(dry_run)
    with repo.open_repo() as r:
        require_drafts_remote(r)
        plan.fetch(r, DRAFTS_REMOTE)
        local = repo.ref_exists(r, f"refs/heads/{branch}")
        remote = repo.ref_exists(r, f"refs/remotes/{DRAFTS_REMOTE}/{branch}")
        if not (local or remote):
            raise click.ClickException(f"no draft {branch} here or on {DRAFTS_REMOTE}")
        if local and not force and not is_pushed(r, branch):
            raise click.ClickException(
                f"{branch} has commits that are not on {DRAFTS_REMOTE}; "
                "save them with post draft save, or pass --force to drop them anyway"
            )

        where = " and ".join(
            w for w, present in (("here", local), (f"on {DRAFTS_REMOTE}", remote)) if present
        )
        if not (yes or dry_run):
            click.confirm(f"Delete {branch} {where}? This cannot be undone.", abort=True)

        if repo.current_branch(r) == branch:
            switch_to_main(plan, r)
        if remote:
            plan(
                f"Delete {branch} on {DRAFTS_REMOTE}",
                lambda: repo.push(r, DRAFTS_REMOTE, branch, delete=True),
            )
        if local:
            plan(f"Delete local branch {branch}", lambda: porcelain.branch_delete(r, branch))


@cli.group()
def publish():
    """Publish draft branches onto main."""


@dataclass
class Squash:
    """What squash-merging a draft onto main writes, computed without touching the tree."""

    # path -> (content, mode) for every file the merge adds or changes
    writes: dict[str, tuple[bytes, int]] = field(default_factory=dict)
    removes: list[str] = field(default_factory=list)
    # The draft posts among the writes, already marked published
    posts: list[str] = field(default_factory=list)
    titles: list[str] = field(default_factory=list)


def plan_squash(r: Repo, branch: str, redate: bool, now: datetime) -> Squash:
    """
    Work out the squash merge of branch onto main, entirely in memory.

    Refuses on a conflict, when the draft has no post marked draft, or when
    writing would clobber an untracked file or leave the repository.
    """
    ours = repo.branch_commit(r, BASE_BRANCH)
    theirs = repo.branch_commit(r, branch)
    merged, conflicts = three_way_merge(
        r.object_store, repo.merge_base(r, ours, theirs), ours, theirs
    )
    if conflicts:
        names = ", ".join(path.decode() for path in conflicts)
        raise click.ClickException(
            f"{branch} conflicts with {BASE_BRANCH} in {names}; nothing was changed"
        )
    # The merge stores the subtrees it builds, but not the root tree
    r.object_store.add_object(merged)

    squash = Squash()
    for change in tree_changes(r.object_store, ours.tree, merged.id):
        new, old = change.new, change.old
        if change.type == CHANGE_DELETE or new is None:
            if old is not None:
                squash.removes.append(old.path.decode())
            continue
        name = new.path.decode()
        data = repo.blob_data(r, new.sha)
        if repo.is_post(new.path) and repo.post_status(r, new.sha) == "draft":
            text = metadata.publish_text(data.decode(), redate, now)
            data = text.encode()
            squash.posts.append(name)
            squash.titles.append(metadata.title_of(text) or name)
        squash.writes[name] = (data, new.mode)
    if not squash.posts:
        raise click.ClickException(f"{branch} has no post marked status: draft under content/")

    # A file tracked in the current checkout is not untracked: switching to main deals with it
    tracked = [ours.tree, repo.commit_at(r, r.head()).tree]
    refuse_blocked_writes(r, list(squash.writes), f"publishing {branch}", tracked)
    return squash


def refuse_blocked_writes(r: Repo, names: list[str], doing: str, tracked: list[ObjectID]) -> None:
    """
    Refuse writes over untracked files, or through a symlink that leads out of the tree.

    A path in any of the tracked trees is not untracked, so it is fair to write.
    """
    top = repo.root(r)
    # The clean check ignores untracked files, so refuse to write over one, as git merge
    # does; lexists so that a dangling symlink counts too
    untracked = [
        name
        for name in names
        if not any(repo.in_tree(r, tree, name) for tree in tracked) and os.path.lexists(top / name)
    ]
    # Never write through a symlink, at the path or any parent, that leads out of the tree
    inside = top.resolve()
    escaping = [name for name in names if not (top / name).resolve().is_relative_to(inside)]
    for name in escaping:
        warn(f"WARNING: {name} resolves outside the repository, to {(top / name).resolve()}")
    if blocked := sorted(set(untracked) | set(escaping)):
        raise click.ClickException(
            f"{doing} would write over untracked or outside paths "
            f"{', '.join(blocked)}; move or remove them first; nothing was changed"
        )


def write_file(r: Repo, name: str, data: bytes, mode: int) -> None:
    dest = repo.root(r) / name
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)
    dest.chmod(0o755 if mode & 0o100 else 0o644)
    porcelain.add(r, [str(dest)])


def unpublished_posts(r: Repo, branch: str) -> list[str]:
    """Posts the branch adds or changes that main does not carry as published."""
    tip = repo.branch_commit(r, branch)
    main = repo.branch_commit(r, BASE_BRANCH)
    base = repo.merge_base(r, main, tip)
    missing = []
    for change in tree_changes(r.object_store, base.tree if base else None, tip.tree):
        new = change.new
        if change.type == CHANGE_DELETE or new is None or not repo.is_post(new.path):
            continue
        try:
            _, sha = tree_lookup_path(r.__getitem__, main.tree, new.path)
        except KeyError:
            missing.append(new.path.decode())
            continue
        if repo.post_status(r, sha) != "published":
            missing.append(new.path.decode())
    return missing


def finish(plan: Plan, r: Repo, branch: str, *, check: bool = True) -> None:
    """Push main, then delete the published draft branch on the drafts remote and here."""
    if check and (unpublished := unpublished_posts(r, branch)):
        raise click.ClickException(
            f"{BASE_BRANCH} does not have {', '.join(unpublished)} published yet; "
            f"publish it first with: post publish draft {branch.removeprefix(DRAFT_PREFIX)}"
        )
    plan(f"Push {BASE_BRANCH} to {PUBLIC_REMOTE}", lambda: repo.push(r, PUBLIC_REMOTE, BASE_BRANCH))
    if repo.ref_exists(r, f"refs/remotes/{DRAFTS_REMOTE}/{branch}"):
        plan(
            f"Delete {branch} on {DRAFTS_REMOTE}",
            lambda: repo.push(r, DRAFTS_REMOTE, branch, delete=True),
        )
    plan(f"Delete local branch {branch}", lambda: porcelain.branch_delete(r, branch))
    if not plan.dry_run:
        click.echo("\nNext: deploy with uv run poe rsync_upload")


@publish.command("draft")
@slug_argument
@click.option("--redate", is_flag=True, help="Date the post now, replacing any date it has.")
@click.option("--push", is_flag=True, help="Also finish: push main and delete the draft branch.")
@dry_run_option
def publish_draft(name, redate, push, dry_run):
    """Publish draft/SLUG onto main, switching to main first.

    Squash-merges the branch, so the draft's revision history never
    reaches the public repository. Each draft post it adds is marked
    status: published and dated now if it has no date, then the result
    is committed as "Publish <title>". With --push, it then finishes as
    `post publish finish` does.
    """
    branch = repo.draft_branch(name)
    plan = Plan(dry_run)
    with repo.open_repo() as r:
        if not repo.ref_exists(r, f"refs/heads/{branch}"):
            raise click.ClickException(
                f"no local branch {branch}; get it with: post draft switch {name}"
            )
        switch_to_main(plan, r)
        squash = plan_squash(r, branch, redate, datetime.now())

        # Stage only what the merge produced, never other untracked files
        for path, (data, mode) in squash.writes.items():
            label = f"Write {path}" + (", marked published" if path in squash.posts else "")
            plan(label, lambda p=path, d=data, m=mode: write_file(r, p, d, m))
        for path in squash.removes:
            plan(
                f"Remove {path}",
                lambda p=path: porcelain.remove(r, [str(repo.root(r) / p)]),
            )
        message = f"Publish {', '.join(squash.titles)}"
        plan(f'Commit "{message}" on {BASE_BRANCH}', lambda: commit(r, [], message))

        if push:
            finish(plan, r, branch, check=not dry_run)
        elif not dry_run:
            click.echo(
                f"\nNext: post publish finish {shlex.quote(branch.removeprefix(DRAFT_PREFIX))}"
            )


@publish.command("finish")
@slug_argument
@dry_run_option
def publish_finish(name, dry_run):
    """Push main and delete the published draft/SLUG, here and on the drafts remote.

    Refuses unless main already carries the draft's posts as published,
    so an unpublished draft is never deleted.
    """
    branch = repo.draft_branch(name)
    plan = Plan(dry_run)
    with repo.open_repo() as r:
        if not repo.ref_exists(r, f"refs/heads/{branch}"):
            raise click.ClickException(f"no local branch {branch}")
        switch_to_main(plan, r)
        finish(plan, r, branch)
