Title: Are GraphDBs Needed?
Date: 2017-07-22 22:05
Author: crossjam
Category: Uncategorized
Slug: are-graphdbs-needed
Status: published

[Adrian Colyer summarizes][1] an [academic paper][2] that gets into that question, or more accurately benchmarks a few graphdbs on a representative workload:

> If you want to say “my database is better than your database” then you really also need to specify “for what?”. And if you want to evaluate whether graph databases really do earn their keep as compared to relational databases, you really want to do the comparison on the home turf of the graph databases – the use cases they claim to be good at.

The final outcome is that traditional RDBMS engines, using straight SQL instead of a specialized graph query language, have much better performance. [Gremlin][3] takes it on the chin a bit.

Other stores I’d be interested to see benchmarked include: [BlazeGraph][4], [OrientDB][5], [Weaver][6] *(dead?)*, [ArangoDB][8], and [AgensGraph][7].

[1]: https://blog.acolyer.org/2017/07/07/do-we-need-specialized-graph-databases-benchmarking-real-time-social-networking-applications/
[2]: https://event.cwi.nl/grades/2017/12-Apaci.pdf
[3]: https://tinkerpop.apache.org/gremlin.html
[4]: https://www.blazegraph.com/
[5]: http://orientdb.com/
[6]: http://weaver.systems/
[7]: http://www.agensgraph.com/
[8]: https://www.arangodb.com/