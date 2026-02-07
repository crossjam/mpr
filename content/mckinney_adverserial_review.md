---
title: McKinney on Adversarial Review
date: 2026-02-06 22:15
author: C. Ross Jam
status: published
---

Something I haven’t been doing well on my agentic coding projects is
close code review. I'm not quite YOLO vibe coding as I do look at the
code typically.  But I don’t go over it with a fine-tooth comb
applying proper software-development practices.

And I really need to do a better job making sure the tests don’t suck.

On a [recent episode][podcast-episode] of Hugo Bowne-Anderson’s excellent
[Vanishing Gradients podcast][vanishing-gradients-podcast],
[Wes McKinney][wes-mckinney] confirmed a practice that’s been on my TODO list to
put in place: _"adversarial code review"_

> And so what I discovered almost haphazardly, which is the solution to the
> problem, is that you need to have your agents adversarially reviewed. Like all
> of their output needs to be reviewed adversarially, ideally by other models.
> So not having Claude review Claude's output. have Codex and Gemini review
> Claude's output. So every time my Claude code sessions do anything,they commit
> and the commit is immediately reviewed by either Codex or Gemini or both. And
> I feed that output back into my cloud code session. Be like, I see what you
> did there, but you're not getting this past me. You're going to fix all these
> bugs. And so I'm not reading the code anymore,but the code is being read
> aggressively by a lot of agents. And by the time I'm putting up a pull request
> on GitHub now, on RoboRev, for example, like my code review system, Typically,
> there's been 20 or 30 review passes that have taken place if it's a complex
> feature

Apologies for the wall of text on that quote. It was taken directly from the
podcast transcript.

McKinney also had a spicy take on Python usage:

> It’s the agent writing the code. And it’s the development loop of writing the
> code, building testing, write the code, build test and iterating. And so I do
> think we’ll see for many types of software, a shift away from Python towards
> other programming languages. I think Go is probably the best language for
> those like other types of software projects. And like I said, I haven’t
> written a line of Go code in my life.

Now Bowne-Anderson is engaging in a bit of selective, promotional
quoting. In full context, McKinney asserted that there will be an
order-of-magnitude more software written and a lot of agents writing
that code. Similar to [my language observation][typed-languages] on
some Matthew Rocklin content, statically typed languages help agents
succeed. To me, this doesn't mean less Python because of
Go/Rust/TypeScript. It means more code overall: Python created by
humans, augmented by Go/Rust/TypeScript from agents.

[podcast-episode]: https://hugobowne.substack.com/p/python-is-dead-long-live-python-with
[typed-languages]: {filename}/nodding-my-head.md
[vanishing-gradients-podcast]: https://hugobowne.substack.com/podcast
[wes-mckinney]: https://wesmckinney.com
