---
title: "copyedit: Update"
date: 2025-12-09 21:45
author: "C. Ross Jam"
status: published
---

[copyedit][1] is just [a personal tool][5], built with agentic coding,
in the spirit of Simon Willison. It prompts an LLM to copyedit
text. At first, I wasn’t sure how well it would work, but I’ve been
using it to clean up posts here for a while now. It actually works quite
well.

There’s likely a plethora of ways to solve this problem
(_e.g. [vale][3]_), but I’ve had fun putting this together.

In building it I’ve learned a few things:

- The utility of hijacking a CLI module like Willison’s [llm][2] has
  been immense. There’s a lot of underlying plumbing that comes in
  handy. At the same time, llm hasn’t clicked as a Python package for
  me.
- With a bit of prompting, LLMs are pretty good at keeping my general
  style, but there are a few mannerisms I’m going to need to add to the
  system prompt, for example leaving off leading 'Is' and 'Its' on
  fragments.
- Annoyingly, LLMs don’t seem to comprehend word wrapping, although I
  should actually test that out. It feels a bit heavyweight to apply AI
  to that task, so I should probably apply a word-wrapping
  post-processing step.


Speaking of [vale][3]:

> Vale is an open-source, command-line tool that brings your editorial
> style guide to life. 

And looks like there’s [a good book from Pragmatic Programmers][4]:

> **Write Better with Vale**
>
> Automate Your Style Guides and Lint Prose Like You Lint Code
>
> by Brian P. Hogan
>
> Create consistent content that gives readers confidence with Vale,
> the open-source prose linter that helps you enforce your style guide
> automatically. Use battle-tested rules based on freely available,
> popular style guides, apply your brand’s terms with a custom
> vocabulary, and integrate Vale into your text editor, Git hooks, and
> CI pipeline. Catch typos and inclusive-language issues before they
> ship, and spend your energy on shaping ideas instead of fixing
> copy. Whether you’re a technical writer working in a docs-as-code
> environment, or a software engineer who occasionally writes, you’ll
> ship clean, consistent copy every time. 


[1]: https://github.com/crossjam/copyedit_ai
[2]: https://llm.datasette.io/
[3]: https://vale.sh
[4]: https://pragprog.com/titles/bhvale/write-better-with-vale/
[5]: {filename}/copyedit_ai.md



