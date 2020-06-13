Title: Exactly Once Processing
Date: 2017-07-28 18:43
Author: crossjam
Category: Uncategorized
Slug: exactly-once-processing
Status: published

I promised to revisit [the topic of Kafka’s new “exactly once processing.”][3] A while ago, Tyler Treat generated a relatively popular post entitled [*“You Cannot Have Exactly Once Delivery”*][2]. Treat came back and [recontextualized the original argument][1] in the face of Confluent’s recent work.

> First, let me say what Confluent has accomplished with Kafka is an impressive achievement and one worth celebrating. They made a monumental effort to implement these semantics, and it paid off. The intention of this post is not to minimize any of that work but to try to clarify a few key points and hopefully cut down on some of the misinformation and noise.

The gist is that the Kafka Streams approach is a fairly closed framework that works with the messaging system to ensure a particular semantics correctly with reasonable performance. That’s a good thing. Definitely worth a read if you’re a messaging junkie. 

[1]: http://bravenewgeek.com/you-cannot-have-exactly-once-delivery-redux/
[2]: http://bravenewgeek.com/you-cannot-have-exactly-once-delivery/
[3]: https://crossjam.net/wp/mpr/2017/07/exactly-once/