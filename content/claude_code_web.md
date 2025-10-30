---
title: "Impressed With Claude Code Web"
date: 2025-10-29
author: "C. Ross Jam"
status: published
---

It’s early days but I had a really nice initial experience using
[Claude Code Web][1]

> Claude Code on the web runs Claude Code tasks remotely, working with
> code from your GitHub repositories. This article explains how it
> works, when to use it instead of running Claude Code in your
> terminal or IDE, and what workflows it enables. 

[Simon Willison has a post][4] with a much more detailed interaction, but
overall he seems to align with how I felt.

I used it to [modernize][2] an old repo, [lastfm-to-sqlite][3], which
ingests Last.fm scrobbles into an sqlite database. The workflow just
naturally progressed from using Claude Code on the cli. Maybe I went
overboard with the summaries, but I found it extremely helpful
throughout the development process. My hope is that the summaries can
become either archival documentation or rolled into release notes.

As I was working, the integration of Claude Code, on the Web and
command line, with [the GitHub CLI][5] makes for a nice
combination. My next experiment will be to see if I can sketch out
some requirements in a GitHub issue, have Claude Code Web fetch it,
and then churn out a solid PR. Leveraging GitHub issues and PRs as a
system of record for agentic engagement with a codebase might be a
best practice.

Also on my TODO list is giving [Codex][6] on the web a try.


[1]: https://support.claude.com/en/articles/12618689-claude-code-on-the-web
[2]: https://github.com/crossjam/scrobbledb/pull/1
[3]: https://github.com/jacobian/lastfm-to-sqlite
[4]: https://simonwillison.net/2025/Oct/20/claude-code-for-web/
[5]: https://cli.github.com
[6]: https://openai.com/index/introducing-codex/

