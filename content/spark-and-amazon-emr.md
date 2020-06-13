Title: Spark and Amazon EMR
Date: 2013-02-28 17:39
Author: crossjam
Category: Uncategorized
Slug: spark-and-amazon-emr
Status: published

Howto on [deploying Spark into Amazon’s elastic environment][1]:
> A common business scenario is the need to store and query large data sets. You can do this by running a data warehouse on a cluster of computers. By distributing the data over many computers, you return results quickly because the computers share the load of processing the query. One limitation on the speed at which queries can be returned, however, is the time it takes to retrieve the data from disk.

> You can increase the speed of queries returned from a data warehouse by using the Shark data warehouse system. Shark runs on top of Spark, an open-source cluster computing system optimized for speed. Spark speeds up data analytics by loading data into memory, providing much faster performance than a disk-based system like Hadoop. For more information on Spark, see http://spark-project.org/.

[1]: http://aws.amazon.com/articles/Elastic-MapReduce/4926593393724923