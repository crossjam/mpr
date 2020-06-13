Title: Diggin’ On Whoosh
Date: 2012-09-22 17:00
Author: crossjam
Category: Uncategorized
Slug: diggin-on-whoosh
Status: published

I’m starting to observe that when dealing in data exploration, right after summary statistics, keyword style searching is high up on the TODO list. Until you really need them though, pulling out the big boys like Solr/Lucene or Sphinx are sort of a pain. When you’re in iterative exploration mode the tax of dealing with enterprise scalable software is substantial. YAGNI probably applies. However, if you’re of a Pythonic mind the [Whoosh][1] is a nice, lightweight starter toolkit.

> Whoosh is a fast, featureful full-text indexing and searching library implemented in pure Python. Programmers can use it to easily add search functionality to their applications and websites. Every part of how Whoosh works can be extended or replaced to meet your needs exactly.

I've been incorporating Whoosh into some data analysis on a tiny data set and it’s been a blast. So much so I’ll soon try it out on a bigger, but not massive, pile of bits. A nice feature of a pure Pythonic search library is that you can stash arbitrary Python data structures in the index. This really increases the utility of dealing with search results as opposed to having to go to another store to retrieve more complex non-indexed objects.

Whoosh is also useful for embedding in Swiss Army command shells built using [cliff][2].

[1]: https://bitbucket.org/mchaput/whoosh/wiki/Home
[2]: https://github.com/dreamhost/cliff