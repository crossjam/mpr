---
title: Ai2, Open Coding Agents
date: 2026-01-28 23:00
author: C. Ross Jam
status: published
---

Ai2, the Allen Institute for AI, is admirable in that it releases fully open
large models: data, code, and weights. This week they announced
[_Open Coding Agents_][open-coding-agents]

> Over the past year, coding agents have transformed how developers write, test,
> and maintain software. These systems can debug, refactor, and even submit pull
> requests—fundamentally changing what software development looks like. Yet
> despite this progress, most coding agents share the same constraints: they're
> closed, expensive to train, and difficult to study or adapt to private
> codebases.
>
> Ai2 Open Coding Agents change that. Today we’re releasing not just a
> collection of strong open coding models, but a training method that makes
> building your own coding agent for any codebase – for example, your personal
> codebase or an internal codebase at your organization – remarkably accessible
> for tasks including code generation, code review, debugging, maintenance, and
> code explanation.
>
> ...
>
> The first release in our Open Coding Agents family is SERA (Soft-verified
> Efficient Repository Agents). The strongest – SERA-32B – solves 54.2% of
> SWE-Bench Verified problems, surpassing prior open-source state-of-the-art
> coding models of comparable sizes and context lengths while requiring only 40
> GPU days (or fewer) to train on a cluster of 2 NVIDIA Hopper GPUs or NVIDIA
> RTX PRO 6000 Blackwell Server Edition GPUs. SERA models are optimized and
> compatible with Claude Code out of the box. With our fine-tuning method, you
> can specialize them to your own codebase including your full engineering stack
> and conventions quickly and at low cost.

These releases are great building blocks for further open-source development. To
be clear, SERA is a fine-tuned version of [Qwen 3][qwen-3], so it doesn't
provide complete end-to-end transparency.

They're also useful for independent learning. A genuinely benchmark-competitive
model with freely available training data and code is a nice starter kit for a
class. Plus these present realistic application of modern
post-training approaches.

With the crazy functionality and robustness of current TUI frameworks,
it’s not inconceivable a small-to-medium-sized business can completely own
their agentic coding stack.

[open-coding-agents]: https://allenai.org/blog/open-coding-agents
[qwen-3]: https://qwen.ai/blog?id=qwen3
