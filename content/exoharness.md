---
title: exoharness
date: 2026-08-19
author: "C. Ross Jam"
status: published
---

Speaking of Cal folks and harnesses, rummaging around on YouTube, I
chanced across Latent Space [lightning podcast][lightning-podcast]
with [Swyx] and [Alexander Krentsel][krentsel] on [exoharness]

> exoharness is a minimal architecture for building agents. It
> separates trusted infrastructure for state, resources, and security
> from agent-specific logic that can evolve, stop, resume, and rewind
> across runs. 


YouTube embed after the break. I can’t do the conversation technical
justice, but this is what happens to harness engineering when you let
hardcore Systems folks get after it.

<!-- PELICAN_END_SUMMARY --> 


Here’s some pull quotes from [spec][exoharness-spec] document:

> A harness often conflates two different concerns: the infrastructure
> required to serve an agent, such as message history, secure access
> to privileged resources, and sandboxes, and the semantics of how the
> agent thinks and acts, such as compaction, memory, and
> programmability choices like bash, JavaScript, or SQL tools. 
>
> To make that separation explicit, this doc introduces the idea of an
> exoharness: a trusted substrate that manages durable state, brokers
> access to privileged resources, and provides low-level execution
> plumbing without owning agent semantics. The exoharness manages the
> non-semantic substrate. 
>
> An executor is the layer that owns those semantics: it runs the turn
> loop, including prompt assembly, model calls, tool use, and memory
> or compaction policy. A harness is the combination of an exoharness
> and an executor. 
>
> ...
>
> * The exoharness gives you durable conversations, sessions, turns,
>   append-only events, artifacts, bindings, secrets, and sandboxes. 
> * The executor still owns the semantics: prompt assembly, model
>   calls, memory and compaction policy, approvals UX, and the turn
>   loop. 
> * A harness is what most people actually use: an executor built on
>   top of an exoharness. 

This is all in service of advancing the state of the art for
[Recursive Self-Improvement][rsi] in agentic harnesses.


[!embed](https://youtu.be/5lFD-34dhqE?si=paWOGK5m2UUfZPhn)

[exoharness]: https://exoharness.ai
[lightning-podcast]: https://youtu.be/5lFD-34dhqE?si=paWOGK5m2UUfZPhn
[krentsel]: https://www.krentsel.com/
[swyx]: https://swyx.io
[exoharness-spec]: https://github.com/exoharness/exo/blob/main/exoharness/docs/spec.md
[rsi]: https://en.wikipedia.org/wiki/Recursive_self-improvement
