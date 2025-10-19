---
title: "More On Prek"
date: 2025-10-18
author: "C. Ross Jam"
status: published
---

From Hugo van Kemenade, [some benchmarking][1] of the performance of
[prek][2] for managing git commit hooks:

> prek is noticeably quicker at installing hooks.

>> ⚡ About 10x faster than pre-commit and uses only a third of disk space.
	This 10x is a comparison of installing hooks using the excellent hyperfine benchmarking tool.

> Here’s my own comparison.

Kemenade doesn’t see 10x but definitely a significant performance
boost. He also provides some handy shell aliases for [pre-commit][3]
and prek.


[1]: https://hugovk.dev/blog/2025/ready-prek-go/
[2]: https://prek.j178.dev
[3]: https://pre-commit.com/
