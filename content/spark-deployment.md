Title: Spark Deployment
Date: 2012-12-20 20:24
Author: crossjam
Category: Uncategorized
Slug: spark-deployment
Status: published

Wow! I didn’t realize how easy it was to [run a Spark/Mesos cluster on Amazon EC2][1]:
> The spark-ec2 script, located in Spark’s ec2 directory, allows you to launch, manage and shut down Spark clusters on Amazon EC2. It automatically sets up Mesos, Spark and HDFS on the cluster for you. This guide describes how to use spark-ec2 to launch clusters, how to run jobs on them, and how to shut them down. It assumes you’ve already signed up for an EC2 account on the Amazon Web Services site.

Might be fun to just spin one up and run against some [Common Crawl data][2].

[1]: http://spark-project.org/docs/latest/ec2-scripts.html
[2]: http://commoncrawl.org/data/accessing-the-data/