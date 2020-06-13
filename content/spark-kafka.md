Title: spark-kafka
Date: 2015-01-04 17:36
Author: crossjam
Category: Uncategorized
Slug: spark-kafka
Status: published

You can also [turn a Kafka topic into a Spark RDD][1]
> Spark-kafka is a library that facilitates batch loading data from Kafka into Spark, and from Spark into Kafka.

> This library does not provide a Kafka Input DStream for Spark Streaming. For that please take a look at the spark-streaming-kafka library that is part of Spark itself.

This could come in handy to pre-ingest some data to build up some history before connecting to a [Kafka][2] data stream using [Spark Streaming][3].

[1]: https://github.com/tresata/spark-kafka
[2]: http://kafka.apache.org/
[3]: https://spark.apache.org/streaming/