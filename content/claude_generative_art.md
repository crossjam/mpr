---
title: "Generative Art in Claude"
date: 2025-11-08
author: "C. Ross Jam"
status: published
---

[Previously][2] I noticed that Claude had a skill for generative
art. Since I’d like to build my own, non-browser, generative art
platform I haven’t put it to the test. But it does provide an avenue
for experimentation.

[Les Orchard](https://lmorchard.com/) also discovered the Claude
skill. And he actually [used the skill to create some generative
art][1]:

> Anthropic recently introduced the notion of Agent Skills for Claude,
> which Simon Willison wrote may be "a bigger deal than MCP". Figured
> I should check things out and noticed one of the example skills was
> for producing algorithmic art. That dovetails nicely with my own
> noodlings in web-based art sketches. So, I gave it a shot. 
>
> Long story short, here's a sketch I made with Claude's help, wrapped
> up as a web component that hopefully works in your browser: 

Go visit the post to see the result. I actually find it quite
compelling.

He documents his process along the way, which serves as a case study
of using agentic coding for generative art. One thing that caught my
eye was the desire to capture intermediate results. I’m not sure if
there’s a good model between continuous, implicit version capture
(expensive, granularity?) and explicit user version commits (human
toil). Wonder if an over the shoulder agent could monitor the state of
the work and intelligently prompt the user at various points for
explicit confirmation?


A final thought from Orchard:

> If you'd like the source, I've got it up on GitHub. It's messy and
> it's not groundbreaking art, but the process was gratifying. While
> Claude generated the bulk of the code, I didn't just sit back: I
> gave it ideas, did some debugging and coding, and steered things to
> make it my own. 


[1]: https://blog.lmorchard.com/2025/11/05/hunting-horizon/
[2]: {filename}/generative_art_good_company.md
