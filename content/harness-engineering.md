---
title: Harness Engineering
date: 2026-02-19 20:15
author: C. Ross Jam
status: published
---

[Previously][hashimoto-ai-adoption], I had picked up on Mitchell Hashimoto using
the phrase "harness engineering". That term might be catching on.

Quoting [OpenAI’s recent post][openai-harness-engineering], entitled _"Harness
engineering: leveraging Codex in an agent-first world"_:

> Over the past five months, our team has been running an experiment: building
> and shipping an internal beta of a software product with 0 lines of
> manually-written code.
>
> The product has internal daily users and external alpha testers. It ships,
> deploys, breaks, and gets fixed. What’s different is that every line of
> code—application logic, tests, CI configuration, documentation, observability,
> and internal tooling—has been written by Codex. We estimate that we built this
> in about 1/10th the time it would have taken to write the code by hand.

Birgitta Böckeler, a Distinguished Engineer at Thoughtworks, follows
up further [on the impacts of harness
engineering][fowler-harness-engineering].

> It was very interesting to read OpenAI’s recent write-up on “Harness
> engineering” which describes how a team used “no manually typed code at all”
> as a forcing function to build a harness for maintaining a large application
> with AI agents. After 5 months, they’ve built a real product that’s now over 1
> million lines of code.
>
> The article is titled “Harness engineering: leveraging Codex in an agent-first
> world”, but only mentions “harness” once in the text. Maybe the term was an
> afterthought inspired by Mitchell Hashimoto’s recent blog post. Either way, I
> like “harness” as a word to describe the tooling and practices we can use to
> keep AI agents in check.
>
> The OpenAI team’s harness components mix deterministic and LLM-based
> approaches across 3 categories (grouping based on my interpretation):
>
> 1. Context engineering: Continuously enhanced knowledge base in the codebase,
>    plus agent access to dynamic context like observability data and browser
>    navigation
> 1. Architectural constraints: Monitored not only by the LLM-based agents, but
>    also deterministic custom linters and structural tests
> 1. “Garbage collection”: Agents that run periodically to find inconsistencies
>    in documentation or violations of architectural constraints, fighting
>    entropy and decay

Working from an assumption that OpenAI is engaged in good-faith reporting on the
final app, which is currently an internal beta, Böckeler draws some implications
for production software development. Will harnesses become the new service
templates? Does the AI need **more constraints** on its autonomy, not fewer
guardrails, to deliver robust software? Is it even possible to apply this
approach to pre-AI codebases?

She closes out with:

> And finally, for once, I like a term in this space. Though it’s only 2 weeks
> old — I can probably hold my metaphorical breath until somebody calls their
> one-prompt, LLM-based code review agent a harness…

Personally, I had been thinking of "the harness" from the perspective
of an individual developer. What’s the GUI-based IDE, or TUI that they
use on a daily basis to interact with a codebase and drive agentic
coding? What are its affordances, and what constraints does it place
on a model's code generation?

Zooming out a bit to the project or organizational level makes a lot of sense,
though. As described by OpenAI, that’s not a single system or tool but a set of
processes they discovered on the fly for this effort. With repetition, patterns
will emerge, become codified, and eventually reified into new software tools.
Then you could have a nice intersection between the project’s harness and a
developer’s harness. Sort of like how git is a narrow waist that joins CI/CD
approaches and developer environments, based upon a particular perspective on
source code version control.

Hold on to your knickers! Prepare for turbulence.

[fowler-harness-engineering]: https://martinfowler.com/articles/exploring-gen-ai/harness-engineering.html
[hashimoto-ai-adoption]: %7Bfilename%7D/hashimoto-ai-journey.md
[openai-harness-engineering]: https://openai.com/index/harness-engineering/
