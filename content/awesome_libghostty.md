---
title: Awesome libghostty
date: 2026-03-01 20:30
author: C. Ross Jam
---

For some reason the [Ghostty] terminal emulator popped to
[the top of Hacker News][hn-ghostty] again. Mitchell Hashimoto jumped in to
comment:

> I'm the original creator of Ghostty. It's been a few years now! I don't know
> why this is on the front page of HN again but let me give some meaningful
> updates across the board.
>
> First, libghostty is _way more exciting_ nowadays. It is already backing more
> than a dozen terminal projects that are free and commercial:
> https://github.com/Uzaaft/awesome-libghostty I think this is the real future
> of Ghostty and I've said this since my first public talk on Ghostty in 2023:
> the real goal is a diverse ecosystem of terminal emulators that aim to solve
> specific terminal usage but all based on a shared, stable, feature-rich, high
> performant core. It's happening! More details what libghostty is here:
> https://mitchellh.com/writing/libghostty-is-coming
>
> I suspect by the middle of 2027, the number of people using Ghostty via
> libghostty will dwarf the number of users that actually use the Ghostty GUI.
> This is a win on all sides, because more libghostty usage leads to more stable
> Ghostty GUI too (since Ghostty itself is... of course... a libghostty
> consumer). We've already had many bugs fixed sourced by libghostty embedders.

And here’s what he said about libghostty back in 2025.

> Libghostty Is Coming
>
> Over two years ago, in one of my first public talks about Ghostty, I shared my
> vision for libghostty: an embeddable library for any application to embed
> their own fully functional, modern, and fast terminal emulator. Libghostty is
> finally starting to take shape, and I'm excited to share more details about my
> plans for it.
>
> The first libghostty library will be libghostty-vt: a zero-dependency library
> that provides an API for parsing terminal sequences and maintaining terminal
> state, extracted directly from Ghostty's real-world proven core. It doesn't
> even require libc!

The current wave of AI coding agent enthusiasm is forging a renaissance in text
user interfaces. As Hashimoto hoped, libghostty seems to be right in the mix, as
exhibited by the [Awesome libghostty][awesome-libghostty] repository: "A curated
list of awesome projects, tools, and resources built with or for libghostty."

There are some interesting projects in there. Ghostty hasn’t quite stuck with
me, and the HN thread has a few gripes pointing to issues that could be
problematic. I’m on the lookout for a robust agent orchestration front end to
manage multiple asynchronous coders. It’s good to know the core of Ghostty is
helping a thousand flowers bloom.

[awesome-libghostty]: https://github.com/Uzaaft/awesome-libghostty
[ghostty]: https://ghostty.org/
[hn-ghostty]: https://news.ycombinator.com/item?id=47206009
