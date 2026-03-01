---
title: Building Agentic Kernels
date: 2026-02-28 21:30
author: C. Ross Jam
status: published
---

After having [digested][pi-coding-post] Mario Zechner’s
[lessons][zechner-lessons] regarding the pi coding agent, along with
[pondering][ronacher-on-pi] Armin Ronacher’s
[dissection of OpenClaw and pi][pi-in-openclaw], I find the core ideas of agentic
coding harnesses intriguing. They appeared together on a Syntax
[podcast episode][syntax-episode] and were quite the hoot! The gist of the
discussion was that pi is really simple, ridiculously effective, and highly
dangerous! The danger comes from letting an agent (LLM+tools+loop) have full
access to your file system with your permissions. The effectiveness emerges
because pi starts with limited functionality but can easily modify itself while
continuing to run.

Multiple recent webinars I’ve attended have similarly proclaimed: "You can build
one of these harnesses in (much) less than 1,000 lines of code," with 1,000 being
generous. The prolific [Hugo Bowne-Anderson][hugo-bowne-anderson] recently held
[a workshop / live-coding session][ivan-leo-livecoding] that did exactly this.

> Yesterday, I ran a workshop with Ivan Leo (ex-Manus) called “Building Your Own
> OpenClaw from Scratch” to show you how to build your own AI assistant from
> first principles. We covered:
>
> - How coding agents are really general-purpose computer use agents that happen
>   to be great at writing code
> - Building the core agent loop with an LLM and tool calls
> - Context management, memory compaction, and progressive disclosure
> - How agents can write their own tools and hot-reload them on the fly (via a
>   factory pattern)
> - Making the agent trigger actions automatically (send a Telegram message, log
>   to a database, fire off an email) using hooks
> - Connecting the agent to Telegram via FastAPI
> - Sandboxing and production deployment with Modal
>
> We wrote this blog post for those who don’t have 100 minutes to watch the
> entire workshop right now.

I’m one of those folks who didn’t have 100 minutes this past Friday to watch,
but I definitely want to go back and review the recording. The
[blog post][ivan-leo-transcript-post] is pretty hefty, building up a conceptual
design and framework, then providing the gory details of the actual
implementation in Python. Thanks so much to Ivan and Hugo for this great gift.

Having read the article end-to-end, I see a clear path for a developer to fit
the entirety of the harness into their brain, use it as a pedagogical starting
point, and then build further. This could mean starting with Leo’s code and
extending it with new concepts, or porting it to another language or system. The
code from this session is small enough that it can be an operational
[kernel][kernel-definition] for building more complex things. It’s also great
for personal experimentation and tinkering.

pi is another such kernel, written in TypeScript. I’ve seen similar harnesses in
other languages pop up around the Web. These pi-inspired agentic coding harness
implementations are kernels in the same way that
[the Scheme programming language is a kernel][scheme-minimalism].

> Scheme is a very simple language, much easier to implement than many other
> languages of comparable expressive power. This ease is attributable to the use
> of lambda calculus to derive much of the syntax of the language from more
> primitive forms. For instance of the 23 s-expression-based syntactic
> constructs defined in the R5RS Scheme standard, 14 are classed as derived or
> library forms, which can be written as macros involving more fundamental
> forms, principally lambda. As R5RS (§3.1) says: "The most fundamental of the
> variable binding constructs is the lambda expression, because all other
> variable binding constructs can be explained in terms of lambda expressions."

Digging into some of the commercial terminal harnesses (many of which have
source code openly available on GitHub), you can see they aren’t all that
complex either. There’s a simple core of plumbing, a kernel, wrapped in fancy
porcelain.

Anyhoo, once you’ve worked through implementing and experimenting with one of
these kernels, all sorts of opportunities catch the eye. What’s possible if I
embed such a harness in a more complex system? How much mileage can I get out of
extending a harness with domain-specific features? It’s also great education for
assessing trade-offs in a given implementation or comparing across complete
packages.

Amped to kick off some explorations!

[hugo-bowne-anderson]: https://hugobowne.substack.com/
[ivan-leo-livecoding]: https://youtu.be/dDQ4rKXeHRw
[ivan-leo-transcript-post]: https://hugobowne.substack.com/p/building-agents-that-build-themselves
[kernel-definition]: https://en.wiktionary.org/wiki/kernel#Noun
[pi-coding-post]: {filename}/pi_coding_agent.md
[pi-in-openclaw]: https://lucumr.pocoo.org/2026/1/31/pi/
[ronacher-on-pi]: {filename}/ronacher_on_pi.md
[scheme-minimalism]: https://en.wikipedia.org/wiki/Scheme_(programming_language)#Minimalism
[syntax-episode]: https://youtu.be/AEmHcFH1UgQ?si=8_IR1HJf6jc_VPkr
[zechner-lessons]: https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
