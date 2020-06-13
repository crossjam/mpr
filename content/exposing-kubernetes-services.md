Title: Exposing Kubernetes Services
Date: 2018-07-05 22:36
Author: crossjam
Category: Uncategorized
Slug: exposing-kubernetes-services
Status: published

While there are quite a bunch of them, the fundamental conceptual elements of Kubernetes are fairly accessible. Nodes? Check. Containers? Check. Pods? Check. Services? [Pretty straightforward][1], although there is some not oft mentioned complexity in the underlying network routing across pods. 

> A Kubernetes Service is an abstraction which defines a logical set of Pods and a policy by which to access them - sometimes called a micro-service. The set of Pods targeted by a Service is (usually) determined by a Label Selector (see below for why you might want a Service without a selector).

Check out the “Virtual IPs and service proxies,” subhead of the __Services__ docs to see what I mean about networking.


Exposing services to the outside world? Not so much. Alternatively, if you can make sense of [this gobbledygook][2], you’re a better person than I. __Service Types__ are the singular concept where I have yet to see a good, comprehensible tutorial, either written, audio, or video. Something I’ll be on the lookout for.

[1]: https://kubernetes.io/docs/concepts/services-networking/service/
[2]: https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types