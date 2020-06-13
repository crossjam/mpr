Title: Reconciling Streaming Jargon
Date: 2015-02-01 18:16
Author: crossjam
Category: Uncategorized
Slug: reconciling-streaming-jargon
Status: published

I really enjoyed reading [Martin Kleppmann’s treatise][1] on varying communities and terminology related to stream processing:
> Some people call it stream processing. Others call it Event Sourcing or CQRS. Some even call it Complex Event Processing. Sometimes, such self-important buzzwords are just smoke and mirrors, invented by companies who want to sell you stuff. But sometimes, they contain a kernel of wisdom which can really help us design better systems.

> In this talk, we will go in search of the wisdom behind the buzzwords. We will discuss how event streams can help make your application more scalable, more reliable and more maintainable. Founded in the experience of building large-scale data systems at LinkedIn, and implemented in open source projects like Apache Kafka and Apache Samza, stream processing is finally coming of age.

On the day job, I’m on my third deployment of a message queueing system to support prototyping of stream processing algorithms. I’m really starting to appreciate the fundamental differences between various approaches. I can also say there’s no “right way” to do it. Each use case has to be looked at individually and there definitely will be some bespoke customization. Carefully define your correctness and performance guarantees and there’s a chance you’ll get it right.

Dispatches like Kleppmann’s though, are helpful in understanding what the landscape looks like and where you’d like to be.

[1]: http://blog.confluent.io/2015/01/29/making-sense-of-stream-processing/