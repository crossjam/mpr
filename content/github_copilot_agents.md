---
title: "Enjoying GitHub Copilot Agents"
date: 2025-11-29
author: "C. Ross Jam"
status: published
---

In my agentic coding explorations, I’m really liking [the coding agents
provided by GitHub Copilot][2]. Here’s [the 101 intro][1].

> Earlier this year, GitHub introduced an integrated, enterprise-ready
> coding agent for Copilot. Coding agent is a software engineering
> (SWE) agent that runs independently in the background to complete
> assigned tasks — similar to a peer developer. 
>
> The agent starts its work when you hand it a task. Then it spins up
> a fully customizable development environment, powered by GitHub
> Actions. You can track it every step of the way, from issue to pull
> request to review to approval. 
>
> The agent is designed to help you offload tasks like fixing bugs,
> test coverage, or refactoring code, so you can work on what
> interests you most. ✨ 

More from the docs:

> Benefits over traditional AI workflows
>
> When used effectively, Copilot coding agent offers productivity
> benefits over traditional AI assistants in IDEs: 
> 
> With AI assistants in IDEs, coding happens locally. Individual
> developers pair in synchronous sessions with the AI
> assistant. Decisions made during the session are untracked and lost
> to time unless committed. Although the assistant helps write code,
> the developer still has a lot of manual steps to do: create the
> branch, write commit messages, push the changes, open the PR, write
> the PR description, get a review, iterate in the IDE, and
> repeat. These steps take time and effort that may be hard to justify
> for simple or routine issues. 
> 
> With Copilot coding agent, all coding and iterating happens on
> GitHub as part of the pull request workflow. You can create multiple
> custom agents that specialize in different types of tasks. Copilot
> automates branch creation, commit message writing and pushing, PR
> opening, and PR description writing. Developers let the agents work
> in the background and then steer Copilot to a final solution using
> PR reviews. Working on GitHub adds transparency, with every step
> happening in a commit and being viewable in logs, and opens up
> collaboration opportunities for the entire team. 

The integration with GitHub, no surprise, is excellent and really
working well for me. It’s easy to interact with an agent through a
PR. Launching agents based upon GitHub Issues is trivial and
natural. I can actually push commits to an agent’s development branch
seamlessly. The UX on the agent session tracking has been better than
what I’ve experienced with Claude Code, Codex, and Jules. Not a huge
difference but the polish feels a notch above.

The only downer so far is that you don’t have any way to specify a
particular model to use. Despite that the code results have been on
par from what I’ve seen from other coding agents. In any event, I
ponied up for a $10 a month subscription and I’m already cranking
through features on personal projects. Feels like good value.


[1]: https://github.blog/ai-and-ml/github-copilot/github-copilot-coding-agent-101-getting-started-with-agentic-workflows-on-github/
[2]: https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent
