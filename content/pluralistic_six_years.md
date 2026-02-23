---
title: Six Years of Pluralistic
date: 2026-02-22 20:00
author: C. Ross Jam
status: published
---

Cory Doctorow’s [Pluralistic had its sixth birthday][pluralistic-six-years] last
week! 💥 🎉 🎂

> Six years ago today, after 19 years with Boing Boing, during which time I
> wrote tens of thousands of blog posts, I started a new, solo blog, with the
> semi-ironic name "Pluralistic." I didn't know what Pluralistic was going to
> be, but I wasn't writing Boing Boing anymore, and I knew I wanted to keep
> writing the web in some fashion.
>
> Six years and more than 1,500 posts later, I am so satisfied with how
> Pluralistic is going. I spent a couple of decades processing everything that
> seemed interesting or significant through a blog, which created a massive
> database (and mnemonically available collection of partially developed
> thoughts) that I'm now reprocessing as a series of essays that make sense of
> today in light of everything that I've thought about for my whole adult life,
> which are, in turn, fodder for books, both fiction and nonfiction. I call this
> "The Memex Method":

Looks like [I first discovered Pluralistic][pluralistic-discovery] back in
January 2022. So not a super-early adopter, but I’ve been on board longer than
the half-life.

The first segment of his post focuses on what he gets out of the hard graft
needed to create Pluralistic on a mostly daily basis, both personally and
professionally.

> Making Pluralistic is several kinds of hard work. Over the past six years,
> I've become an ardent collagist, spending more and more time on the weird,
> semi-grotesque images that run atop every edition. Anything you devote
> substantial time to on a near-daily basis is something that gives you insight
> – into yourself, and into the thing you're doing.

Off and on, I’ve been a daily blogger over the years. I even pulled off
[a posting run of 540 days in a row][540-streak]. I can heartily agree with this
sentiment.

A third segment of his post, after documenting publishing tooling in the middle,
is an extended screed about AI, its hazards, and its opportunities. Taken as a
whole, this part could be a bit overcooked. I was amused that he uses AI in a
similar way to me: copy editing.

> There is one technology that has made my POSSE life better, and it might
> surprise you. This year, I installed Ollama – an open-source LLM – on my
> laptop. It runs pretty well, even without a GPU. Every day, before I run
> Loren's python publication scripts, I run the text through Ollama as a
> typo-catcher (my prompt is "find typos"). Ollama always spots three or four of
> these, usually stuff like missing punctuation, or forgotten words, or double
> words ("the the next thing") or typos that are still valid words ("of top of
> everything else").

Instead of going fully local with Ollama, though,
[my homegrown copyedit tool][copyedit] calls out to a frontier model API.
Invoking a local model is just a bit of reconfiguration away, so it would
probably be a good experiment to try an open-source one for a while. I’m just a
little too lazy to set up and keep running the local inference server, though.

In any event, cheers to Pluralistic and here’s hoping it’s around for many more
years.

_Hint: If you’re into Pluralistic, Doctorow operates a [Discourse], not
[Discord](https://discord.com), forum at [chinwag.pluralistic.net][chinwag].
Fully [open source][discourse-github], ’natch. Low volume, high signal._

[540-streak]: %7Bfilename%7D/540.md
[chinwag]: https://chinwag.pluralistic.net
[copyedit]: https://github.com/crossjam/copyedit_ai
[discourse]: https://www.discourse.org/
[discourse-github]: https://github.com/discourse/discourse
[pluralistic-discovery]: %7Bfilename%7D/doctorow_pluralist.md
[pluralistic-six-years]: https://pluralistic.net/2026/02/19/now-we-are-six/
