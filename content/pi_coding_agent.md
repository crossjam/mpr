---
title: "pi coding agent"
date: 2026-01-03 13:30
author: "C. Ross Jam"
status: published
---

Thanks to Armin Ronacher, I learned about the [pi coding agent][1]. Mario
Zechner’s blog post on [what he learned building pi][2] outlines his underlying
principles in creating an agentic coding framework:

> In the past three years, I've been using LLMs for assisted coding. If you read
> this, you probably went through the same evolution: from copying and pasting
> code into ChatGPT, to Copilot auto-completions (which never worked for me), to
> Cursor, and finally the new breed of coding agent harnesses like Claude Code,
> Codex, Amp, Droid, and opencode that became our daily drivers in 2025.
>
> ...
>
> So what's an old guy yelling at Claudes going to do? He's going to write his
> own coding agent harness and give it a name that's entirely un-Google-able, so
> there will never be any users. Which means there will also never be any issues
> on the GitHub issue tracker. How hard can it be?
>
> To make this work, I needed to build:
>
> - [pi-ai][3]: A unified LLM API with multi-provider support (Anthropic,
>   OpenAI, Google, xAI, Groq, Cerebras, OpenRouter, and any OpenAI-compatible
>   endpoint), streaming, tool calling with TypeBox schemas, thinking/reasoning
>   support, seamless cross-provider context handoffs, and token and cost
>   tracking.
> - [pi-agent-core][4]: An agent loop that handles tool execution, validation,
>   and event streaming.
> - [pi-tui][5]: A minimal terminal UI framework with differential rendering,
>   synchronized output for (almost) flicker-free updates, and components like
>   editors with autocomplete and markdown rendering.
> - [pi-coding-agent][6]: The actual CLI that wires it all together with session
>   management, custom tools, themes, and project context files.
>
> My philosophy in all of this was: if I don't need it, it won't be built. And I
> don't need a lot of things.

One of the things about this new era of agentic coding that excites me is the
Cambrian explosion of interaction paradigms. I’m just using a few of the popular
TUIs and cloud agents as an individual developer. Within that regime, the space of
available tools and refinement mechanisms (MCP, skills, hooks, agent-specific
CLI tools, extensions, and version-control integration) can seem overwhelming.

pi looks like a well-designed, highly opinionated, modular approach. In 2026,
I’m going to invest some time seeing if I can be productive with pi. Once that
succeeds, I’ll go a level deeper and see if I can’t customize pi into
a tool that fits my hand well.

[1]: https://shittycodingagent.ai
[2]: https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
[3]: https://github.com/badlogic/pi-mono/tree/main/packages/ai
[4]: https://github.com/badlogic/pi-mono/tree/main/packages/agent
[5]: https://github.com/badlogic/pi-mono/tree/main/packages/tui
[6]: https://github.com/badlogic/pi-mono/tree/main/packages/coding-agent
