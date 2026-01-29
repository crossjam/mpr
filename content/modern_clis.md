---
title: Modern CLIs
date: 2026-01-29 17:00
author: C. Ross Jam
---

Just discovered Derick Schaefer’s book [_CLI: A Practical Guide to
Creating Modern Command-Line Interfaces_][modern-clis]

> Once the backbone of early computing, the command-line interface
> (CLI) nearly disappeared in the shadow of graphical user
> interfaces. But today, it’s experiencing a powerful
> resurgence—driven by DevOps, automation, cloud-native
> infrastructure, and the rise of generative AI. While its roots trace
> back to the 1960s, the CLI has evolved into a modern development
> essential: fast, scriptable, cross-platform, and precise. 
> 
> ...
> 
> This book is a modern guide to command-line development, written for
> engineers, architects, and toolmakers building the next generation
> of CLI applications. It offers clear explanations, battle-tested
> patterns, and real-world examples written in Go—an ideal language
> for high-performance, cross-platform development. Readers will also
> find Spotlights on widely adopted tools like Git, WP-CLI, and Warp
> Terminal, revealing the design thinking behind some of today’s most
> influential CLIs. 

The book is interesting to me on multiple fronts. I’d like to think
I’m a command line interface (CLI) tool connoisseur just because of my
long time UNIX usage. The history angle of the book is a quick
hook. 

When starting a new development project, I usually default to building
a CLI. I’ve had it in the back of my head to do some research on best
practices. Discovering _CLI ..._ is really timely since it seems to
have pragmatic design advice for CLI tools.

Also, Schaefer only publishes physical versions of the books.

I was alerted to the book via an excellent [Software Engineering Radio
podcast episode interview with Schaefer][podcast-episode].

> In this episode, Derick Schaefer, author of CLI: A Practical Guide to
> Creating Modern Command-Line Interfaces, talks with host Robert
> Blumen about command-line interfaces old and new. Starting with a
> short review of the origin of commands in the early unix systems,
> they trace the evolution of commands into modern CLIs. Following the
> historic rise, fall, and re-emergence of CLIs, they consider
> innovative examples such as git, github, WordPress, and
> warp. Schaefer clarifies whether commands are the same as CLIs and
> then discusses a range of topics, including implementation
> languages, packages in the golang ecosystem for CLI development,
> CLIs and APIs, CLIs and AIs, AI tooling versus MCP, the
> object-command pattern, command flags, API authentication, whether
> CLIs should be stateless, and output formats – json, rich text. 


The interview was a rich conversation with real technical depth. No
fluff. I probably don’t listen to SE-Radio episodes often enough, but
this one was a sterling example of the podcast quality. Also, the
content has a Creative Commons license attached making it handy for
testing and demos.

[modern-clis]: https://moderncli.dev
[modern-clis-toc]: https://moderncli.dev/overview/
[podcast-episode]: https://se-radio.net/2026/01/se-radio-702-derick-schaefer-on-modern-clis/
