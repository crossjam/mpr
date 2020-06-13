Title: Big Dicts
Date: 2012-04-30 21:04
Author: crossjam
Category: Uncategorized
Slug: big-dicts
Status: published

[*atbr*][1] seems like an interesting approach to **really** large scale in memory key/value store, otherwise known as dictionaries, or dicts, in Python.
> *…atbr is basically a thin swig-wrapper around Google’s (memory efficient) opensource sparsehash (written in C++). Atbr also supports relatively efficient loading of tsv key value files (tab separated files) since loading mapreduce output data quickly is one of our main use cases.*

While the authors seem a little more focused on Hadoop integration, I’ve got another interesting use case. [NetworkX][2] is a well developed Python module for graph representation, manipulation, and algorithms. The module uses Python’s built-in  dicts as the primary data structure to represent these graphs. In my experience, NetworkX tends to fall over a bit with big graphs. Maybe using atbr as a replacement underneath NetworkX would improve both memory usage and execution speed. *Yet another personal hacking project I could adopt.*

Also of interest was some of [the benchmarking that inspired atbr][4] and demonstrated that [Python dicts are actually pretty decent][3].

[1]: http://atbrox.com/2012/04/25/atbr-large-scale-in-memory-hashtables-in-python/
[2]: http://networkx.lanl.gov/
[3]: http://incise.org/hash-table-benchmarks.html
[4]: http://blog.aggregateknowledge.com/2011/11/27/big-memory-part-3-5-google-sparsehash/