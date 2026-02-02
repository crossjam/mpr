---
title: Ronacher On Pi
date: 2026-02-01 22:30
author: C. Ross Jam
status: published
---

Maybe I was ahead of the curve relative to [OpenClaw]?
[Previously, I noted][previously-noted] Mario
[Zechner's lessons][zechners-lessons] from building [pi][pi-coding-agent], an
alternative coding agent. According to Armin Ronacher,
[pi is at the core of OpenClaw][pi-in-openclaw].

> If you haven't been living under a rock, you will have noticed this week that
> a project of my friend Peter went viral on the internet. It went by many
> names. The most recent one is OpenClaw but in the news you might have
> encountered it as ClawdBot or MoltBot depending on when you read about it. It
> is an agent connected to a communication channel of your choice that just runs
> code.
>
> What you might be less familiar with is that what's under the hood of OpenClaw
> is a little coding agent called Pi. And Pi happens to be, at this point, the
> coding agent that I use almost exclusively. Over the last few weeks I became
> more and more of a shill for the little agent. After I gave a talk on this
> recently, I realized that I did not actually write about Pi on this blog yet,
> so I feel like I might want to give some context on why I'm obsessed with it,
> and how it relates to OpenClaw.
>
> Pi is written by Mario Zechner and unlike Peter, who aims for "sci-fi with a
> touch of madness," Mario is very grounded. Despite the differences in
> approach, both OpenClaw and Pi follow the same idea: LLMs are really good at
> writing and running code, so embrace this. In some ways I think that's not an
> accident because Peter got me and Mario hooked on this idea, and agents last
> year.

Do read Armin's post. He deep dives into what's elegant about pi and how that
elegance enables the madness that is OpenClaw. Per Armin's typical attention to
detail, he clearly and efficiently describes the key design points of pi. Even
better, he introspects on how he extends the system to increase his own
productivity.

> These are all just ideas of what you can do with your agent. The point of it
> mostly is that none of this was written by me, it was created by the agent to
> my specifications. I told Pi to make an extension and it did. There is no MCP,
> there are no community skills, nothing. Don't get me wrong, I use tons of
> skills. But they are hand-crafted by my clanker and not downloaded from
> anywhere. For instance I fully replaced all my CLIs or MCPs for browser
> automation with a skill that just uses CDP. Not because the alternatives don't
> work, or are bad, but because this is just easy and natural. The agent
> maintains its own functionality.

I think it's fair to label a self-modifying, agentic coding framework as
madness. 🫤

[openclaw]: https://openclaw.ai
[pi-coding-agent]: https://shittycodingagent.ai
[pi-in-openclaw]: https://lucumr.pocoo.org/2026/1/31/pi/
[previously-noted]: {filename}/pi_coding_agent.md
[zechners-lessons]: https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
