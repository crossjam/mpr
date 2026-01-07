--- 
title: OpenAI PLANS.md
date: 2026-01-07 14:30
author: C. Ross Jam
status: published
---

I’ve had this [blog post on exec plans][1] from the OpenAI Cookbook sitting in a
tab for a while. Mainly, I was stuck pondering how Codex could be induced to run
for multiple hours. To date, my agentic coding has pretty much peaked at keeping
an agent engaged for ten to twenty minutes.

> Codex and the gpt-5.2-codex model (recommended) can be used to implement
> complex tasks that take significant time to research, design, and implement.
> The approach described here is one way to prompt the model to implement these
> tasks and to steer it towards successful completion of a project.
>
> These plans are thorough design documents, and "living documents". As a user
> of Codex, you can use these documents to verify the approach that Codex will
> take before it begins a long implementation process. The particular PLANS.md
> included below is very similar to one that has enabled Codex to work for more
> than seven hours from a single prompt.
>
> We enable Codex to use these documents by first updating AGENTS.md to describe
> when to use PLANS.md, and then of course, to add the PLANS.md file to our
> repository.

Then I took a closer look at the [source for PLANS.md][2] and noticed how it
aligned with much of my current process for agentic coding, but on steroids. For
example, I routinely ask my agents to create task checklists when generating
plans and then track progress during implementation by checking items off.

It’s definitely not an exact match  (I encourage agents to apply timestamps within
plans as much as possible) but then again I’m not OpenAI in terms of scale and
velocity. Meanwhile, I’ve already learned quite a bit about steering agents from
some initial reading. Otherwise, this looks like a nice component to add to my
[agentic-project-cookiecutter][3].


[1]: https://cookbook.openai.com/articles/codex_exec_plans
[2]: https://github.com/openai/openai-cookbook/blob/499c4c8719bbae2394f856a87647d56d4afe8b06/articles/codex_exec_plans.md?plain=1#L21
[3]: https://github.com/crossjam/agentic-project-cookiecutter
