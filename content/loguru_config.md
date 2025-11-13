---
title: "Modernizing loguru-config"
date: 2025-11-11
author: "C. Ross Jam"
status: published
---

Over the past year or two, I have acquired a taste for [loguru][1],
which has [excellent documentation][2], for logging in Python:

> Loguru is a library which aims to bring enjoyable logging in Python.

> Did you ever feel lazy about configuring a logger and used print()
> instead?… I did, yet logging is fundamental to every application and
> eases the process of debugging. Using Loguru you have no excuse not
> to use logging from the start, this is as simple as from loguru
> import logger. 

> Also, this library is intended to make Python logging less painful
> by adding a bunch of useful functionalities that solve caveats of
> the standard loggers. Using logs in your application should be an
> automatism, Loguru tries to make it both pleasant and powerful. 

One thing that the loguru package didn’t have out of the box is a way
to do configuration from a file. I went poking around on the ’Net and
found [a somewhat moribund loguru-config][3] package. Support for TOML
files was particularly attractive.

> Loguru-config is a simple configurator for the Loguru logging
> library. It extends the functionality of Loguru by allowing the user
> to configure the logger from a configuration file. This package
> provides a much-needed feature to Loguru, which is the ability to
> configure the logger from a configuration file (for example, using
> loguru alone, one can't automatically configure the logger to write
> to sys.stdout or sys.stderr from within a configuration file). 

> The configuration can have syntax similar to the one used by the
> native logging library in Python (i.e. support cfg://, ext://,
> etc.), but extends it to support even more features. It can also be
> easily extended to support even more features quite easily (see
> Extending the configurator for more details). 

> The configurator supports parsing of JSON, JSON5, YAML, and TOML
> files (out of the box) and can be extended to support other formats
> (again, see Extending the configurator below). 

No commits might have just indicated the work was finished. However,
when I tried to put it to work, it didn’t play nicely with modern
Python packaging (a. k. a. uv and friends). Also, the TOML package it
relied on seems to have not kept up with Python releases, so was
effectively end-of-life.

Thus for fun, and reps, I figured I’d try my hand using agentic coding
to [modernize the codebase][4] a bit. Unsurprisingly, the package name
remains the same. It’s just a fork under my GitHub account. Yeah open
source! 🎉🎉🎉

For this project, I targeted [Codex Cloud][5]. The experience was
pretty good even though I’ve been primed by Claude Code as a first
impression of agentic coding. Somewhat annoying is the fact that the
user can’t add commits to a branch shared with Codex. All of the code
has to be generated via prompting the agent. That said I was able to
significantly refine the package into a workable state with little
effort. And I even got it to generate a bunch of example configuration
documents for all of the supported formats!

I need to review the code a bit more, but I already have an existence
proof of plugging this config module into another personal
project. Of course I did it by simply pointing another coding agent at
the URL for my repo, but on first CLI blush, things seem to be
working.

If I have some spare cycles, maybe I’ll dig in to the Codex logs and
assess what worked, what didn’t, and whether it increased
productivity. To be honest though, even if I could have done it faster
by hand, I’m not sure it wouldn’t have come out worse, and frankly it
was just fun giving this new software development style a whirl.

[1]: https://github.com/Delgan/loguru
[2]: https://loguru.readthedocs.io/en/stable/
[3]: https://github.com/erezinman/loguru-config
[4]: https://github.com/crossjam/loguru-config
[5]: https://developers.openai.com/codex/cloud
