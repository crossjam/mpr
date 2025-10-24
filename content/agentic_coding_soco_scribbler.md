---
title: "soco-scribbler: Agentic Development"
date: 2025-10-24
author: "C. Ross Jam"
status: published
---

I made some recent forward progress on my side quest project
[soco-scribbler][1]. This is an effort to revise the [sonos-lastfm][2]
project, which uses [SoCo][3] under the covers, to log track info from
Sonos speakers.

The screen capture below illustrates monitoring of three speakers and
track logging from one that’s actively playing. The ultimate goal is
to emit the track info to other systems such as an sqlite database or
a message streaming platform like [nats](https://nats.io). But just
handing off to Python logging is a good start.

![Screen capture of soco-scribbler running in a terminal
console]({static}/images/soco-scribbler screenshot.png)

The interesting bit is that I used OpenAI’s [Codex CLI][4] to flesh
out and revise my broken handwritten first cut. Here’s the task list
that I prompted Codex to create.

- [x] Rework the `scribble` CLI options in `src/soco_scribbler/soco_scribbler.py:18` to remove Last.fm credential flow, keep interval settings, and add logging parameters.
- [x] Convert `SocoScribbler` into a subclass of `SonosScrobbler` that sets placeholder Last.fm env vars, disables the Last.fm network, and accepts logging configuration.
- [x] Implement helpers to ensure log storage, format timestamped entries, append to file/console, and override `scrobble_track` to log locally while updating history.
- [x] Update the command body to use the new options, set interval env vars, drop credential/setup handling, and keep the monitoring loop via `run()`.
- [x] Validate the new CLI surface with `uv run python -m soco_scribbler.soco_scribbler --help` and manually confirm logging output without Last.fm submission.
- [x] Introduce `platformdirs` to resolve per-user config/data directories in an OS-aware way and refactor existing hardcoded paths.
- [x] Update documentation/help text to describe the new config directory behavior powered by `platformdirs`.

Not only did I subclass the `SonosScrobbler` class to hijack track
scrobbling but I specced out a bunch of other necessary but rote
tasks. After approving the plan, I just told Codex to "make it
so". Thus the xs checking off task completion. The result worked right
out of the gate. There’s some subsequent human written adjustments to
handle a bit of an edge case, but I think I could have just thrown the
error message at Codex and it would have been fine fixing it.

Once I got up and rolling this was a quite pleasant experience. One
that I might not have even given a go if not for agentic coding. As
I’ve said in other venues, I’m skeptically optimistic but this
decreases the level of skepticism a bit.

[1]: https://mpr.crossjam.net/wp/mpr/2025/06/soco-scribbler/
[2]: https://github.com/denya/sonos-lastfm
[3]: http://python-soco.com
[4]: https://developers.openai.com/codex/cli/
