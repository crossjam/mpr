"""The local deploy target check, against directories under tmp_path."""

import os
import pwd

import pytest
from click.testing import CliRunner

from mpr import deploy
from mpr.deploy import Account, check_target, cli, untraversable

# A web server account that owns nothing here, so only "other" bits apply
WEB = Account("www", uid=99999, gids=frozenset({99999}))


@pytest.fixture(autouse=True)
def traversable(monkeypatch):
    """
    The temp directory's ancestors are private to the test user, so WEB
    could never reach anything under them. Tests of everything but that
    pretend it can; test_untraversable_parent checks the real thing.
    """
    monkeypatch.setattr(deploy, "untraversable", lambda target, web: [])


@pytest.fixture
def deployer():
    return Account.lookup(pwd.getpwuid(os.getuid()).pw_name)


@pytest.fixture
def target(tmp_path):
    site = tmp_path / "site"
    (site / "2026").mkdir(parents=True)
    (site / "index.html").write_text("hi")
    (site / "2026" / "post.html").write_text("post")
    for path in (tmp_path, site, site / "2026"):
        path.chmod(0o755)
    for path in (site / "index.html", site / "2026" / "post.html"):
        path.chmod(0o644)
    yield site
    # Let pytest clean up whatever a test locked down
    for root, dirs, _ in os.walk(tmp_path):
        for name in dirs:
            os.chmod(os.path.join(root, name), 0o755)


@pytest.mark.parametrize(
    ("mode", "uid", "gid", "want", "expected"),
    [
        (0o640, 1, 99999, 4, True),  # group read via membership
        (0o640, 1, 1, 4, False),  # no other read
        (0o604, 1, 1, 4, True),  # other read
        (0o400, 99999, 1, 4, True),  # owner read
        (0o700, 99999, 1, 4 | 1, True),
        (0o711, 1, 1, 4 | 1, False),  # traverse but not list
    ],
)
def test_account_permission_rules(mode, uid, gid, want, expected):
    assert WEB.can(mode, uid, gid, want) is expected


def fake_stat(mode, uid, gid):
    return os.stat_result((mode, 0, 0, 1, uid, gid, 0, 0, 0, 0))


@pytest.mark.parametrize(
    ("mode", "uid", "gid", "expected"),
    [
        (0o755, 99999, 1, True),  # owner write
        (0o775, 1, 99999, True),  # group write
        (0o755, 1, 99999, False),  # group without write
        (0o777, 1, 1, False),  # world-writable does not count
    ],
)
def test_deployer_writes_only_as_owner_or_group(mode, uid, gid, expected):
    assert WEB.owns_or_shares(fake_stat(mode, uid, gid), 2 | 1) is expected


def test_running_as_root_fails(target):
    [problem] = check_target(target, Account("root", 0, frozenset({0})), WEB, 0o022)
    assert "running as root" in problem


def test_root_can_do_anything():
    assert Account("root", 0, frozenset({0})).can(0o000, 1, 1, 7)


def test_readable_writable_target_passes(target, deployer):
    assert check_target(target, deployer, WEB, 0o022) == []


def test_missing_target_fails(tmp_path, deployer):
    [problem] = check_target(tmp_path / "nope", deployer, WEB, 0o022)
    assert "does not exist" in problem


def test_file_target_fails(target, deployer):
    [problem] = check_target(target / "index.html", deployer, WEB, 0o022)
    assert "not a directory" in problem


def test_unwritable_subdirectory_fails(target, deployer):
    (target / "2026").chmod(0o555)
    [problem] = check_target(target, deployer, WEB, 0o022)
    assert "no owner or group write" in problem
    assert str(target / "2026") in problem


def test_unreadable_existing_file_fails(target, deployer):
    (target / "index.html").chmod(0o600)
    [problem] = check_target(target, deployer, WEB, 0o022)
    assert "cannot read existing" in problem
    assert str(target / "index.html") in problem


def test_untraversable_parent(target, deployer):
    target.parent.chmod(0o750)
    assert target.parent.resolve() in untraversable(target, WEB)
    assert untraversable(target, deployer) == []


def test_untraversable_parent_fails(target, deployer, monkeypatch):
    monkeypatch.setattr(deploy, "untraversable", lambda target, web: [target.parent])
    [problem] = check_target(target, deployer, WEB, 0o022)
    assert "cannot traverse" in problem
    assert str(target.parent) in problem


def test_restrictive_umask_fails(target, deployer):
    problems = check_target(target, deployer, WEB, 0o027)
    assert any("new files" in p and "640" in p for p in problems)
    assert any("new directories" in p and "750" in p for p in problems)


def test_long_lists_are_summarized(target, deployer):
    for n in range(8):
        (target / f"locked{n}.html").write_text("x")
        (target / f"locked{n}.html").chmod(0o600)
    [problem] = check_target(target, deployer, WEB, 0o022)
    assert problem.endswith("and 3 more")


def test_cli_unknown_web_user(target):
    result = CliRunner().invoke(cli, [str(target), "--web-user", "no-such-user-here"])
    assert result.exit_code == 1
    assert "no user 'no-such-user-here'" in result.output


def test_cli_reports_success(target, deployer):
    result = CliRunner().invoke(cli, [str(target), "--web-user", deployer.name])
    assert result.exit_code == 0, result.output
    assert "is writable by" in result.output


def test_cli_reports_problems(tmp_path, deployer):
    result = CliRunner().invoke(cli, [str(tmp_path / "nope"), "--web-user", deployer.name])
    assert result.exit_code == 1
    assert "does not exist" in result.output


def test_unscannable_subdirectory_fails(target, deployer):
    (target / "2026").chmod(0o000)
    problems = check_target(target, deployer, WEB, 0o022)
    assert any("cannot scan" in p and str(target / "2026") in p for p in problems)


def test_cli_judges_the_effective_user(target, monkeypatch):
    # rsync writes with the effective UID, which a setuid or sudo wrapper may change
    monkeypatch.setattr(os, "geteuid", lambda: 0)
    result = CliRunner().invoke(cli, [str(target), "--web-user", "root"])
    assert result.exit_code == 1
    assert "running as root" in result.output
