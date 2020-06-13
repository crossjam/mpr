Title: Streaming Spark
Date: 2012-07-06 20:23
Author: crossjam
Category: Uncategorized
Slug: streaming-spark
Status: published

Cool! Scalable streamed data processing on top of Hadoop-like infrastructure, via [*Discretized Streams (PDF)*][1]
>  The key idea behind D-Streams is to treat a streaming computation as a series of deterministic batch computations on small time intervals. For example, we might place the data received each second into a new interval, and run a MapReduce operation on each interval to compute a count. Similarly, we can perform a running count over several intervals by adding the new counts from each interval to the old result. Two immediate advantages of the D-Stream model are that consistency is well-defined (each record is processed atomically with the interval in which it arrives), and that the processing model is easy to unify with batch systems. In addition, as we shall show, we can use similar recovery mechanisms to batch systems, albeit at a much smaller timescale, to mitigate failures more efficiently than existing streaming systems, i.e., recover data faster at a lower cost

That’s how the Cal CS Division rolls.

[Via Ben Lorica][2]

[1]: http://www.cs.berkeley.edu/~matei/papers/2012/hotcloud_spark_streaming.pdf
[2]: https://mobile.twitter.com/#!/bigdata/status/215859206631333888