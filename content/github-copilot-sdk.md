---
title: GitHub Copilot SDK
date: 2026-01-26 22:22
author: C. Ross Jam
status: published
---

GitHub Copilot now has [an SDK][gh-copilot-sdk]!

From [the announcement blog post][gh-copilot-sdk-post]:

> Building agentic workflows from scratch is hard.
>
> You have to manage context across turns, orchestrate tools and commands, route
> between models, integrate MCP servers, and think through permissions, safety
> boundaries, and failure modes. Even before you reach your actual product
> logic, you’ve already built a small platform.
>
> GitHub Copilot SDK (now in technical preview) removes that burden. It allows
> you to take the same Copilot agentic core that powers GitHub Copilot CLI and
> embed it in any application.
>
> This gives you programmatic access to the same production-tested execution
> loop that powers GitHub Copilot CLI. That means instead of wiring your own
> planner, tool loop, and runtime, you can embed that agentic loop directly into
> your application and build on top of it for any use case.
>
> You also get Copilot CLI’s support for multiple AI models, custom tool
> definitions, MCP server integration, GitHub authentication, and real-time
> streaming.

I’ll have more to say in an upcoming post, but the fact that platforms
like Claude, GitHub Copilot, et al. have SDKs explodes the optionality
in agentic coding. You can **embed** these frameworks into bespoke
tooling along with their built-in **extension** mechanisms, like
skills, and MCP. In a past life, I used to make the argument that
"scripting" languages were high leverage because they intentionally
supported both embedding and extending.

As an old Lisp weenie, I definitely comprehend that there are limits on the
utility of extreme environment customization. For solo developers, it’s a win.
For teams and organizations that need consistent, shared development practices,
it’s a challenge. Letting a thousand flowers bloom is wonderful until you have
to transfer standards and expertise between developers.

One angle of deep interest, though, is the rapid creation of domain-specific
platforms for niche, high-expertise audiences.

[gh-copilot-sdk]: https://github.com/github/copilot-sdk
[gh-copilot-sdk-post]: https://github.blog/news-insights/company-news/build-an-agent-into-any-app-with-the-github-copilot-sdk/
