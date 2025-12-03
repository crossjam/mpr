---
title: "TIL: podcast-archiver"
date: 2025-12-02
author: "C. Ross Jam"
status: published
---

TIL: [podcast-archiver][1]

> A fast and simple command line client to archive all episodes from
> your favorite podcasts. 
> 
> Podcast Archiver takes the feed URLs of your favorite podcasts and
> downloads all available episodes for you—even those "hidden" in
> paged feeds. You'll end up with a complete archive of your
> shows. The archiver also supports updating an existing archive, so
> that it lends itself to be set up as a cronjob. 

For my [retrocast][2] project, I’ve been casting about for a solution
to reliably download all the episodes from an RSS feed. [aria2][4] is
the current path being pursued. The approach has been to fork aria2 as
a subprocess and then feed it episode URLs over one of aria2’s
RPC-over-HTTP interfaces. Not as elegant as I’d like. 

A trick I’ve picked up is hijacking [click][5]‑based CLI projects and
blending them into my own CLI projects. Either via eyeball inspection
or metaprogramming, it’s easy to grab commands and wire them into my
own app. This technique needs some refinement to deal with potential
configuration impedance mismatches between CLI toolkits. I’ll go into
detail in another post, but I put it to good effect by integrating
Simon Willison’s [llm](https://llm.datasette.io) package into another
personal project. I got the 90% of llm that seamlessly manages models,
plugins, prompts, and AI vendor APIs. My extra bits of functionality
and porcelain benefit from it.

So next up, let’s apply this to retrocast and podcast-archiver.

Bonus TIL: [rich-click][3]

> rich-click is a wrapper around Click that renders help output nicely using Rich.
>
> - Click is a "Python package for creating beautiful command line interfaces".
> - Rich is a "Python library for rich text and beautiful formatting
>   in the terminal".
>
> The intention of rich-click is to provide attractive help output
> from Click, formatted with Rich, with minimal customization
> required. 

Discovered this because podcast-archiver uses rich-click to implement
a pretty text interface. I’m a heavy user of both packages, so this is
definitely one to take a look at.

[1]: https://codeberg.org/janw/podcast-archiver
[2]: https://github.com/crossjam/retrocast
[3]: https://ewels.github.io/rich-click/latest/
[4]: https://aria2.github.io/
[5]: https://click.palletsprojects.com/ 

