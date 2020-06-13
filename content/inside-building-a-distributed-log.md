Title: Inside Building a Distributed Log
Date: 2017-12-22 14:44
Author: crossjam
Category: Uncategorized
Slug: inside-building-a-distributed-log
Status: published

[Tyler Treat][4] is publishing [a deep dive series][1] on how to implement distributed log infrastructure:
> In this series, we’re not going to spend much time discussing why the log is useful. Jay Kreps has already done the legwork on that with [*The Log: What every software engineer should know about real-time data’s unifying abstraction*][2]. There’s even a book on it. Instead, we will focus on what it takes to build something like this using Kafka and NATS Streaming as case studies of sorts—Kafka because of its ubiquity, NATS Streaming because it’s something with which I have personal experience. We’ll look at a few core components like leader election, data replication, log persistence, and message delivery. Part one of this series starts with the storage mechanics. Along the way, we will also discuss some lessons learned while building NATS Streaming, which is a streaming data layer on top of the [NATS][3] messaging system. The intended outcome of this series is threefold: to learn a bit about the internals of a log abstraction, to learn how it can achieve the three goals described above, and to learn some applied distributed systems theory.

Looking forward to more in this sequence.

[1]: http://bravenewgeek.com/building-a-distributed-log-from-scratch-part-1-storage-mechanics/
[2]: https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying
[3]: https://nats.io/
[4]: https://bravenewgeek.com/