---
title: "mdformat"
date: 2025-12-28 19:30
author: "C. Ross Jam"
status: published
---

I’ve created [a handy tool][6] for [copyediting my blog
posts][7]. Unfortunately, the models tend to extend my text into long
lines and don't properly word-wrap.

Enter [mdformat][1]

> Mdformat is an opinionated Markdown formatter that can be used to enforce a consistent
> style in Markdown files. Mdformat is a Unix-style command-line tool as well as a Python
> library.
>
> The features/opinions of the formatter include:
>
> - Consistent indentation and whitespace across the board
> - Always use ATX style headings
> - Move all link references to the bottom of the document (sorted by label)
> - Reformat indented code blocks as fenced code blocks
> - Use 1. as the ordered list marker if possible, also for noninitial list items
>
> Mdformat will not change word wrapping by default. The rationale for this is to support
> Semantic Line Breaks.

These two plugins, [mdformat-footnote][2] and [mdformat-front-matters][3], have been
useful. A long time ago, I picked up the Pandoc footnote style in Markdown. This year, I
started using YAML front matter to align with my use of Quarto on another blog.

I actually started [implementing this feature][4] by hand without
assistance from an agentic coder. Then I asked [GitHub Copilot][5] to
review the PR. It found a few issues, including a couple of clear
brainos by the human, and made some suggestions that were easy to
adopt. The two of us delivered a better product.

GitHub Copilot feels like a vastly underappreciated entry into the agentic coding space.

_P. S. This post was copyedited with my own copyediting tool._

[1]: https://mdformat.readthedocs.io/en/stable/
[2]: https://github.com/executablebooks/mdformat-footnote
[3]: https://github.com/KyleKing/mdformat-front-matters
[4]: https://github.com/crossjam/copyedit_ai/pull/56
[5]: https://github.com/features/copilot
[6]: https://github.com/crossjam/copyedit_ai
[7]: %7Bfilename%7D/copyedit_ai.md
