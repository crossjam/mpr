---
title: "Python Supply Chain Security"
date: 2025-12-24 15:15
author: "C. Ross Jam"
---

[Michael Kennedy][2] does the Python community a service and explains how
to [integrate pip-audit into package development][1] to help secure the
dependency supply chain:

> pip-audit is great because you can just run it on the command
> line. It will check against PyPA’s official list of vulnerabilities
> and tell you if anything in your virtual environment or requirements
> files is known to be malicious.
>
> You could even set up a GitHub Action to do so, and I wouldn’t
> recommend against that at all. But it’s also valuable to make this
> check happen on developers’ machines. It’s a simple two-step process
> to do so ...

Here’s the precis on [pip-audit][3]

> pip-audit is a tool for scanning Python environments for packages
> with known vulnerabilities. It uses the Python Packaging Advisory
> Database (https://github.com/pypa/advisory-database) via the PyPI
> JSON API as a source of vulnerability reports. 

Kennedy illustrates basic installation and usage of pip-audit from the
command line. He also incorporates it into a `pytest`
test. Personally, I think I’d rather add it as a Poe The Poet task and
then roll it into a `qa` meta task. That approach already fits into my
GitHub action workflow.

Also, TIL about `uv`’s [dependency cooldowns][4]:

> Dependency cooldowns
>
> uv also supports dependency "cooldowns" in which resolution will
> ignore packages newer than a duration. This is a good way to improve
> security posture by delaying package updates until the community has
> had the opportunity to vet new versions of packages. 
> 
> This feature is available via the exclude-newer option and shares
> the same semantics. 
> 
> Define a dependency cooldown by specifying a duration instead of an
> absolute value. Either a "friendly" duration (e.g., 24 hours, 1
> week, 30 days) or an ISO 8601 duration (e.g., PT24H, P7D, P30D) can
> be used. 

Even better, this can be specified within a `tool.uv` section of
`pyproject.toml` file.

[1]: https://mkennedy.codes/posts/python-supply-chain-security-made-easy/
[2]: https://mkennedy.codes/
[3]: https://github.com/pypa/pip-audit
[4]: https://docs.astral.sh/uv/concepts/resolution/#dependency-cooldowns

