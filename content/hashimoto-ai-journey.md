---
title: 'Hashimoto: AI Adoption Journey'
date: 2026-02-11 21:03
author: C. Ross Jam
status: published
---

[Mitchell Hashimoto][mitchell-hashimoto] is another respected developer who is
pursuing a considerate, principled approach to using AI for software
development. He took a moment to document his
[journey of adoption][hashimoto-ai-journey]

> My experience adopting any meaningful tool is that I've necessarily gone
> through three phases: (1) a period of inefficiency (2) a period of adequacy,
> then finally (3) a period of workflow and life-altering discovery.
>
> In most cases, I have to force myself through phase 1 and 2 because I usually
> have a workflow I'm already happy and comfortable with. Adopting a tool feels
> like work, and I do not want to put in the effort, but I usually do in an
> effort to be a well-rounded person of my craft.
>
> This is my journey of how I found value in AI tooling and what I'm trying next
> with it. In an ocean of overly dramatic, hyped takes, I hope this represents a
> more nuanced, measured approach to my views on AI and how they've changed over
> time.

One technique he’s adopted is ["Engineer the Harness"][engineer-the-harness]

> I don't know if there is a broad industry-accepted term for this yet, but I've
> grown to calling this "harness engineering." It is the idea that anytime you
> find an agent makes a mistake, you take the time to engineer a solution such
> that the agent never makes that mistake again. I don't need to invent any new
> terms here; if another one exists, I'll jump on the bandwagon.

This space is interesting to me. Hashimoto primarily focuses on tweaking
`AGENTS.md` and related tools. It requires careful evaluation to balance costs
and benefits, but customizing the actual interactive TUI or agent loop could
also be promising. Matthew Rocklin
[demonstrated TUI hacking][rocklin-affordance] to enable affordances that made
him more productive. On the agent loop side, I’m guessing context management and
domain-specific tooling would be quite possible.

Do any of these harness frameworks provide an extension language that enables
such engineering? 🤔

[engineer-the-harness]: https://mitchellh.com/writing/my-ai-adoption-journey#step-5-engineer-the-harness
[hashimoto-ai-journey]: https://mitchellh.com/writing/my-ai-adoption-journey
[mitchell-hashimoto]: https://mitchellh.com
[rocklin-affordance]: {filename}/rocklin-s-claude-chic.md
