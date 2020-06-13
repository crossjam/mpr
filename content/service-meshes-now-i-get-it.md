Title: Service Meshes, Now I Get It
Date: 2017-07-14 20:28
Author: crossjam
Category: Uncategorized
Slug: service-meshes-now-i-get-it
Status: published

Traveling in the Kubernetes orbit, I couldn’t help but hear about some new [Istio][1] thing. Unfortunately, I didn’t really have time to dig in. [Google Cloud Platform Podcast][2] during the commute for the win:

> Due to popular demand, this week Francesc and Mark are joined by Product Manager Varun Talwar and Senior Staff Software Engineer Sven Mawson to discuss all things Istio, an open platform to connect, manage, and secure microservices.

And [straight from the Istio docs][6]:

> This document introduces Istio: an open platform to connect, manage, and secure microservices. Istio provides an easy way to create a network of deployed services with load balancing, service-to-service authentication, monitoring, and more, without requiring any changes in service code. You add Istio support to services by deploying a special sidecar proxy throughout your environment that intercepts all network communication between microservices, configured and managed using Istio’s control plane functionality.

> Istio currently only supports service deployment on Kubernetes, though other environments will be supported in future versions.

Serendipitously, [the latest episode of The ArchiTECHt Show podcast][3] featured an interview with the CEO of Buoyant, William Morgan, about [Linkerd][5], which seems to be an alternative product for service meshes. From the [Linkerd][4] site:

> Linkerd is an open source, scalable service mesh for cloud-native applications.

> Linkerd was built to solve the problems we found operating large production systems at companies like Twitter, Yahoo, Google and Microsoft. In our experience, the source of the most complex, surprising, and emergent behavior was usually not the services themselves, but the communication between services. Linkerd addresses these problems not just by controlling the mechanics of this communication but by providing a layer of abstraction on top of it.

Both platforms essentially put a proxy layer between the microservices and the underlying LAN network transport. The GCP Podcast made this crystal clear. Then a bunch of functionality related to distributed services can be factored out of the apps and into the service mesh (e.g., load balancing, retries, circuit breaking). Istio is k8s only at the moment, while Linkerd is friendly with other orchestration tools like Marathon on Mesos.

Once upon a time, I worked on a project that could have really used this technology.

[1]: https://istio.io/
[2]: https://www.gcppodcast.com/post/episode-85-istio-with-varun-talwar-and-sven-mawson/
[3]: http://architechtshow.com/ep-28-buoyant-ceo-on-building-better-applications-and-conquering-the-fail-whale-with-microservices
[4]: https://linkerd.io/overview/what-is-linkerd/
[5]: https://linkerd.io/
[6]: https://istio.io/docs/concepts/what-is-istio/overview.html