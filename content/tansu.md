---
title: Tansu
date: 2026-01-25 23:15
author: C. Ross Jam
---

Link parkin’: [Tansu][tansu]

> ### Diskless Kafka on top of PostgreSQL, S3 or SQLite
>
> Tansu is an Open Source, Apache Kafka®-compatible messaging
> broker. Super simple. Single binary. Built-in schema validation,
> open table format support (Iceberg, Delta). Built to be stateless
> and easy to use with plug-and-play storage. 

I’ve been interested in messaging systems, especially [Apache
Kafka][apache-kafka], since Kafka was first announced to the world by
Jay Kreps in a blog post called ["The Log: ..."][kreps-the-log]. _Has
it really been 12 years?_ Haven’t needed to use Kakfa over the past
two to three years, but my ears always perk up when I hear of a new
entrant into the messaging space.

[Redpanda][redpanda] has been around for a while as a low operations
version of Kafka. [AutoMQ][automq] has existed for a bit as Kafka on
S3.

Tansu, according to its [docs][tansu-docs], would appear to be a bit
of a generalization in both directions:

> Tansu is a drop-in replacement for Apache Kafka with PostgreSQL,
> SQLite, S3 or memory storage engines. Without the cost of broker
> replicated storage for durability. Licensed under the Apache
> License. Written in 100% safe 🦺 async 🚀 Rust 🦀.
>
> ...
>
> Similarly, support for the Apache Iceberg or Delta Lake open table
> formats can be enabled ...

A [validating schema registry][tansu-registry] is also baked in. At
least when I last engaged with the Kafka ecosystem, this component was
an add on maintained by Confluent.

Something to explore.


[tansu]: https://tansu.io/
[apache-kafka]: https://kafka.apache.org/
[kreps-the-log]: https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying
[redpanda]: https://redpanda.com
[automq]: https://automq.com/
[tansu-docs]: https://docs.tansu.io/
[confluent]: https://confluent.io/
[tansu-registry]: https://docs.tansu.io/docs/schema-registry
