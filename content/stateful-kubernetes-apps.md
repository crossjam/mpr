Title: Stateful Kubernetes Apps
Date: 2018-05-02 14:32
Author: crossjam
Category: Uncategorized
Slug: stateful-kubernetes-apps
Status: published

I haven’t dived too far down the Kubernetes rabbit hole yet, but one thing I was trying to tinker with was deploying Kafka within a k8s cluster. The results were ... unsatisfying. The folks at [Cockroach Labs][2] have [observed similar issues][1] and are offering advice on how to deal with stateful k8s apps.
> In short: managing state in Kubernetes is difficult because the system’s dynamism is too chaotic for most databases to handle––especially SQL databases that offer strong consistency.

I’ll note that for Kafka, the odd peccadillos of ZooKeeper configuration make the process “anti-cloud native”. And how to expose long-lived, stateful connections, also seems to work against the Kubernetes grain.

I’m sure someone, somewhere has wrangled through all of these problems but there does seem to be a lot of toil here.

[1]: https://www.cockroachlabs.com/blog/kubernetes-state-of-stateful-apps/
[2]: https://www.cockroachlabs.com/