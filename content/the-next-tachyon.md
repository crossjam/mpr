Title: The Next Tachyon
Date: 2013-04-29 21:58
Author: crossjam
Category: Uncategorized
Slug: the-next-tachyon
Status: published

[!embed](https://twitter.com/bigdata/status/328905487586299905)

[@bigdata goes deeper into Tachyon][1]:
> A release slated for the summer will include features2 that enable data sharing (users will be able to do memory-speed writes to Tachyon). With Tachyon, Spark users will have for the first time, a high throughput way of reliably sharing files with other users. Moreover, despite being an external storage system Tachyon is comparable to Spark’s internal cache. Throughput tests on a cluster showed that Tachyon can read 200x and write 300x faster than HDFS. (Tachyon can read and write 30x faster than FDS’ reported throughput.)

> Similar to the resilient distributed datasets (RDD) fundamental within Spark, fault-tolerance in Tachyon also relies3 on the concept of lineage – logging the transformations used to build a dataset, and using those logs to rebuild datasets when needed. Additionally as an external storage system Tachyon also keeps tracks of binary programs used to generate datasets, and the input datasets required by those programs.

Terabyte scale analytics at interactive speeds. Coming soon to a laptop near you.

[1]: http://strata.oreilly.com/2013/04/tachyon-open-source-distributed-fault-tolerant-in-memory-file-system.html
