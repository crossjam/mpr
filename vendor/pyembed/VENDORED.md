Vendored from https://github.com/jaywink/pyembed at commit
f79ce0b8acd6d0dbe93809ed4c92c764792d5627 (2021-08-06), which is the last
commit on the upstream repo and matches what `tool.uv.sources` previously
pinned via a git dependency.

Upstream is unmaintained (no commits since 2021, no PyPI release newer than
1.3.3, same vintage code). setuptools >=82 removed the `pkg_resources`
module, which `pyembed/core/discovery.py` imported to locate its bundled
`config/providers.json`. Patched that one call to use `os.path.dirname(__file__)`
instead, so this package no longer depends on `pkg_resources` at all and we
can keep setuptools current.
