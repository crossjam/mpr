---
title: "Agor: Agent Orchestration"
date: 2025-11-28
author: "C. Ross Jam"
status: published
---

Link parkin’: [Agor][1]

> Think Figma, but for AI coding assistants. Orchestrate Claude Code,
> Codex, and Gemini sessions on a multiplayer canvas. Manage git
> worktrees, track AI conversations, and visualize your team's agentic
> work in real-time. 
>
> > TL;DR: Agor is a multiplayer spatial canvas where you coordinate
> > multiple AI coding assistants on parallel tasks, with GitHub-linked
> > worktrees, automated workflow zones, and isolated test
> > environments—all running simultaneously. 
> 

Picked this up from [an episode of the Data Engineering Podcast][2]
featuring [Max Beauchemin of Apache Airflow][3] and [Apache
Superset][4] fame. Definitely give it a listen.

> In this crossover episode, Max Beauchemin explores how multiplayer,
> multi‑agent engineering is transforming the way individuals and
> teams build data and AI systems. He digs into the shifting boundary
> between data and AI engineering, the rise of “context as code,” and
> how just‑in‑time retrieval via MCP and CLIs lets agents gather what
> they need without bloating context windows. Max shares hard‑won
> practices from going “AI‑first” for most tasks, where humans focus
> on orchestration and taste, and the new bottlenecks that appear —
> code review, QA, async coordination — when execution accelerates
> 2–10x. He also dives deep into Agor, his open‑source agent
> orchestration platform: a spatial, multiplayer workspace that
> manages Git worktrees and live dev environments, templatizes prompts
> by workflow zones, supports session forking and sub‑sessions, and
> exposes an internal MCP so agents can schedule, monitor, and even
> coordinate other agents. 

It's very early days for Agor, but the UX Beauchemin described was
interesting. Effectively, he hijacked Kanban cards as a frontend for
agent orchestration. The claim is that Agor is great for individual
users and is showing promise for teams. Also, a wide range of agentic
coders are supported, including Claude Code, Codex, Gemini, and
opencode. User interfaces in the orchestration space should be open
season for experimentation. 

[1]: https://agor.live
[2]: https://www.dataengineeringpodcast.com/episodepage/blurring-lines-data-ai-and-the-new-playbook-for-team-velocity
[3]: https://en.wikipedia.org/wiki/Apache_Airflow
[4]: https://superset.apache.org 


