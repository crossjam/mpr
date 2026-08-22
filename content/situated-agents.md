---
title: "Situated Agents"
date: 2026-08-18
modified: 2026-08-19
author: "C. Ross Jam"
status: published
---

[Drew Breunig][dbreunig] recently [posted about agent
harnesses][harness-post] and started off like so:

> Harrison Chase once excitedly shared an insight that agents are
> comprised of 4 things: a system prompt, a planning tool, a file
> system, and subagents. In the year-plus since he said that, I think
> this remains largely true. (Though you might tweak it to have general
> tools, etc.)
> 
> Lately, we’ve been experiencing a wave of harnesses. It seems like
> everyday a new coding harness lands. I’m sure we’ll see another few
> dozen before the month is out.

Not a bad characterization by Chase. Today you’d have to add a set of
tools for agentic loops though.

And not a bad piece by Breunig either. I consider myself a bit of a
[harness connoisseur][cursor-cli-post] and there were quite a few he
listed that I hadn’t heard of. [Prime Agent][prime-agent] has
some interesting core concepts ([RLM], [Continual
Harness][continual-harness]) and seems small enough to fit in one’s
head. Not quite sure what to make of [QM] but it could make sense for
organizations extremely into agentic deployment.

I’m usually down with my Cal peeps (_Go Bears!_), but Matei and the
team at Databricks may have gone a bit too meta with [Omnigent]. 

> So we built Omnigent: a meta-harness that sits above the agents you
> already use (Claude Code, Codex, Pi, or custom agents) and makes
> them interoperable parts of a richer system. Omnigent targets the
> problems where a single harness stops: it adds easy ways to compose
> multiple agents, control them with advanced policies, and
> collaborate live with teammates. 

> We believe people will soon work with agents through this new layer,
> the meta-harness. That’s why today we’re open sourcing Omnigent
> under Apache 2.0. 

Then again, the AMP Lab alums do have a solid track record, so maybe
Omnigent will join the ranks of Spark and MLflow. 

Just check out who the first author was on this 2024 (?!) [position
post on compound AI systems][compound-systems] from the Berkeley
Artificial Intelligence Research Lab:

> AI caught everyone’s attention in 2023 with Large Language Models
> (LLMs) that can be instructed to perform general tasks, such as
> translation or coding, just by prompting. This naturally led to an
> intense focus on models as the primary ingredient in AI application
> development, with everyone wondering what capabilities new LLMs will
> bring. As more developers begin to build using LLMs, however, we
> believe that this focus is rapidly changing: state-of-the-art AI
> results are increasingly obtained by compound systems with multiple
> components, not just monolithic models. 


Back to Breunig who approaches his conclusion with: 

> The burst of harness innovation, I believe, isn’t going to slow
> because managing these layers is much stickier than less-situated
> agents. It’s trivial to jump from Claude Code to Codex when one
> tires of Opus’s writing, but if the entire org and team have already
> set up a system that manages all of the above, it’s really hard to
> shift. 

Fun times in this space and catnip for systems folks like me.


[harness-post]: https://www.dbreunig.com/2026/08/14/harnesses-are-situated-agents.html
[dbreunig]: https://www.dbreunig.com/
[cursor-cli-post]: {filename}/cursor_cli.md
[prime-agent]: https://github.com/PrimeIntellect-ai/prime-agent
[rlm]: https://www.primeintellect.ai/blog/rlm
[continual-harness]: https://arxiv.org/abs/2605.09998
[qm]: https://qm.ycombinator.com
[omnigent]: https://www.databricks.com/blog/introducing-omnigent-meta-harness-combine-control-and-share-your-agents
[compound-systems]: https://bair.berkeley.edu/blog/2024/02/18/compound-ai-systems/
