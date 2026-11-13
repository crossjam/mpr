---
title: "Writing With An LLM"
date: 2026-11-12 21:09
author: "C. Ross Jam"
status: published
---

### The Problem

And since I’m getting back into posting, I now need to adjust my
approach a bit. I had been using my homegrown [`copyedit`][copyedit_ai]
cli tool to review posts before publishing. According to Thomas
Ptacek, that’s not _[How To Write With An
LLM][how_to_write_with_an_llm]_. He has two simple rules:

> **Rule Number One: You may not use a single word an LLM suggests to you.**
>
> Breaking this rule is what’s going to get you into trouble. Reason
> being: frontier models are supernaturally good at selecting pleasing
> turns of phrase. It’s sort of their whole thing. The problems with
> what models suggest are subtle. Think of it this way: frontier
> models are wedged in a mode where everything they write is a
> magazine headline. Headlines are good, but you’d wonder about
> someone who wrote an article with dozens of them. 
> 
> ...
>
> **Rule Number Two: Avoid encouragement**
>
> LLMs also infect your writing through influence campaigns. This is a
> much subtler problem, and the damage is less obvious, but it’s still
> a way in which LLMs will make your writing worse, and if that’s
> going to be the outcome, you might as well not enlist LLMs at all.

Over and above [my fanboy attraction][fanboy] to Ptacek’s technical
writing, _How To Write ..._ has a nugget of truth in human sensitivity
to AI writing, "Readers can detect LLM words in the parts per
trillion." So my past approach with `copyedit` is right out.

### What Can Be Done?

Oddly enough the solution might be ... more AI? 

Ptacek built a custom gui application to workshop his writing. The
tool, developed via agentic coding, spots problems in the writing.
Then it’s up to him if and how to integrate the feedback. After he
does that, the tool / agent is asked to judge. Iteration may ensue.

That’s it.

A bit of taste is needed in determining a set of prompts that fits
one’s personal style. Reading his piece for inspiration is left as an
exercise to the reader. In a [follow up][swillison_followup], Simon
Willison (another Internet technical writer I aspire to emulate) has a
concrete [proofing prompt][proofing_prompt] as a good starting point.

Firing your favorite coding harness at an app to do this workshopping
is where the "more AI" comes in.

Fundamentally, this boils down to a maxim I’ve had in my head since
forever. **There is no good writing. Only good rewriting.** Make AI
help with the toil of flagging the issues, but stick it to the human
to do the substantively valuable work of rewriting. 

Now off to sic [pi] on the next version of `copyedit`.


[how_to_write_with_an_llm]: https://sockpuppet.org/blog/2026/09/17/how-to-write-with-an-llm/
[swillison_followup]: https://simonwillison.net/2026/Sep/17/how-to-write-with-an-llm/
[proofing_prompt]: https://simonwillison.net/guides/agentic-engineering-patterns/prompts/#proofreader
[copyedit_ai]: https://github.com/crossjam/copyedit_ai
[fanboy]: {filename}/what_thomas_said.md
[pi]: https://pi.dev

