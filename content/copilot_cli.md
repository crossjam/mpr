---
title: "GitHub Copilot CLI"
date: 2026-01-31
author: "C. Ross Jam"
---

Link parkin’: [GitHub Copilot CLI][1].

> Agent-powered, GitHub-native
>
> Execute coding tasks with an agent that knows your repositories, issues, and
> pull requests—all natively in your terminal.

It’s really a knockoff of Claude Code but, as might be expected, incorporates
nice integration with GitHub features like issues and PRs. Interestingly, the
default model is Claude Sonnet 4.5.

Using GitHub Copilot [locally][3] is what grabs me.

> The command-line interface (CLI) for GitHub Copilot allows you to use Copilot
> directly from your terminal. You can use it to answer questions, write and
> debug code, and interact with GitHub.com. For example, you can ask Copilot to
> make some changes to a project and create a pull request.
>
> GitHub Copilot CLI gives you quick access to a powerful AI agent, without
> having to leave your terminal. It can help you complete tasks more quickly by
> working on your behalf, and you can work iteratively with GitHub Copilot CLI
> to build the code you need.

But then you can actually [delegate work back to a cloud agent][2]:

> Delegate tasks to Copilot coding agent
>
> The delegate command lets you push your current session to Copilot coding
> agent on GitHub. This lets you hand off work while preserving all the context
> Copilot needs to complete your task.
>
> You can delegate a task using the slash command, followed by a prompt:
>
> > /delegate complete the API integration tests and fix any failing edge cases
>
> Copilot will ask to commit any of your unstaged changes as a checkpoint in a
> new branch it creates. Copilot coding agent will open a draft pull request,
> make changes in the background, and request a review from you.
>
> Copilot will provide a link to the pull request and agent session on GitHub
> once the session begins.

So far, the best cloud agent experience for me has been with [GitHub
Copilot’s agents][4], so a TUI specifically for GitHub Copilot is a
welcome addition.


[1]: https://github.com/features/copilot/cli
[2]: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/use-copilot-cli#delegate-tasks-to-copilot-coding-agent
[3]: https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli#introduction
[4]: https://github.com/features/copilot/agents
