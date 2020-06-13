Title: Armbrust on Spark Structured Streaming
Date: 2016-05-26 23:01
Author: crossjam
Category: Uncategorized
Slug: armbrust-on-spark-structured-streaming
Status: published

I enjoyed this [O’Reilly Data Podcast conversation][1] with Michael Armbrust regarding Apache Spark 2.0’s Structured Streaming:
> With the release of Spark version 2.0, streaming starts becoming much more accessible to users. By adopting a continuous processing model (on an infinite table), the developers of Spark have enabled users of its SQL or DataFrame APIs to extend their analytic capabilities to unbounded streams.

> Within the Spark community, Databricks Engineer, Michael Armbrust is well-known for having led the long-term project to move Spark’s interactive analytics engine from Shark to Spark SQL. (Full disclosure: I’m an advisor to Databricks.) Most recently he has turned his efforts to helping introduce a much simpler stream processing model to Spark Streaming (“structured streaming”).

You’ll need a login, but there’s also [a deeper dive video][2] from  Armbrust and Tathagata Das going into more details of Structured Streaming.

At one point, Ben Lorica asked Armbrust about the dimensions upon which developers should evaluate streaming platforms. The obvious ones (delivery guarantees, latency, throughput) were brought up. I’d add a few more

* **expressiveness**, how convenient is it to express common streaming computations and how possible is it to implement exquisite solutions
* **agility**, the ease with which stream processing code can be correctly updated and re-deployed
* **monitoring**, getting useful performance metrics and debugging information out of the system

Apache Spark Structured Streaming, [Kafka Streams][3], [Twitter Heron][5],[ Apache Flink][4]. So much to choose from.

[1]: https://www.oreilly.com/ideas/structured-streaming-comes-to-apache-spark-2-0
[2]: https://www.oreilly.com/learning/apache-spark-2-0--introduction-to-structured-streaming
[3]: http://www.confluent.io/blog/introducing-kafka-streams-stream-processing-made-simple
[4]: http://flink.apache.org/
[5]: http://heronstreaming.io/