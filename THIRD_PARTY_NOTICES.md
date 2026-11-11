# Third-party notices

This repository contains copies of the third-party code below. Each
keeps its original license, which is in the directory alongside it.
The rest of the repository is licensed as described in `LICENSE.md`.

| Path | Upstream | License | Copyright |
| --- | --- | --- | --- |
| `vendor/pyembed` | [jaywink/pyembed](https://github.com/jaywink/pyembed) | MIT (`LICENSE.txt`) | 2013 Matt Thomson; 2026 Brian M. Dennis |
| `vendor/pyembed-markdown` | [crossjam/pyembed-markdown](https://github.com/crossjam/pyembed-markdown), a fork of [pyembed/pyembed-markdown](https://github.com/pyembed/pyembed-markdown) | MIT (`LICENSE.txt`) | 2013 Matt Thomson; 2026 Brian M. Dennis |
| `plugins/pelican_json_feed` | [crossjam/pelican_json_feed](https://github.com/crossjam/pelican_json_feed), a fork of [andrewheiss/pelican_json_feed](https://github.com/andrewheiss/pelican_json_feed) | MIT (`LICENSE`) | 2017 Andrew Heiss; 2026 Brian M. Dennis |
| `plugins/summary` | [getpelican/pelican-plugins](https://github.com/getpelican/pelican-plugins) (via the crossjam fork) | AGPL-3.0 (`LICENSE`) | Pelican plugin contributors |
| `themes/crossjam-svbhack` | [crossjam/pelican-svbhack](https://github.com/crossjam/pelican-svbhack/tree/crossjam/mpr), a fork of [gfidente/pelican-svbhack](https://github.com/gfidente/pelican-svbhack) | MIT (`LICENSE`) | 2012 William Ting, 2013 Giulio Fidente; 2026 Brian M. Dennis |

The MIT licenses require that their copyright and permission notices
stay with copies of the code, which the license files in each
directory do. Every MIT component here has been modified for this
repository, so each license file also carries a copyright line for
Brian M. Dennis. Local changes to the vendored pyembed packages are
described in their `VENDORED.md` files.

## plugins/summary and the AGPL

`plugins/summary` is the only copyleft code here. It is unmodified from
the copy in pelican-plugins and stays under AGPL-3.0, with its license
in `plugins/summary/LICENSE`. Pelican loads it as a plugin alongside
this repository's Apache 2.0 code; Apache 2.0 code may be combined with
AGPL-3.0 code, so the combination at build time is permitted. The
AGPL's network-use clause applies to users interacting with the program
itself over a network. The plugin runs only when the site is built,
and the published site is static output, not the program.

If `plugins/summary` is ever modified, the changed files need a notice
saying so and when, as AGPL-3.0 section 5 requires, and the modified
plugin stays under AGPL-3.0.

Pelican itself is also AGPL-3.0, but it is installed as a dependency
rather than copied in.
