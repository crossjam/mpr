---
title: "copyedit_ai"
date: 2025-11-12
author: "C. Ross Jam"
status: published
---

Speaking of personal projects, I wandered off on a sidequest to create
my own CLI tool for copyediting my text. The idea is to have something
that can take text in, prompt an LLM to proofread, and ship the result
back. Following UNIX norms, the baseline is to read and write to
standard input and standard output. After that, it’s bells and
whistles.

<!-- PELICAN_END_SUMMARY -->

This one took a slightly odd path but I’ve got something out the door:
[copyedit_ai][2]. Okay, nothing fancy and probably only of use to
me. Here’s how I did it.

- Started off with Claude just to generate a Bash script with this
  prompt
  
  > Use the Python llm cli package from Simon Willison to  create a
  > bash script that reads from standard input or a file and then
  > prompts a model to copyedit the text from stdin. The prompt should
  > be something like ...

- Gave the script a test drive
- Requested a few features, like passing extra arguments
- Felt decent about the script
- Created a new GitHub repo from a [cookiecutter][3] that [aligns][4] with a lot of my
  personal preferences
- Stuffed the script [into the repository][5]
- Prompted Claude Code to take [this plan][6] and generate [an implementation plan][7]
- Pushed the code up to GitHub
- Pointed Claude Code Web at the repo and told it "Make it so!", more or less
- Iterated with Claude Code Web to reach the tool’s current state

I **think** this will turn out quite useful. Even if it doesn’t pan
out, going through the process struck me as just one of many
reasonable ways to approach agentic coding. I sort of like having a
chatbot generate bash as a first draft. Plop it into a container of
guidelines and guardrails. Then let an agent cook.

Speaking of personal utilities, I’m fiending for a simple way to use
[the 1Password CLI][1] or [SDK][8] to grab api key secrets and install
them in the current shell _(ai_key_op?)_. In the age of LLMs, api key
fatigue is real. Maybe a little TUI action as a bonus. Feels like yet
another job for agentic coding.

[1]: https://developer.1password.com/docs/cli/
[2]: https://github.com/crossjam/copyedit_ai
[3]: https://github.com/JnyJny/python-package-cookiecutter
[4]: {filename}/package_cookiecutter.md
[5]: https://github.com/JnyJny/python-package-cookiecutter
[6]: https://github.com/crossjam/copyedit_ai/blob/main/PLANNING.md
[7]: https://github.com/crossjam/copyedit_ai/blob/main/PLAN-2025-11-10.md
[8]: https://developer.1password.com/docs/sdks/
