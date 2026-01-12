---
title: harbor
date: 2026-01-11 21:45
author: C. Ross Jam
status: published
---

Link parkin’: the [harbor][1] framework.

From the [docs][2]:

> ## Motivation
>
> Why we built Harbor
>
> Harbor is a framework for evaluating and optimizing agents and models in
> container environments.
>
> When we released Terminal-Bench in May, we were surprised to see it used in
> unexpected ways like building custom evals, optimizing prompts, running RL,
> generating SFT traces, and CI/CD agent testing.
>
> We also learned that defining and managing containerized tasks at scale is
> hard. We built Harbor to make it easy.
>
> Harbor provides:
>
> - Simple, modular interfaces for environments, agents, and tasks
> - All popular CLI agents pre-integrated
> - A registry of popular benchmarks and datasets
> - Integrations with cloud sandbox providers like Daytona, Modal, and E2B for
>   horizontal scaling
> - Integrations with frameworks like SkyRL and GEPA for optimizing agents

Related: [Simon Willison on a new product, Sprites.dev][3] from Fly.io:

> New from Fly.io today: [Sprites.dev][4]. Here’s their blog post and YouTube
> demo. It’s an interesting new product that’s quite difficult to explain—Fly
> call it “Stateful sandbox environments with checkpoint & restore” but I see it
> as hitting two of my current favorite problems: a safe development environment
> for running coding agents and an API for running untrusted code in a secure
> sandbox.

And [directly from Kurt Mackey, the horse’s mouth][5]:

> The state of the art in agent isolation is a read-only sandbox. At Fly.io,
> we’ve been selling that story for years, and we’re calling it: ephemeral
> sandboxes are obsolete. Stop killing your sandboxes every time you use them.
>
> ...
>
> We have a lot to say about how Sprites work. They’re related to Fly Machines
> but sharply different in important ways. They have an entirely new storage
> stack. They’re orchestrated differently. No Dockerfiles.
>
> But for now, I just want you to think about what I’m saying here. Whether or
> not you ever boot a Sprite, ask: if you could run a coding agent anywhere,
> would you want it to look more like a read-only sandbox in a K8s cluster in
> the cloud, or like an entire EC2 instance you could summon in the snap of a
> finger?
>
> I think the answer is obvious. The age of sandboxes is over. The time of the
> disposable computer has come.

And here I’m only mentioning a small slice of what’s going on in the
space. Willison’s post covers multiple other offerings and that’s not
even close to comprehensive. Innovation in isolated execution,
including containers, is getting a bump due to agentic coding.

[1]: https://harborframework.com
[2]: https://harborframework.com/docs
[3]: https://simonwillison.net/2026/Jan/9/sprites-dev/
[4]: https://sprites.dev
[5]: https://fly.io/blog/code-and-let-live/
