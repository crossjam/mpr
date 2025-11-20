---
title: "Anthropic’s Claude Code Best Practices"
date: 2025-11-19
author: "C. Ross Jam"
status: published
---

Link parkin’: [_"Claude Code: Best practices for agentic coding"_][1]

> Claude Code is a command line tool for agentic coding. This post
> covers tips and tricks that have proven effective for using Claude
> Code across various codebases, languages, and environments. 

In particular, I’m looking at extending my own Claude Code environment
as documented in this piece to integrate the [GitHub CLI][3]

> For repeated workflows—debugging loops, log analysis, etc.—store
> prompt templates in Markdown files within the .claude/commands
> folder. These become available through the slash commands menu when
> you type /. You can check these commands into git to make them
> available for the rest of your team.
> 
> Custom slash commands can include the special keyword $ARGUMENTS to
> pass parameters from command invocation. 
>
> For example, here’s a slash command that you could use to
> automatically pull and fix a Github issue: 

I need to do some research on whether this approach or [Agent
Skills][2] is better. Maybe this note from the skills docs will solve
the question:

> How Skills are invoked: Skills are model-invoked—Claude autonomously
> decides when to use them based on your request and the Skill’s
> description. This is different from slash commands, which are
> user-invoked (you explicitly type /command to trigger them). 

[1]: https://www.anthropic.com/engineering/claude-code-best-practices
[2]: https://code.claude.com/docs/en/skills
[3]: https://cli.github.com/manual/
