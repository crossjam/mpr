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

The discovery requests in `pyembed/core/discovery.py` also had no timeout,
so one unresponsive host could hang a site build indefinitely. They now use
the same 10 second timeout as the consumer requests.

## License

MIT, copyright 2013 Matt Thomson and 2026 Brian M. Dennis, per `LICENSE.txt` (also declared in
`setup.py`). The original copyright and permission notice stay in place, as the
MIT license requires, with a line added for Brian M. Dennis's changes. The local patches above are under the same license.
