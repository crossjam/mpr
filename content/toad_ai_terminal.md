---
title: Toad, AI In The Terminal
date: 2026-01-18 22:15
author: C. Ross Jam
status: published
---

Out of [the ashes of Textualize][ashes], Will McGugan has created [toad]: "A
unified interface for AI in your terminal".

From [McGugan’s release announcement][release]:

> My startup for terminals wrapped up mid-2025 when the funding ran dry. So I
> don’t have money, but what I do have are a very particular set of skills.
> Skills I have acquired over a very long career convincing terminals they are
> actually GUIs.
>
> Skills which I have used to create a terminal app that offers a more pleasant
> experience for agentic coding. Toad (a play on Textual Code) is a front-end
> for AI tools such as OpenHands, Claude Code, Gemini CLI, and many more. All of
> which run seamlessly under a single terminal UI, thanks to the ACP protocol.
>
> At the time of writing, Toad supports 12 agent CLIs, and I expect many more to
> come online soon.

I discovered toad via Rui Carmo, who has been working on a sandbox for various
agents, duly named [agentbox]:

> ## Agentbox - Coding Agent Sandbox
>
> There's no perfect way to sandbox agents (yet), but at least we can try
> limiting the damage using containers.
>
> Agentbox is a simple Docker-based coding agent sandbox, originally inspired by
> running Batrachian Toad as a general-purpose coding assistant TUI and now
> generalized to more tools.
>
> Whatever agent you prefer, Agentbox aims to provide a reliable and isolated
> environment which will help you boostrap pretty much any development
> environment.
>
> ### Motivation
>
> I found myself wanting to quickly spin up isolated coding environments for AI
> agents, without having to deal with complex orchestration tools or heavy VMs,
> and also wanting to limit CPU usage from Batrachian Toad itself.

With LLMs and agentic coding igniting a renaissance in CLIs and textual
interfaces, old UNIX-heads like me are having a grand old time.

[agentbox]: https://github.com/rcarmo/agentbox
[ashes]: https://willmcgugan.github.io/whats-next/
[release]: https://willmcgugan.github.io/toad-released/
[toad]: https://github.com/batrachianai/toad?tab=readme-ov-file
