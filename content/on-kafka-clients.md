Title: On Kafka Clients
Date: 2017-08-24 21:10
Author: crossjam
Category: Uncategorized
Slug: on-kafka-clients
Status: published

Link parkin’: [*A Tale of Two Kafka Clients*][1]

> We use and love Kafka at Data Syndrome. It enables us to move processing from batch to realtime with minimal pain and complexity. However, during a recent project we learned a hard lesson about the kafka-python package that has me thinking about how to make the choice between open source tools. In this post we reflect on the open source decision making process. We describe two Kafka clients for Python, the issues we encountered, and the solution we’ll be using going forward.

Slightly disappointed that there wasn’t mention of [pykafka][2], which is not Confluent controlled but still pretty robust.

[1]: https://blog.datasyndrome.com/a-tale-of-two-kafka-clients-c613efab49df
[2]: https://github.com/Parsely/pykafka