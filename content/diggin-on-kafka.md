Title: Diggin’ On Kafka
Date: 2013-04-11 19:57
Author: crossjam
Category: Uncategorized
Slug: diggin-on-kafka
Status: published

Putting [Apache Kafka][1] through it’s paces at the office and I’m starting to like what I see after some initial confusion.
> Why we built this

> Kafka is a messaging system that was originally developed at LinkedIn to serve as the foundation for LinkedIn's activity stream and operational data processing pipeline. It is now used at a variety of different companies for various data pipeline and messaging uses.

> Activity stream data is a normal part of any website for reporting on usage of the site. Activity data is things like page views, information about what content was shown, searches, etc. This kind of thing is usually handled by logging the activity out to some kind of file and then periodically aggregating these files for analysis. Operational data is data about the performance of servers (CPU, IO usage, request times, service logs, etc) and a variety of different approaches to aggregating operational data are used.

> In recent years, activity and operational data has become a critical part of the production features of websites, and a slightly more sophisticated set of infrastructure is needed. 

I like their particular set of [design choices][2]. The client consumer side takes a little getting used to if you’re a lazy pub/sub guy like me. Kafka makes the client do a little bit more work and manage its own topic state. The upside is good to great performance, horizontal scaling, and a client can implement the message delivery semantics *(at most once, at least once, exactly once)* the client needs, without spoiling it for everyone else.

Great to see logical message offsets in [the upcoming 0.8.x releases][3] to make life a little easier.

[1]: http://kafka.apache.org/
[2]: http://kafka.apache.org/design.html
[3]: https://cwiki.apache.org/confluence/display/KAFKA/Changes+in+Kafka+0.8