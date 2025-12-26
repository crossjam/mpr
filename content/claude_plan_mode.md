---
title: "Claude Plan Mode"
date: 2025-12-26 16:30
author: "C. Ross Jam"
---

Armin Ronacher [dug into Claude Code’s plan mode][1] as an interested
bystander. 

> However today I had two interesting conversations with people who
> really like plan mode. As a non-user of plan mode, I wanted to
> understand how it works. So I specifically looked at the Claude Code
> implementation to understand what it does, how it prompts the agent,
> and how it steers the client. I wanted to use the tool loop just to
> get a better understanding of what I’m missing out on. 
>
> This post is basically just what I found out about how it works, and
> maybe it’s useful to someone who also does not use plan mode and
> wants to know what it actually does. 

This one took me a few days to get around to, but it turned out to be
an interesting **reflection on how I work** with Claude. In essence,
like Ronacher I’ve unknowningly recreated many key aspects of plan
mode!

Over the last month, I start every agentic coding session with a
prompt on the order of "generate a plan, in markdown format, include a
timestamp, with a task check list, and write it into a plans folder."
Then I review the plan, typically only making minor changes. 
I commit these plans to the working repository.

With a plan in place I’ll kick the agent in action. If the plan is
fairly complex, with multiple phases, and might hit usage limits, I
might ask to only complete a couple of the first phases, then pause to
let me review.

Here’s more from Armin

> Plan mode as it exists in Claude has this sort of weirdness in my
> mind where it doesn’t come quite natural to me. It might come
> natural to others! But why can I not just ask the model to plan with
> me? Why do I have to switch the user interface into a different
> mode? Plan mode is just one of many examples where I think that
> because we are already so used to writing or talking to machines,
> bringing in more complexity in the user interface takes away some of
> the magic. I always want to look into whether just working with the
> model can accomplish something similar enough that I don’t actually
> need to have another user interaction or a user interface that
> replicates something that natural language could potentially do. 
>
> This is particularly true because my workflow involves wanting to
> double check what these plans are, to edit them, and to manipulate
> them. I feel like I’m more in control of that experience if I have a
> file on disk somewhere that I can see, that I can read, that I can
> review, that I can edit before actually acting on it. The Claude
> integrated user experience is just a little bit too far away from me
> to feel natural. I understand that other people might have different
> opinions on this, but for me that experience really was triggered by
> the thought that if people have such a great experience with plan
> mode, I want to understand what I’m missing out on. 
> 
> **And now I know: I’m mostly a custom prompt to give it structure,
> and some system reminders and a handful of examples.** 

Emphasis mine on that last line.

The other nice thing about making plans explicit documentation is that 

1. Work can be handed off to another agentic system. 
2. You can try the same plan with multiple different agents.
2. Resets and restarts are easy.

[1]: https://lucumr.pocoo.org/2025/12/17/what-is-plan-mode/
