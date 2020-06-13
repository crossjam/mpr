Title: Apache Spark 0.9.0
Date: 2014-02-03 23:12
Author: crossjam
Category: Uncategorized
Slug: apache-spark-0-9-0
Status: published

Good to see [a release of Apache Spark][1] with [GraphX][2] included, even if the graph package is only in alpha:
> We are happy to announce the availability of Spark 0.9.0! Spark 0.9.0 is a major release and Spark’s largest release ever, with contributions from 83 developers. This release expands Spark’s standard libraries, introducing a new graph computation package (GraphX) and adding several new features to the machine learning and stream-processing packages. It also makes major improvements to the core engine, including external aggregations, a simplified H/A mode for long lived applications, and hardened YARN support.

Spark is an open source project on the move. Previously, in-memory distributed computation was the big selling point. Now it’s unification of disparate computational models cleanly embedded within the Hadoop ecosystem.

[1]: http://spark.incubator.apache.org/news/spark-0-9-0-released.html
[2]: http://amplab.github.io/graphx/