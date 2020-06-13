Title: The Cloud Unit of Computation
Date: 2012-10-06 19:22
Author: crossjam
Category: Uncategorized
Slug: the-cloud-unit-of-computation
Status: published

> ZeroVM is to virtualization what SQLite is to DBMS.

Diggin’ in the feed cratez, I ran across a piece by Ben Lorica:  [*“How ZeroVM changes analytics in the cloud”*][1]. As Lorica points out, [ZeroVM][2] is more akin to the Java Virtual Machine then virtualization containers. However, there’s an interesting implication:

> Converged Storage in the Cloud The amount of time it takes to transfer data between two specialized clusters has led to storage systems with compute capabilities2. A recent example is storage vendor CleverSafe including Hadoop MapReduce into its dispersed storage network. Users of Hadoop MapReduce who have played with cloud computing are familiar with this issue: performing big data analysis in the cloud usually means having to first transfer data from storage systems (S3) to compute resources (EC2). This means that if lowering latency is an issue, bandwidth and data size limits what you can do. In contrast (assuming cloud services providers install it) ZeroVM lets you perform computations on the storage cluster!

Anyone who’s done any significant Big Data or parallel computation has run up against the issue of moving data versus moving computation. A computation container that’s cheap to deploy but isolates like an entire PC could be pretty handy. Throw in modern deployment tools like Chef and Puppet with Amazon Web Service style APIs and things get really interesting. Any chance AWS itself could get commoditized from below?

[1]: http://practicalquant.blogspot.com/2012/09/how-zerovm-changes-analytics-in-cloud.html
[2]: http://zerovm.org/