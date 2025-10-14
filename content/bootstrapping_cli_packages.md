---
title: "Bootstrapping Python CLI Packages"
date: 2025-10-10
author: "C. Ross Jam"
status: published
---

As an avowed command line interface (CLI) guy my default approach to
building new Python functionality is to write a packages that’s
embedded within a CLI right from the getgo. Fortunately, Python is
blessed with many packages to support this. [click][1] and [typer][2]
are my gotos. I so admire click that I believe the package should be a
part of the Python standard library.

I also have a few opinions regarding packaging ([uv][6] please), logging
(use [loguru][7]), and configuration ([platform user directories][8] + [TOML
files][9]). If you do enough of these CLIs within a certain period of
time, you start to yearn for some bootstrapping automation. Recently I
landed on a couple of packages that align with my preferences and
could really help here.

First off is [a batteries included cookiecutter][3] for new Python
packages.

> There are many cookiecutter templates, but this one is mine and I'm
> sharing it with you. Create complete Python packages with zero
> configuration - including CLI, testing, documentation, and automated
> PyPI publishing via GitHub Actions. 

Second is the [typerdrive][10] [package][4] ([background from Tucker Beck][5])

>During my time as an engineer working primarily with Python, I've
> written a a fair number of CLIs powered by Typer. One type of
> project that has been popping up for me a lot lately involves
> writing CLI programs that interface with RESTful APIs. These are
> pretty common these days with so many service companies offering
> fully operational battlestations...I mean, platforms that can be
> accessed via API. 
> 
> I've established some pretty useful and re-usable patterns in
> building these kinds of apps, and I keep finding new ways to improve
> both the developer experience and the user experience. Every time I
> go about porting some feature across to a new or old CLI, I wish
> there was a library that wrapped them all up in a nice package. Now,
> there is _typerdrive_:
>
> ...
>
> These are the challenges I found myself facing repeatedly when
> building CLIs that talk to APIs:
>
> - Settings management: so you're not providing the same values as
>   arguments over and over 
> - Cache management: to store auth tokens you use to access a secure
>   API 
> - Handling errors: repackaging ugly errors and stack traces into
>   nice user output 
> - Client management: serializing data into and out of your requests
> - Logging management: storing and reviewing logs to diagnose errors
> 
> typerdrive wraps all this up into an interface that's easy for users
> and developers as well. 

I could see myself creating a combination of these two into a new
cookiecutter with a few tweaks of my own for AI engineered CLIs and
REPLs. My thanks to the fine gentlemen who authored these packages and
made them publicly available.

[1]: https://click.palletsprojects.com/en/stable/
[2]: https://typer.tiangolo.com
[3]: https://jnyjny.github.io/python-package-cookiecutter/
[4]: https://github.com/dusktreader/typerdrive
[5]: https://blog.dusktreader.dev/2025/05/13/introducing-typerdrive-develop-api-connected-typer-apps-at-lightspeed/
[6]: https://docs.astral.sh/uv
[7]: https://loguru.readthedocs.io/en/stable/
[8]: https://platformdirs.readthedocs.io/en/latest/#
[9]: https://tomlkit.readthedocs.io/en/latest/
[10]: https://dusktreader.github.io/typerdrive/
