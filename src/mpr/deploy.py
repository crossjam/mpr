"""Check that a local deploy target can be synced into and served from."""

import grp
import os
import pwd
import stat
import sys
from dataclasses import dataclass
from pathlib import Path

import click

# How many offending paths to name before summarizing the rest
EXAMPLES = 5


@dataclass(frozen=True)
class Account:
    """A user and every group it belongs to."""

    name: str
    uid: int
    gids: frozenset[int]

    @classmethod
    def lookup(cls, name: str) -> "Account":
        entry = pwd.getpwnam(name)
        return cls(name, entry.pw_uid, frozenset(os.getgrouplist(name, entry.pw_gid)))

    def can(self, mode: int, uid: int, gid: int, want: int) -> bool:
        """
        Whether this account gets `want` (some of 4=r, 2=w, 1=x) on a file
        with the given mode and ownership, by Unix owner/group/other rules.
        """
        if self.uid == 0:
            return True
        if uid == self.uid:
            bits = (mode >> 6) & 7
        elif gid in self.gids:
            bits = (mode >> 3) & 7
        else:
            bits = mode & 7
        return bits & want == want

    def can_path(self, st: os.stat_result, want: int) -> bool:
        return self.can(st.st_mode, st.st_uid, st.st_gid, want)

    def owns_or_shares(self, st: os.stat_result, want: int) -> bool:
        """Like can_path, but only through owner or group bits, never other."""
        return (st.st_uid == self.uid or st.st_gid in self.gids) and self.can_path(st, want)


def owner(st: os.stat_result) -> str:
    try:
        return pwd.getpwuid(st.st_uid).pw_name
    except KeyError:
        return str(st.st_uid)


def group(gid: int) -> str:
    try:
        return grp.getgrgid(gid).gr_name
    except KeyError:
        return str(gid)


def summarize(problem: str, paths: list[Path]) -> str:
    named = ", ".join(str(p) for p in paths[:EXAMPLES])
    more = f" and {len(paths) - EXAMPLES} more" if len(paths) > EXAMPLES else ""
    return f"{problem}: {named}{more}"


def untraversable(target: Path, web: Account) -> list[Path]:
    """The directories above `target` that `web` cannot pass through."""
    return [
        parent
        for parent in reversed(target.resolve().parents)
        if not web.can_path(parent.stat(), 1)
    ]


def check_target(target: Path, deployer: Account, web: Account, umask: int) -> list[str]:
    """
    Everything that would stop `deployer` from rsyncing into `target`, or
    stop `web` from reading the result. An empty list means go ahead.

    rsync runs without --perms, so files it creates take the sender's mode
    masked by the deployer's umask, and files it updates keep their mode.
    New files are judged from a 0644/0755 source under `umask`; existing
    ones from their current mode.
    """
    if not target.exists():
        return [f"{target} does not exist; create it first, owned by the deploying user"]
    if deployer.uid == 0:
        return ["running as root; deploy as an account with owner or group write on the target"]
    if not target.is_dir():
        return [f"{target} is not a directory"]

    problems = []
    target_st = target.stat()

    blocked = untraversable(target, web)
    if blocked:
        problems.append(summarize(f"{web.name} cannot traverse", blocked))

    unwritable = []
    unreadable = []
    # A directory os.walk cannot list hides everything in it from this check
    unscannable: list[Path] = []
    for root, dirs, files in os.walk(
        target, onerror=lambda err: unscannable.append(Path(err.filename))
    ):
        root_path = Path(root)
        root_st = root_path.stat()
        # rsync --delete has to add and remove entries in every directory,
        # and the deploying account gets that from owner or group write only
        if not deployer.owns_or_shares(root_st, 2 | 1):
            unwritable.append(root_path)
        if not web.can_path(root_st, 4 | 1):
            unreadable.append(root_path)
        for name in files:
            path = root_path / name
            if not web.can_path(path.lstat(), 4):
                unreadable.append(path)
        dirs.sort()

    if unscannable:
        problems.append(summarize(f"{deployer.name} cannot scan", unscannable))
    if unwritable:
        problems.append(
            summarize(
                f"{deployer.name} has no owner or group write on (target is "
                f"{owner(target_st)}:{group(target_st.st_gid)}; fix ownership or mode)",
                unwritable,
            )
        )
    if unreadable:
        problems.append(summarize(f"{web.name} cannot read existing", unreadable))

    # New entries belong to the deployer, in the directory's group if it is
    # setgid, otherwise the deployer's own primary group
    new_gid = (
        target_st.st_gid if target_st.st_mode & stat.S_ISGID else pwd.getpwuid(deployer.uid).pw_gid
    )
    for kind, mode, want in (("files", 0o644, 4), ("directories", 0o755, 4 | 1)):
        if not web.can(mode & ~umask, deployer.uid, new_gid, want):
            problems.append(
                f"{web.name} could not read new {kind}: umask {umask:03o} makes them "
                f"{mode & ~umask:03o}, owned by {deployer.name}:{group(new_gid)}"
            )
    return problems


def current_umask() -> int:
    mask = os.umask(0)
    os.umask(mask)
    return mask


@click.command()
@click.argument("target", type=click.Path(path_type=Path))
@click.option(
    "--web-user", default="caddy", show_default=True, help="The account the web server runs as"
)
def cli(target: Path, web_user: str) -> None:
    """Check TARGET before a local deploy rsyncs the site into it."""
    deployer = Account.lookup(pwd.getpwuid(os.geteuid()).pw_name)
    try:
        web = Account.lookup(web_user)
    except KeyError:
        raise click.ClickException(
            f"no user {web_user!r} on this machine; pass the web server's account"
        ) from None

    problems = check_target(target, deployer, web, current_umask())
    if problems:
        for problem in problems:
            click.echo(click.style("✗ ", fg="red") + problem, err=True)
        sys.exit(1)
    click.echo(
        click.style("✓ ", fg="green")
        + f"{target} is writable by {deployer.name} and readable by {web.name}"
    )


if __name__ == "__main__":
    cli()
