Title: Pulsar Messaging Concepts
Date: 2017-09-29 20:05
Author: crossjam
Category: Uncategorized
Slug: pulsar-messaging-concepts
Status: published
Attachments: wp/mpr/wp-content/uploads/2017/09/pulsar-logo-1.png

[<img src="https://crossjam.net/wp/mpr/wp-content/uploads/2017/09/pulsar-logo-1.png" alt="Pulsar logo" title="pulsar-logo.png" border="0" width="280" height="54" style="float:left;padding:10px" />][1] I still like to play like a messaging guy on occasion. Today I was digging around the documentation for [Apache Pulsar][1] which is the underlying messaging framework for the [Streamlio][2] product. 
> Pulsar’s key features include:

> * Native support for multiple clusters in a Pulsar instance, with seamless geo-replication of messages across clusters
* Very low publish and end-to-end latency
* Seamless scalability out to over a million topics
* A simple client API with bindings for Java, Python, and C++
* Multiple subscription modes for topics (exclusive, shared, and failover)
* Guaranteed message delivery with persistent message storage provided by Apache BookKeeper

Pulsar’s underlying, fundamental concepts are quite interesting, compared to [nsq][4], [Kafka][5], [rabbitmq][6] et. al. The clustering and brokering seem a bit complex but Pulsar is from folks who had some really hard problems. The notion of failover subscriptions is an interesting twist though. Might be worth taking Pulsar for test drive in a few containers.

[1]: https://pulsar.apache.org/
[2]: https://streaml.io/
[3]: http://pulsar.apache.org/docs/latest/getting-started/ConceptsAndArchitecture/
[4]: http://nsq.io/
[5]: https://kafka.apache.org/
[6]: https://www.rabbitmq.com/