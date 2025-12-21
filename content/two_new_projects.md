---
title: "Two New Side Projects"
date: 2025-12-20 20:00
author: "C. Ross Jam"
status: published
---

I’ve been putting in the reps with agentic coding, gaining patterns
and confidence. So much so that I’m committing to launching two
projects here at the end of the year.

### Humble Librarian

Let’s start with Humble Librarian. I’m a bit of a [Humble Book Bundle][1]
addict.

> BOOKS BUNDLES
>
> Looking for your next great read? Immerse yourself in adventurous
> comics, discover spectacular fantasy worlds, whip up your soon-to-be
> favorite recipe, run a new tabletop RPG system, and more with our
> curated book bundles. Whether you're a voracious reader or want to
> explore new genres, our exclusive bundles can help you find your
> next literary love. Plus, a portion of the bundle proceeds go to
> charity! 

Over the last few years I’ve plunked down for 80+ book bundles. I tend
towards tech book and comics bundles, with dashes of science fiction
and self-help. I’ve also independently bought a number of ebooks
directly from [Manning][2], [Pragmatic Programmers][3], [No
Starch][4], [eBooks.com][5], and self-publishers. Each bundle will
typically have 10 or more books included.

Bottom line, I have a metric crap-ton of EPubs, PDFs, CBZs, and mobis
to deal with. Half the time when I’m looking at a new Humble Book
Bundle, I’m not sure if I already have the books on offer. 

Let’s see how far we can get using agentic coding to build file system
crawler, indexer, and chat UX for dealing with my personal library.


### Peyote

Over fifteen years ago I made [some headway][7] on [a project named
peyote][6]. The idea was to use Python, PyGame, and OpenGL to create
generative art on the order of processing. I managed to get one piece
completed and then ran out of steam.

Below is a portion of a plan that I asked Claude Code to create for a
screensaver, `hextrail` that recently caught my eye.

> ## HexTrail Screensaver - Code Summary and Python Port Plan
> 
> ## Original Code Summary
> 
> **HexTrail** is an XScreenSaver module written in C with OpenGL that
> creates a mesmerizing animated pattern of colored lines growing
> across a hexagonal grid. 
> 
> ### Core Concept
> 
> The screensaver creates a honeycomb grid of hexagonal
> cells. Animated "arms" (lines) grow from the centers of hexagons
> toward their edges, then continue into neighboring hexagons,
> creating a branching network of colorful trails across the hexagonal
> substrate. 
> 
> ### Key Data Structures
> 
> 1. **arm** (hextrail.c:39-43)
>     - State: EMPTY, IN, WAIT, OUT, or DONE
>     - `ratio`: Growth progress (0.0 to 1.0)
>     - `speed`: Animation speed
> 
>  2. **hexagon** (hextrail.c:45-53)
>     - Position (XYZ coordinates)
>     - 6 neighbors (pointers to adjacent hexagons)
>     - 6 arms (one for each edge)
>     - Color index
>     - Border state and animation ratio
> 
>  3. **hextrail_configuration** (hextrail.c:55-70)
>     - Grid dimensions and hexagon array
>     - Color palette (8 colors)
>     - OpenGL context and rotation state
>     - Animation state (FIRST, DRAW, FADE)
> 
> 

That’s just an initial assessment from the [XScreensaver][9] C source
code for `hextrail`. I’m feeling confident I can work with Claude and
Codex to make a passable start on a featureful, modernized peyote app
with `hextrail` and my old sketch `substrate` as starters.

### Bottom Line

As many others diving into agentic coding point out, the process might
not necessarily be more productive for straight code creation. But
these tools lower the barrier for kicking off new projects and getting
them above threshold. 

Forza!

[1]: https://www.humblebundle.com/books
[2]: https://www.manning.com/
[3]: https://pragprog.com/
[4]: https://nostarch.com/
[5]: https://www.ebooks.com/
[6]: https://github.com/crossjam/peyote
[7]: {content}/mission_accomplished.md
[8]: https://processing.org/
[9]: https://www.jwz.org/xscreensaver/
