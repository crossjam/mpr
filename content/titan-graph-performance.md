Title: Titan Graph Performance
Date: 2012-08-08 08:07
Author: crossjam
Category: Uncategorized
Slug: titan-graph-performance
Status: published

I've [mentioned][2] the Titan graph store before. [Aurelius](http://thinkaurelius.com/), the company building Titan, has posted [a performance study][1] of the DB that heavily relied on Amazon Web Services:
> The presentation to follow discusses the simulation’s social graph structure, the types of processes executed on that structure, and the various runtime analyses of those processes under normal and peak load. The presentation concludes with a discussion of the Amazon EC2 cluster architecture used and the associated costs of running that architecture in a production environment. In short summary, Titan performs well under substantial load with a relatively inexpensive cluster and as such, is capable of backing online services requiring real-time Big Graph Data.

The kicker is that their analysis of one year’s AWS costs to support a half-million users is well within an early startup’s wheelhouse. Also, their modeling and sim approach is pretty interesting. They’ve probably simplified the discussion approach for presentation, but there’s a bunch of approaches in the CS literature that are also applicable.

[1]: http://thinkaurelius.com/2012/08/06/titan-provides-real-time-big-graph-data/
[2]: http://crossjam.net/wp/mpr/2012/06/titan-graph-store/