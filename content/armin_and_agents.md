---
title: "Armin and Agents"
date: 2025-11-25
author: "C. Ross Jam"
status: published
---

[Armin Ronacher][2] has been working on agentic systems. He’s one of the
reasons I’m skeptically optimistic about AI coding agents. His work is
a prime example of principled, considerate, measured, and
well-informed exploration of the possibilities. 

Currently he thinks [_Agent Design Is Still Hard_][1]

> TL;DR: Building agents is still messy. SDK abstractions break once
> you hit real tool use. Caching works better when you manage it
> yourself, but differs between models. Reinforcement ends up doing
> more heavy lifting than expected, and failures need strict isolation
> to avoid derailing the loop. Shared state via a file-system-like
> layer is an important building block. Output tooling is surprisingly
> tricky, and model choice still depends on the task. 

Lots of goodness and, to be honest, stuff that’s over my head at the
moment. I’m definitely not as deep in the weeds as Armin. However, I
was struck by this statement:

> ### Testing and Evals 
>
> We find testing and evals to be the hardest problem here. This is
> not entirely surprising, but the agentic nature makes it even
> harder. Unlike prompts, you cannot just do the evals in some
> external system because there’s too much you need to feed into
> it. This means you want to do evals based on observability data or
> instrumenting your actual test runs. So far none of the solutions we
> have tried have convinced us that they found the right approach
> here. Unfortunately, I have to report that at the moment we haven’t
> found something that really makes us happy. I hope we’re going to
> find a solution for this because it is becoming an increasingly
> frustrating aspect of building an agent. 

I’m primarily attracted to the plumbing aspects, tracing and
observability, but AI evals practice does not seem to be converging on
common processes.

[1]: https://lucumr.pocoo.org/2025/11/21/agents-are-hard/
[2]: https://lucumr.pocoo.org/about/
