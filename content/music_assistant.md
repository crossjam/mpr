---
title: apple-music-python, MusicKit Authentication, and Music Assistant
date: 2026-01-17 16:20
author: C. Ross Jam
status: published
---

It was a bit of a circuitous route, but I seem to have discovered a means to
inspect a user’s Apple Music Library with Python.

Previously, when I was [exploring Apple Music APIs][apple-music-apis-post], I
landed on the [apple-music-python] package and its
[repository][apple-music-python-repo]. Recently, I did the legwork to reactivate
an old Apple Developer account and get the credentials for searching with the
package.

Reading one of the [repo's issues][repo-issue] surfaced Apple’s [_User
Authentication for MusicKit_][music-kit-auth] documentation and [Web
flow][music-kit-web]. I started pondering if an agentic coder could do the
heavy lifting involved in porting this to Python. But more research was in
order. Surely there must be another Python package that dealt with this?

Then I learned about [Music Assistant][music-assistant].

> Music Assistant is a music library manager for your offline and online music
> sources which can easily stream your favourite music to a wide range of
> supported players and be combined with the power of Home Assistant!
>
> ...
>
> ### Music Assistant Server
>
> The Music Assistant server is a free, opensource Media library manager that
> connects to your streaming services and a wide range of connected speakers.
> The server is the beating heart, the core of Music Assistant and it keeps
> track of your music sources. It must run on an always-on device like a
> Raspberry Pi, a NAS or an Intel NUC or alike. The server can access multiple
> music providers and stream to multiple player types.

One of the output providers is Sonos 😲 💥 🎉! My fave!! And a supported streaming
service is, guess what, Apple Music, including a nice auth flow according to
this [pull request][music-assistant-pr].

So yes indeed, someone else had dealt with this issue. The solution looked a bit
hairy though, so I decided to revisit apple-music-python one last time. Jonathan
Jacobson had submitted [a yet to be accepted PR][jacobson-pr] that extended
apple-music-python under the assumption that the Music User Token was already
available, something that can be handled via Music Assistant.

Bringing it all together, in the short term, I’m just going to install Music
Assistant and experiment with Apple Music support. Can’t imagine it’ll be too
hard to pry out a Music User Token, assuming I can actually authenticate. Then
I’ll just experiment with [Jacobson’s package repo][jacobson-repo] that upgrades
apple-music-python.

The ultimate goal is to augment [scrobbledb] with the ability to enrich the data
with information from [my favorite DJ mix platform][dj-mix-platform-post].

[apple-music-apis-post]: {filename}/apple_music_apis.md
[apple-music-python]: https://apple-music-python.readthedocs.io/en/latest/
[apple-music-python-repo]: https://github.com/mpalazzolo/apple-music-python
[repo-issue]: https://github.com/mpalazzolo/apple-music-python/issues/8
[music-kit-auth]: https://developer.apple.com/documentation/applemusicapi/user-authentication-for-musickit
[music-kit-web]: https://js-cdn.music.apple.com/musickit/v3/docs/index.html?path=/story/user-authorization--page
[music-assistant]: https://www.music-assistant.io
[music-assistant-pr]: https://github.com/music-assistant/server/pull/2230
[jacobson-pr]: https://github.com/mpalazzolo/apple-music-python/pull/24
[jacobson-repo]: https://github.com/j-jacobson/apple-music-python
[scrobbledb]: https://github.com/crossjam/scrobbledb
[dj-mix-platform-post]: {filename}/best_dj_mix_platform.md
