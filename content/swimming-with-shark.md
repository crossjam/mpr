Title: Swimming With Shark
Date: 2013-01-23 21:03
Author: crossjam
Category: Uncategorized
Slug: swimming-with-shark
Status: published

Oy! I had forgotten how painful the bleeding edge of academic research can be. Spent most of the day wrasslin’ with [Shark][1] from the [Berkeley AMPLab][4], *Go Bears!* Shark = [Spark][2] + [Hive][3]. I’m trying to build the BigRAM (TM) chops and this seems to be a relatively straightforward way to do so.

Thanks to a version mismatch between HDFS client libraries, I got sucked into rebuilding most of the Shark stack. Managed to tame Scala, Hive, Spark, and sbt, but couldn’t eliminate the pesky incompatibility. Being behind a firewall while having lots of remote dependencies didn’t help things. I swear Java has more different ways to define an http proxy. Currently Shark 1 - Me 0.

Oh well. It’s off to jar hunting tomorrow.

[1]: http://shark.cs.berkeley.edu/
[2]: http://spark-project.org/research/
[3]: http://hive.apache.org/
[4]: https://amplab.cs.berkeley.edu/