---
title: uv and .env
date: 2025-10-05
author: C. Ross Jam
status: published
...

From Daniel Roy Greenfeld, ["TIL: Loading .env files with uv run"][1]

> We don't need python-dotenv, use uv run with --env-file, and your
> env vars from .env get loaded.

Good to know, even though I’m all in on [direnv][2] to auto load .env
files. Also, handy to make [Poe the Poet][3] tasks that invoke `uv`
underneath the covers really explicit.


[1]: https://daniel.feldroy.com/posts/til-2025-09-env-files-with-uv-run
[2]: https://direnv.net
[3]: https://poethepoet.natn.io/index.html

