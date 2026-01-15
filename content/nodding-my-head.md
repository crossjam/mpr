---
title: Confirmation Bias
date: 2026-01-14 23:00
author: C. Ross Jam
status: published
---

Various public developers are documenting how they work with agentic coding. I’m
seeing many bits and pieces of their approach align with how I’ve been engaging
with this development style. At the same time, I learn a lot about new
techniques that could be applicable.

Do keep in mind that we’re all figuring this out as we go along. Foundational
principles are few and far between, and things change so fast that all
assumptions could be upended in a few months.

Let’s dig in a bit...

<!-- PELICAN_END_SUMMARY -->

## Armin’s View

I found myself nodding my head quite a bit reading Armin Ronacher’s
[A Year of Vibes][1].

> I’m still perplexed by how TUIs made such a strong comeback. At the moment I’m
> using Amp, Claude Code, and Pi, all from the command line. Amp feels like the
> Apple or Porsche of agentic coding tools, Claude Code is the affordable
> Volkswagen, and Pi is the Hacker’s Open Source choice for me. They all feel
> like projects built by people who, like me, use them to an unhealthy degree to
> build their own products, but with different trade-offs.
>
> I continue to be blown away by what LLMs paired with tool execution can do. At
> the beginning of the year I mostly used them for code generation, but now a
> big number of my agentic uses are day-to-day things. I’m sure we will see some
> exciting pushes towards consumer products in 2026. LLMs are now helping me
> with organizing my life, and I expect that to grow further.

My own experience parallels Ronacher’s. A year ago to date, I knew a little
about agentic coders, and maybe one TUI: [aider][3]. Now I’ve got all three of
Claude, Codex, and Gemini CLIs installed and seriously thinking of adding a few
more (_TIL [pi][2]_).

Similar thoughts from  [previously reading][5] Mario Zechner on lessons from pi.

## Over to Matthew Rocklin

Matthew Rocklin (n.b. I’m a [Coiled](https://coiled.io) fanboy) has gotten into
agentic coding [4]:

> I started AI development with Cursor. It was great having the AI experience
> inside a VSCode-like editor, where I could see everything that was going on.
> When I saw terminal-based tools like Claude Code I thought "whoa, that doesn't
> seem sensible, I need to see what's going on".
>
> Today I code with Claude Code, git diff, and occasionally vim. I don't feel a
> need or desire to OK every change in the diff. I've got more important things
> to do. I suspect that you do too.

And I’m independently warming to one of his big ideas:

> I deeply respect the philosophical position of Python, which I'll state as
> follows:
>
> > Prioritize human performance over compute performance.
> >
> > By optimizing for ease and iteration speed we're able to search solution
> > space more broadly and more quickly, finding much better solutions, making
> > that 100x drop in performance negligible.
>
> Python was a bold bet, and a bet that paid off amazingly well. No one expected
> this silly dynamic language originally designed for education to become the
> world's juggernaut in performance software.
>
> With AI though, the usability benefits of Python no longer apply as strongly,
> and we're more free to choose different ecosystems.
>
> Personally, I use ...
>
> - **Rust** for computational development, using PyO3 to connect to Python,
>   where I still do most of my testing
> - **Typescript** for frontend development, which I'm leaning into more deeply

I might swap Rust for Go as the systems language. In any event, a modern
language that embraces:

1. strong static typing
1. fast, full-program compilation
1. ecosystem-standardized linting and code formatting
1. testing facilities directly in the language

probably best supports agents in rapidly exploring the solution space.
TypeScript might be the JavaScript that was meant for me.

## Closing With Ellen

Ellen Berger is [a recent discovery][6]. But digging into her archives is
illuminating, especially
[_What AI I Use How and When (November 2025 Update)_][7]:

> AI technology develops remarkably fast. Tools evolve, new capabilities emerge,
> and what worked brilliantly six months ago might now be obsolete. My approach:
> test new things regularly when they become available, especially if I hear
> good things from other practitioners or read compelling coverage. I try to
> take these tools seriously — complete actual tasks with them, see what works
> best, then decide whether to adopt them properly and learn them well, or park
> them for later review. I also periodically reassess existing tools to see if
> I’m still as interested in them as I used to be.

> This is what I recommend to anyone working seriously with AI: constant
> experimentation balanced with building deep expertise in your core tools.

Definitely listen to Ellen and get your reps in. Also, she has some good
pointers to supporting tech, like audio dictation tools.

> ## Remote Asynchronous Agents
>
> Trend: ⬆️⬆️⬆️ Increasingly central to my workflow
>
> These are the best way to work productively with AI coding tools without
> directly babysitting them whilst they work.
>
> Main tools:
>
> - GitHub Copilot Coding Agent — Very easy to use, available on GitHub. Just
>   assign issues or trigger tasks, including from within VS Code
> - Codex Cloud — Excellent tool for async work
> - Claude Code Web — Also very good for remote tasks
>
> Much of my coding work now happens by triggering tasks, assigning them to an
> agent, and letting them work in the background.

Honestly, GitHub Copilot feels like magic to me at the moment.

[1]: https://lucumr.pocoo.org/2025/12/22/a-year-of-vibes/
[2]: https://shittycodingagent.ai
[3]: https://aider.chat
[4]: https://matthewrocklin.com/ai-zealotry/
[5]: %7Bfilename%7D/pi_coding_agent.md
[6]: %7Bfilename%7D/a-ruler-for-agentic-coding.md
[7]: https://everything.intellectronica.net/p/november-2025-what-ai-i-use-how-and-when
