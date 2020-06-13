Title: Exactly Once
Date: 2017-07-07 20:40
Author: crossjam
Category: Uncategorized
Slug: exactly-once
Status: published

Confluent [recently announced][1] support for exactly-once processing of messages in the [Apache Kafka messaging framework][2]
> I’m thrilled that we have hit an exciting milestone the Kafka community has long been waiting for: we have  introduced exactly-once semantics in Apache Kafka in the 0.11 release. In this post, I’d like to tell you what exactly-once semantics mean in Apache Kafka, why it is a hard problem, and how the new idempotence and transactions features in Kafka enable correct exactly-once stream processing using Kafka’s Streams API.

Jay Kreps, one of the creators of Kafka, dove deeply [into the technical weeds][3] of how this is achieved:

> There is this claim floating around, and everyone seems quite sure it is true without knowing exactly why, that Exactly Once Delivery/Semantics is mathematically impossible. Yet despite this being apparently common knowledge, you rarely see people linking to some kind of proof of this or even a precise definition of what is meant by exactly-once. They link to other things such as the FLP result or the Two Generals problem as evidence, but nothing about exactly once. In distributed systems you can’t talk about something being possible or impossible without describing precisely what the thing is, as well as describing a setting that controls what is possible (asynchronous, semi-synchronous, etc), and a fault-model that describes what bad things can happen.

> So is there a way we could define formally define a property like what we want to achieve?

> Yes, it turns out that there is just such a property. ...

The key things people need to ask are 1) what are the operational semantic definitions; 2) what are the failure modes; and 3) what are the guarantees under failures. Whenever you’re trying to determine if a distributed system claim is true, read the fine print. Closely.

I haven’t had my toes in the Kafka stream much recently but I’m fascinated by the toolkit’s rise in the developer community. Also, I used to be a bit of a messaging system wonk in my previous job. So this bit of news captivates me.

More to come on this...

[1]: https://www.confluent.io/blog/exactly-once-semantics-are-possible-heres-how-apache-kafka-does-it/
[2]: https://kafka.apache.org/
[3]: https://medium.com/@jaykreps/exactly-once-support-in-apache-kafka-55e1fdd0a35f