---
title: "Moderninzing Python Generative Art"
date: 2025-10-15
author: "C. Ross Jam"
status: published
---

Over 15 years ago, I completed [a generative art hack in
Python][1]. Effectively I transliterated a work from [Processing][2]
into a combination of [pygame][3] and some lower level bit
manipulation libraries. Further work never got all that far into
making a robust framework or re-implementing other works.

Fast forward to the current era and maybe it’s time for a
revisit. Especially as I’m looking for some new themes for this
blog. First off, there’s likely a free order of magnitude or two
speedup that’s been gained just through processor and GPU
improvements. Second, thanks to the AI bubble, the software layers for
programming with accelerators in Python has vastly improved. Third, it
looks like OpenGL isn’t the only way to do fast bit level graphics
anymore.

Just for grins, I’ve been tasking [Gemini Deep Research][4] to create  reports on
how this could be done. Here’s a sample:

> I. Executive Synthesis: Framework Recommendations and Performance Benchmarks

> A. The Architecture of Choice: Optimal Stack for Real-Time
> 
> Generative Art The investigation into Python frameworks suitable for real-time
> generative art, specifically those handling large bitmap images
> represented by NumPy arrays, identifies an optimal stack that
> minimizes CPU overhead and leverages modern hardware capabilities. The
> most architecturally sound and performance-oriented solution centers
> on the use of pygfx and fastplotlib, relying on the WGPU graphics
> backend.

> This combination is strategically superior because it addresses the
> constraints inherent in legacy visualization tools. Frameworks such as
> VisPy and Pyglet, while mature, are typically built upon OpenGL. In
> contrast, WGPU represents a crucial evolutionary step in graphics
> APIs, serving as a high-level abstraction layer that translates
> uniformly across modern, low-level APIs, including Vulkan, Metal, and
> Direct3D. Since WGPU itself is a Rust implementation with C
> bindings , adopting a WGPU-based library inherently satisfies the
> requirement for low-level language bindings while maintaining a
> high-level Python application interface. This architectural choice is
> not merely an incremental performance improvement but a foundational
> necessity to fully exploit the parallel processing power of modern
> GPUs, ensuring greater long-term stability and maximizing performance
> gains compared to frameworks constrained by the legacy overhead of
> OpenGL.

This could also be an interesting exploratory application of agentic
coding. I know a bit about graphics and generative art, but I’m not an
expert. Maybe I could coding-centaur my way into a useful framework in a
reasonable amount of time.


[1]: {filename}mission_accomplished.md
[2]: https://processing.org/
[3]: https://pygame.org/
[4]: https://gemini.google/overview/deep-research/
