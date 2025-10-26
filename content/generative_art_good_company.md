---
title: "In Good Company: Agentic Generative Art"
date: 2025-10-26
author: "C. Ross Jam"
status: published
---

I was poking around in Claude’s configuration menus and noticed this:

![A screen capture of the Claude desktop config menu showing a skill
for algorithmic art][6]

Well, well, well. Claude really does have [a skill for generative
art][1]. Here’s a quick quote from [the skill’s markdown][7]:

> Creating algorithmic art using p5.js with seeded randomness and
> interactive parameter exploration. Use this when users request
> creating art using code, generative art, algorithmic art, flow
> fields, or particle systems. Create original algorithmic art rather
> than copying existing artists' work to avoid copyright violations.

A [skill for Claude][3] extends the system sort of like MCP and tools
but with less code:

> Claude can now use Skills to improve how it performs specific
> tasks. Skills are folders that include instructions, scripts, and
> resources that Claude can load when needed. 

> Claude will only access a skill when it's relevant to the task at
> hand. When used, skills make Claude better at specialized tasks like
> working with Excel or following your organization's brand
> guidelines. 

The Anthropic engineering blog has a deeper dive into [the overall
design and intent of skills][4]:

> Building a skill for an agent is like putting together an onboarding
> guide for a new hire. Instead of building fragmented,
> custom-designed agents for each use case, anyone can now specialize
> their agents with composable capabilities by capturing and sharing
> their procedural knowledge. In this article, we explain what Skills
> are, show how they work, and share best practices for building your
> own. 

And if that isn’t enough for you, Simon Willison 
jumps in with his trademark enthusiasm, [_Claude Skills are awesome,
maybe a bigger deal than MCP_][5]


The `algorithmic-art`skill relies on [p5.js][2] to implement requested pieces. This
makes sense given Claude Code’s TypeScript foundation. What’s crazy to
me is that the Skills mechanism adds the entirety of that previously
linked markdown to the LLM context if the skill is needed. That’s a
lot of tokens consumed! On the flip side, it’s a tremendous example of
actual prompting for generative art in the wild. 

Just more motivation to pursue new dreams of agentic generative art
using Python. Oft attributed to Picasso, "good artists copy, great
artists steal." I might not be either, but I’ll definitely be
examining that skill for inspiration.

[1]: https://github.com/anthropics/skills/tree/main/algorithmic-art
[2]: https://p5js.org
[3]: https://www.anthropic.com/news/skills
[4]: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
[5]: https://simonwillison.net/2025/Oct/16/claude-skills/
[6]: {static}/images/claude_settings.png
[7]: https://github.com/anthropics/skills/tree/main/algorithmic-art/SKILL.md
[8]: {filename}/agentic_generative_art_coding.md
