Vendored from https://github.com/crossjam/pyembed-markdown at commit
c8025b0f3707757f391e9aeb83bc30021cb206c6 (2026-11-10), which is what
`tool.uv.sources` previously pinned via a git dependency. The test suite
(`pyembed/markdown/test/`) is left out, as with the vendored pyembed.

That fork carries two changes on top of the last upstream release
(pyembed/pyembed-markdown, 1.1.0, unmaintained since 2015):

- Registers the extension the way current Python-Markdown expects, and
  renders a "link rot" notice with the plain link instead of failing the
  build when an OEmbed lookup errors
- Uses a raw string for the embed regex, fixing Python 3.13's invalid
  escape sequence warning

Keeping it here alongside pyembed puts both packages under the repo's
`poe bandit` scan, and lets fixes land in this repo directly.
