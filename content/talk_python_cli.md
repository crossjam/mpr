---
title: Talk Python CLI
date: 2026-02-20 22:45
author: C. Ross Jam
status: published
---

Link parkin’: [Talk Python has a CLI][talk-python-cli]

Michael Kennedy introduces the tool in
[a recent blog post][talk-python-cli-post]:

> **TL;DR:** Talk Python now has an open-source CLI tool (talk-python-cli) that
> lets you search 500+ podcast episodes, transcripts, guests, and training
> courses directly from your terminal. Install it with
> `uv tool install talk-python-cli`. It supports text, JSON, and markdown
> output: built for humans, scripts, and AI/LLMs alike.
>
> ...
>
> ## Why build a CLI tool?
>
> I believe Talk Python becomes more valuable as it is used and referenced more
> by the community. The CLI tool closes an important gap. Here are just some
> examples:
>
> 1. **Terminal-first developers:** “I live in my terminal, don’t make me open a
>    browser to find that episode about FastAPI”
> 1. **Automation / scripting folks:** “I want to pipe podcast data into my
>    workflows and script it”
> 1. **AI / LLM builders:** “I need real, high-quality Python community content
>    for my RAG pipeline or podcast assistant”
> 1. **LLM Chat without MCP:** “The MCP server solves the rapid access to live
>    data challenge for AIs that support MCP **and** whose users has installed
>    it. But many LLMs don’t support MCP. I’m looking at you ChatGPT.”

I’m primarily looking at this as design inspiration for
[retrocast]. As in identifying some basic, essential concepts and
operations that make sense for searching a podcast episode repository.

[retrocast]: https://github.com/crossjam/retrocast
[talk-python-cli]: https://github.com/talkpython/talk-python-cli
[talk-python-cli-post]: https://talkpython.fm/blog/posts/talk-python-now-has-a-cli/
