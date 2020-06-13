Title: NetflixGraph
Date: 2013-03-09 13:43
Author: crossjam
Category: Uncategorized
Slug: netflixgraph
Status: published

Interesting. If you have relatively small and relatively static graph data, you can easily ship it around a distributed processing platform thanks to [NetflixGraph][1]
> NetflixGraph is a compact in-memory data structure used to represent directed graph data. You can use NetflixGraph to vastly reduce the size of your application’s memory footprint, potentially by an order of magnitude or more. If your application is I/O bound, you may be able to remove that bottleneck by holding your entire dataset in RAM. This may be possible with NetflixGraph; you’ll likely be very surprised by how little memory is actually required to represent your data.

> NetflixGraph provides an API to translate your data into a graph format, compress that data in memory, then serialize the compressed in-memory representation of the data so that it may be easily transported across your infrastructure.

[1]: https://github.com/Netflix/netflix-graph/wiki