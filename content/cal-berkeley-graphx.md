Title: Cal Berkeley GraphX
Date: 2013-05-20 20:14
Author: crossjam
Category: Uncategorized
Slug: cal-berkeley-graphx
Status: published

C’mon Bears, cut it out. It’s getting embarrassing how much Spark related output there has been recently. In a good way!
> From social networks to targeted advertising, big graphs capture the structure in data and are central to recent advances in machine learning and data mining. Unfortunately, directly applying existing data-parallel tools to graph computation tasks can be cumbersome and inefficient. The need for intuitive, scalable tools for graph computation has lead to the development of new graph-parallel systems (e.g. Pregel, PowerGraph) which are designed to efficiently execute graph algorithms. Unfortunately, these new graph-parallel systems do not address the challenges of graph construction and transformation which are often just as problematic as the subsequent computation. Furthermore, existing graph-parallel systems provide limited fault-tolerance and support for interactive data mining.

> We introduce GraphX, which combines the advantages of both data-parallel and graph-parallel systems by efficiently expressing graph computation within the Spark data-parallel framework. We leverage new ideas in distributed graph representation to efficiently distribute graphs as tabular data-structures. Similarly, we leverage advances in data-flow systems to exploit in-memory computation and fault-tolerance. We provide powerful new operations to simplify graph construction and transformation. Using these primitives we implement the PowerGraph and Pregel abstractions in less than 20 lines of code. Finally, by exploiting the Scala foundation of Spark, we enable users to interactively load, transform, and compute on massive graphs.

Need to drill in to see how [GraphX][1] stacks up to the current spate of “big data” graph toolkits, especially GraphLab. [Ben Lorica reports][2] that GraphX is more oriented towards to programmer productivity as opposed to raw performance:
> GraphX is a new, fault-tolerant, framework that runs within Spark. Its core data structure is an immutable graph5 (Resilient Distributed Graph – or RDG), and GraphX programs are a sequence of transformations on RDG’s (with each transformation yielding a new RDG). Transformations on RDG’s can affect nodes, edges, or both (depending on the state of neighboring edges and nodes). GraphX greatly enhances productivity by simplifying a range of tasks (graph loading, construction, transformation, and computations). But it does so at the expense of performance: early prototype algorithms written in GraphX were slower than those written in GraphLab/PowerGraph.

[1]: https://amplab.cs.berkeley.edu/publication/graphx-grades/
[2]: http://strata.oreilly.com/2013/05/improving-options-for-unlocking-your-graph-data.html