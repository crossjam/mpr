---
title: cyclopts
date: 2026-02-21 23:30
author: C. Ross Jam
---

Link parkin’: [cyclopts]

> Cyclopts is a modern, easy-to-use command-line interface (CLI)
> framework that aims to provide an intuitive & efficient developer
> experience. 
> 
> Why Cyclopts?
> 
> * **Intuitive API:** Quickly write CLI applications using a terse,
>   intuitive syntax. 
> * **Advanced Type Hinting:** Full support of all builtin types and
>   even user-specified (yes, including Pydantic, Dataclasses, and
>   Attrs). 
> * **Rich Help Generation:** Automatically generates beautiful help
>   pages from docstrings and other contextual data. 
> * **Extendable:** Easily customize converters, validators, token
>   parsing, and application launching. 

Being the CLI aficionado that I am, any newly discovered CLI toolkit
is of interest. That being said, it’s near impossible to pry [click]
from my hands. 

A click feature I appreciate is that it’s not trying to be magical
with functions or types. There can be a bit of magic in how it
implements processing declared by option and argument
decorators. However, it’s not trying to imply intent from the code or
make specifying the generated CLI as terse as possible. "Explicit is
better than implicit," is part of The Zen of Python and click is
closer to explicit than many of its successors.

Here’s the intro to a [comparison][typer-comparison] of cyclopts vs
[Typer]. 


> Much of Cyclopts was inspired by the excellent Typer
> library. Despite its popularity, Typer has some traits that I (and
> others) find less than ideal. Part of this stems from Typer's age,
> with its first release in late 2019, soon after Python 3.8's
> release. Because of this, most of its API was initially designed
> around assigning proxy default values to function parameters. This
> made the decorated command functions difficult to use outside of
> Typer. With the introduction of Annotated in python3.9, type-hints
> were able to be directly annotated, allowing for the removal of
> these proxy defaults.
>
> Additionally, Typer is built on top of Click. This makes it
> difficult for newcomers to figure out which elements are
> Typer-related and which elements are click-related. It's also hard
> to tell whether the following criticisms stem from Typer, or the
> underlying Click. For better-or-worse, Cyclopts uses its own
> internal parsing strategy, gaining complete control over the
> process. 
> 
> This section was originally written about Typer v0.9.0 (May
> 2023). Some criticisms have been addressed in later Typer versions;
> updates are noted in the respective sections below. 

I find Typer palatable, know of a few admirable libraries
that use it, and have put it in practice myself. Typically though,
I’ve never found click not up to anything I needed to get done,
including some pretty gnarly CLI argument hacking.

Likely won’t be putting cyclopts to the test, but it’s good to be as
informed as possible.

[cyclopts]: https://cyclopts.readthedocs.io/
[click]: https://click.palletsprojects.com/
[typer-comparison]: https://cyclopts.readthedocs.io/en/stable/vs_typer/README.html
[typer]: https://typer.tiangolo.com/
