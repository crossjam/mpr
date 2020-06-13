Title: Kafka and k8s
Date: 2018-05-07 21:12
Author: crossjam
Category: Uncategorized
Slug: kafka-and-k8s
Status: published

So of course as soon as [I slag on getting Apache Kafka deployed][5] to a Kubernetes cluster, [Confluent announces the Confluent Operator][1]. 

However, [a Datanami interview with Neha Narkhede][2] pretty much vindicates my concerns:
> But like most things in IT, the devil is in the details. “It’s actually not that easy,” says Neha Narkhede, the CTO and co-founder of Confluent, the commercial venture behind open source Apache Kafka. “Kubernetes is amazing, but it was designed for stateless applications.”

> Like all stateful applications, Kafka makes certain assumptions about the infrastructure that it’s running on. “If machines come and go, you have to maintain the logical context of what a node is,” Narkhede tells Datanami. “As the underling hardware changes, you need to make sure that that node concept stays the same. In addition to that, there’s a bunch of networking-layer details that need to be right.”

Two big gotchas on this announcement. First, it’s not shipping yet and even early availability won’t happen until later this summer. Second, the Confluent Operator is going into the closed source, proprietary, revenue generating bucket of the Confluent business. I can totally understand this decision, but it’ll probably be a bit of a bummer for those without an enterprise grade checkbook.

Wonder if either a really good open source deployment of Kafka on k8s emerges or this leaves a window open for other streaming platforms ([Pulsar][3], [NATS Streaming][4]) to be more k8s friendly and garner wide adoption. 

[1]: https://www.confluent.io/blog/introducing-the-confluent-operator-apache-kafka-on-kubernetes/
[2]: https://www.datanami.com/2018/05/03/want-kafka-on-kubernetes-confluent-has-it-made/
[3]: https://pulsar.incubator.apache.org/
[4]: https://github.com/nats-io/nats-streaming-server
[5]: https://crossjam.net/wp/mpr/2018/05/stateful-kubernetes-apps/