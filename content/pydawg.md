Title: pyDAWG
Date: 2012-09-24 21:45
Author: crossjam
Category: Uncategorized
Slug: pydawg
Status: published

Okay, [tons of background knowledge][2] is great, until you find yourself having to search 20Gb / 270+ million lines to find anything in that mountain of data.  Full text indexing seems like the right choice, but again, who wants to deal with Solr/Lucene, ElastiSearch, or Sphinx just to get started?

Enter [DAWG][1]
> This package provides DAWG-based dictionary-like read-only objects for Python (2.x and 3.x).

> String data in a DAWG (Directed Acyclic Word Graph) may take 200x less memory than in a standard Python dict or list and the raw lookup speed is comparable. DAWG may be even faster than built-in dict for some operations. It also provides fast advanced methods like prefix search.

> Based on dawgdic C++ library.

I’m going to give it a shot at work and see what happens. The big upside is fast prefix search *(hopefully)* over and above a key/value store’s fast key lookup. Only obvious downside I can see is constantly hearing [Xzibit][3] in my head when I read the docs for this module.

[1]: http://pypi.python.org/pypi/DAWG/0.3.2
[2]: http://crossjam.net/wp/mpr/2012/09/background-knowledge/
[3]: http://knowyourmeme.com/memes/xzibit-yo-dawg