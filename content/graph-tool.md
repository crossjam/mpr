Title: graph-tool
Date: 2012-12-09 21:50
Author: crossjam
Category: Uncategorized
Slug: graph-tool
Status: published

Link parkin’: [graph-tool][1]
> graph-tool is an efficient python module for manipulation and statistical analysis of graphs (a.k.a. networks). Contrary to most other python modules with similar functionality, the core data structures and algorithms are implemented in C++, making extensive use of template metaprogramming, based heavily on the Boost Graph Library. This confers a level of performance which is comparable (both in memory usage and computation time) to that of a pure C/C++ library.

The [Boost Graph Library][2] gives me the willies though. I’ve never had much luck building or using it embedded within Python. Weird linking or dynamic library  loading issues got me. At a 2.x release though, this module might be worth a test drive.

Via [@hmason](https://twitter.com/hmason)
[!embed](https://twitter.com/hmason/status/277458758127452160)

[1]: http://projects.skewed.de/graph-tool/
[2]: http://www.boost.org/libs/graph/