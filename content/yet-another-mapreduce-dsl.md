Title: Yet Another MapReduce DSL
Date: 2014-02-02 17:41
Author: crossjam
Category: Uncategorized
Slug: yet-another-mapreduce-dsl
Status: published

[Apache Crunch][2] has been around for a while, but the recent addition for support of [Apache Spark][1] and a Scala REPL caught my eye:
> Running on top of Hadoop MapReduce and Apache Spark, the Apache Crunch™ library is a simple Java API for tasks like joining and data aggregation that are tedious to implement on plain MapReduce. The APIs are especially useful when processing data that does not fit naturally into relational model, such as time series, serialized object formats like protocol buffers or Avro records, and HBase rows and columns. For Scala users, there is the Scrunch API, which is built on top of the Java APIs and includes a REPL (read-eval-print loop) for creating MapReduce pipelines.

[1]: http://spark.incubator.apache.org/
[2]: http://crunch.apache.org/index.html