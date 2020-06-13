Title: NATS Streaming
Date: 2017-11-10 18:35
Author: crossjam
Category: Uncategorized
Slug: nats-streaming
Status: published

Soon I’m going to start a new side project with streaming data. As an [Apache Kafka][1] fan, I love the notion of persistent, append only logs with logical record identifiers. Plus the Confluent folks are doing some interesting work with [Kafka Streams][8] for writing stream processing code. Unfortunately, setting up a single node Kafka server seems really pointless to me, but my project initially won’t be cost effective in an honest-to-gosh distributed Kafka installation.

So I started looking around to see if there was anything similar.

Turns out [Redis][2] will be getting [a streams extension][5], that [looks really promising][6]. Probably won’t be here soon enough for my timeline.

Meanwhile, [NATS][3] has [a streaming server][4] wrapped around the core messaging service that has [many of the same semantics as Kafka][7]. NATS and NATS streaming are really lightweight and easy to deploy. The trade is giving up some of the distribution and reliability guarantees that Kafka provides. That's fine at this point.

Need to do some tire kicking this weekend.

[1]: https://kafka.apache.org/
[2]: https://redis.io/
[3]: https://nats.io/
[4]: https://nats.io/documentation/streaming/nats-streaming-intro/
[5]: http://antirez.com/news/114
[6]: https://brandur.org/redis-streams
[7]: https://github.com/nats-io/nats-streaming-server
[8]: https://kafka.apache.org/documentation/streams/