---
title: Command Book
date: 2026-02-07 18:30
author: C. Ross Jam
status: published
---

[Michael Kennedy][michael-kennedy] has released a new app called
[Command Book][command-book]. Here’s the tagline:

> Save your commands. Run them reliably. Monitor their output. Never rebuild
> your terminal setup again.

In
[_"Your Terminal Tabs Are Fragile. I Built Something Better."_][kennedy-terminal-tabs],
Kennedy gets into the pain points that drove the development of Command Book:

> Each of these commands requires that I remember which working directory to
> start in (the daemon runs somewhere else than the flask app for example).
> Getting them up and running is a bit tedious. Certainly doable, but tedious.
>
> You’re working through the day, and you realize some part of your app isn’t
> working. It crashed. Why? You had --reload set and it dutifully reloaded on
> file changes. But the code was half-ready. You or Claude wrote the import
> statement, import new_feature, but you haven’t yet created that module. Or
> maybe it reloaded while you were mid-function having written def scan_files(
> and you get an unmatched brace. Reload fails and you’re hunting through
> terminal tabs for which part stopped working and needs to be restarted.
>
> ## What I actually needed
>
> Terminals are great for interactive work, exploration, quick commands. But
> they are terrible as a process manager. What I wanted was a command/process
> manager for long running commands currently living in my terminal.
>
> I wanted them to be reproducible, instant, reliable and auto restarting if
> code changes, not just reloading unless the code gets out of sync.
>
> **I wanted a terminal companion.**

My mental model is [Docker Compose][docker-compose] without the containers or
the YAML specification. Command output capture and process restart are two
Compose features that are handy if you’re managing a bunch of long-running
processes in development or need to track AI agent sessions launched from a CLI.

As Brent Simmons and John Gruber would say, Command Book is a
[Mac-Assed Mac app][mac-assed-app], but it does have a CLI. There’s a free,
limited version (5 saved commands, limited log capture). $14.99 gets you
unlimited commands and 40× more log capture.

[command-book]: https://commandbookapp.com
[docker-compose]: https://docs.docker.com/compose/
[kennedy-terminal-tabs]: https://mkennedy.codes/posts/your-terminal-tabs-are-fragile-i-built-something-better/
[mac-assed-app]: https://daringfireball.net/linked/2020/03/20/mac-assed-mac-apps
[michael-kennedy]: https://mkennedy.codes/
