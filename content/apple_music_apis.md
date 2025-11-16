---
title: "Apple Music APIs"
date: 2025-11-16
author: "C. Ross Jam"
status: published
---

Work on my [scrobbledb][1] project has been moving along. As scrobble
and track metadata archiving solidifies, the eye turns to how to
exploit that data. Given my predilection to [DJ mixes on Apple
Music][2], I became curious on what was available to leverage Apple’s
music streaming service. Turns out quite a bit.

First off, [the Apple Music API][3]

> Use Apple Music API to access information about media in the Apple
> Music Catalog and a user’s personal iCloud Music Library.
>
>   - Apple Music Catalog includes all resources available in Apple
>     Music.
>
>   - iCloud Music Library contains only those resources the user adds to
>     their personal library. For example, it contains items from Apple
>     Music, songs purchased from iTunes Store, and imports from discs
>     and other apps. This library can include content that’s not in the
>     Apple Music Catalog. 
>
> Use this API to retrieve information about albums, songs, artists,
> playlists, music videos, Apple Music stations, ratings, charts,
> recommendations, and the user’s most-recently played content. With
> proper authorization from the user, you can also create or modify
> playlists and apply ratings to the user’s content. 

Matt Palazzolo put together [a Python module for the Apple Music
API][5], [docs][6], focused strictly on the catalog. Apparently
accessing a user’s iTunes library is a hairier prospect.

Interestingly, the Apple Music API docs point to a bulk metadata
download service [the Apple Music Feed][4].

> Apple Music Feed contains the catalog content of Apple Music
> products in bulk for consumption as feed exports. These bulk exports
> are appropriate for offline use cases, complementing Apple Music
> API, which is best for online use. Apple Music Feed includes content
> metadata for albums, songs, artists, and popularity charts, and
> fully refreshes every 24 hours. You access the Apple Music Feed
> using Apple Media Feed API to request an export of a data set.
>
> With access to the raw data and the information in this
> documentation, you can use Apple Music Feed in many ways. For
> example, if you want to build a discovery engine for Apple Music,
> your team can examine the data and determine endpoint requests to
> serve such an engine. 

Apple itself provides [code examples][7] for the Music Feed.

Clearly this will be relevant to building on top of scrobbledb. Also,
seems like a possibility for an [MCP server][8]

[1]: https://github.com/crossjam/scrobbledb
[2]: {filename}/best_dj_mix_platform.md
[3]: https://developer.apple.com/documentation/applemusicapi
[4]: https://developer.apple.com/documentation/applemusicfeed/
[5]: https://github.com/mpalazzolo/apple-music-python
[6]: https://apple-music-python.readthedocs.io/en/latest/
[7]: https://github.com/apple/music-feed-examples
[8]: https://modelcontextprotocol.io/docs/learn/server-concepts
