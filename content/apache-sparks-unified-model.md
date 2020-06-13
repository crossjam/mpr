Title: Apache Spark’s Unified Model
Date: 2014-09-02 21:59
Author: crossjam
Category: Uncategorized
Slug: apache-sparks-unified-model
Status: published

I’ve been [a fan][5] of [Apache Spark][1] *(Go Bears!)* for a while despite not having a real good opportunity to put the toolkit to practical use. Last year I got to [AMPCamp 3][2] and [the first Spark Summit][3]. At the latter event, The AMPLab started singing a new tune about the benefits of a unified model for big data processing, moving on from selling in-memory computing. 

Cloudera’s [Gwen Shapira posted][4] a good case study of the upside:
> But the biggest advantage Spark gave us in this case was Spark Streaming, which allowed us to re-use the same aggregates we wrote for our batch application on a real-time data stream. We didn’t need to re-implement the business logic, nor test and maintain a second code base. As a result, we could rapidly deploy a real-time component in the limited time left — and impress not just the users but also the developers and their management.


[1]: https://spark.apache.org/
[2]: http://ampcamp.berkeley.edu/3/
[3]: http://spark-summit.org/2013
[4]: http://blog.cloudera.com/blog/2014/08/building-lambda-architecture-with-spark-streaming/
[5]: http://crossjam.net/wp/mpr/2012/07/streaming-spark/