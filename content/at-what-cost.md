Title: At What COST?
Date: 2015-01-20 07:21
Author: crossjam
Category: Uncategorized
Slug: at-what-cost
Status: published

Frank McSherry [published a useful reminder][1] that one must carefully calibrate the need to deploy “big data” solutions:
> Lots of people struggle with the complexities of getting big data systems up and running, when they possibly shouldn’t be using the systems in the first place. The data sets above are certainly not small (billions of edges), but still run just fine on a laptop. Much faster than the distributed systems, at least.

> Here are two helpful guidelines (for largely disjoint populations):

> 1. If you are going to use a big data system for yourself, see if it is faster than your laptop.
> 2. If you are going to build a big data system for others, see that it is faster than my laptop.

This brings back memories of the [CMU work on GraphChi][2], where the processed graphs with billions of edges on a Mac Mini. 

I’ll have to dig up Frank’s paper once it gets published.

[1]: http://www.frankmcsherry.org/graph/scalability/cost/2015/01/15/COST.html
[2]: https://www.usenix.org/conference/osdi12/technical-sessions/presentation/kyrola