---
title: Building Agentic Kernels
date: 2026-02-28 21:30
author: C. Ross Jam
---

After having [digested][pi-coding-post] Mario Zechner’s
[lessons][zechner-lessons] regarding the pi coding agent, along with
[pondering][ronacher-on-pi] Armin Ronacher’s [dissection of OpenClaw
and pi][pi-in-openclaw], I find the core of agentic coding harnesses
intriguing. These guys were both together on a Syntax [podcast
episode][syntax-episode] and quite the hoot! The gist of the
discussion was that pi is really simple, ridiculously effective, and
highly dangerous! The danger comes from letting an agent
(LLM+tools+loop) have full access to your file system with your
permissions.  The effectiveness emerges because pi starts with limited
functionality but can easily modify itself while continuing to run.

Multiple recent webinars I’ve attended have essentially similarly
proclaimed, "you can build one of these harnesses in (much) less than
1000 lines of code, " with 1000 being generous. The prolific [Hugo
Bowne-Anderson][hugo-bowne-anderson] recently held [a workshop /
livecoding session][ivan-leo-livecoding] that did exactly this.

> Yesterday, I ran a workshop with Ivan Leo (ex-Manus) called
> “Building Your Own OpenClaw from Scratch” to show you how to build
> your own AI assistant from first principles. We covered: 
> 
> * How coding agents are really general-purpose computer use agents
>   that happen to be great at writing code 
> * Building the core agent loop with an LLM and tool calls 
> * Context management, memory compaction, and progressive disclosure 
> * How agents can write their own tools and hot-reload them on the
>   fly (via a factory pattern) 
> * Making the agent trigger actions automatically (send a Telegram
>   message, log to a database, fire off an email) using hooks 
> * Connecting the agent to Telegram via FastAPI
> * Sandboxing and production deployment with Modal
> 
> We wrote this blog post for those who don’t have 100 minutes to
> watch the entire workshop right now.

I’m one of those folks who didn’t have 100 minutes this past Friday to
watch, but definitely want to go back and review the recording.  The
[blog post][ivan-leo-transcript-post] is pretty hefty, building up a
conceptual design and framework, then providing the gory details of
actual implementation in Python.

After having read the article end-to-end, I see a clear path to a
developer using this as a pedagogical starting point, but then
building further. This could be by just starting with Leo’s code and
extending with new concepts, or conducting a port to another language
or system. The code from this session is small enough that it can be
an operational [kernel][kernel-definition] for building more complex
things. It’s also great for personal experimentation.

pi is another such kernel, written in TypeScript. I’ve seen variations
in other languages popup around the Web.  These pi inspired agentic
coding harness implementations are kernels in the way that [the Scheme
programming language is a kernel][scheme-minimalism].

> Scheme is a very simple language, much easier to implement than many
> other languages of comparable expressive power. This ease is
> attributable to the use of lambda calculus to derive much of the
> syntax of the language from more primitive forms. For instance of
> the 23 s-expression-based syntactic constructs defined in the R5RS
> Scheme standard, 14 are classed as derived or library forms, which
> can be written as macros involving more fundamental forms,
> principally lambda. As R5RS (§3.1) says: "The most fundamental of
> the variable binding constructs is the lambda expression, because
> all other variable binding constructs can be explained in terms of
> lambda expressions." 

Digging in to some of the commercial terminal harnesses (many of which
have source code openly available on GitHub) you can see they aren’t
all that complex. There’s a simple core of plumbing, wrapped in fancy
porcelain.

Anyhoo, once you’ve worked through implementing and experimenting with
one of these kernels, all sorts of opportunities catch the eye. What’s
possible if I embed such a harness in a more complex system? How much
mileage can I get out of extending a harness with domain specific
features.It’s also great education for assessing tradeoffs in a given
implementation or comparing across complete packages.

[pi-coding-post]: {filename}/pi_coding_agent.md
[pi-coding-agent]: https://shittycodingagent.ai
[zechner-lessons]: https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
[ronacher-on-pi]: {filename}/ronacher_on_pi.md
[pi-in-openclaw]: https://lucumr.pocoo.org/2026/1/31/pi/
[hugo-bowne-anderson]: https://hugobowne.substack.com/
[ivan-leo-livecoding]: https://youtu.be/dDQ4rKXeHRw
[ivan-leo-transcript-post]: https://hugobowne.substack.com/p/building-agents-that-build-themselves
[scheme-minimalism]: https://en.wikipedia.org/wiki/Scheme_(programming_language)#Minimalism
[kernel-definition]: https://en.wiktionary.org/wiki/kernel#Noun
[syntax-episode]: https://youtu.be/AEmHcFH1UgQ?si=8_IR1HJf6jc_VPkr
