---
title: "marimo and quarto"
date: 2025-10-08
author: "C. Ross Jam"
status: published
---

Link parkin’: [marimo + quarto][4]

> This repository provides a framework for integrating Quarto with
> marimo, enabling markdown documents to be executed in a marimo
> environment, and reactive in page. 

[Previously I’ve written][1] about how [marimo][3] is an interesting
project that’s advancing the state of the art in the Python
computational notebook space. One of [quarto’s][2] claims to fame is
straightforward incorporation of Jupyter notebooks in scientific
publishing. As I’m getting up to speed with quarto, I ventured out to
see how well marimo was integrated.

After giving it a quick test drive, the linked extension looks
promising, but is a tad glitchy. Apparently a JavaScript support
library for marimo that’s a few point releases behind main is
necessary to get embedded interactivity working. Not that I
desperately need that feature, but it’s mildly annoying.

If the extension sees continued support and improvement, I’ll be
putting it to good use.

[1]: {filename}/the_marimo_moment.md
[2]: https://quarto.org/
[3]: https://marimo.io/
[4]: https://github.com/marimo-team/quarto-marimo
