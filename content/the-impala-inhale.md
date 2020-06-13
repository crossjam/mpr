Title: The Impala Inhale
Date: 2013-04-19 21:45
Author: crossjam
Category: Uncategorized
Slug: the-impala-inhale
Status: published

[Cloudera’s Impala][2] sounds like [an exciting way to query HDFS and HBase data][3] at interactive speeds. But the installation dependencies are sort of painful, basically forcing either the use of Cloudera Manager or Cloudera’s packages for RedHat Enterprise Linux. Checking out [the fun-filled requirements][1] even includes this gem:
> Impala creates and uses a user and group named impala. Do not delete this account or group and do not modify the account's or group's permissions and rights. Ensure no existing systems obstruct the functioning of these accounts and groups. For example, if you have scripts that delete user accounts not in a white-list, add these accounts to the list of permitted accounts. 

So now the user accounts space gets littered on along with a bunch of other config files across the filesystem. Yick!

Makes [Shark][4] look a lot more attractive from a small scale applied research project level. I think you can do Shark, and Spark, pretty much from tar balls and at user level. And avoiding that enterprisey inhale is a good way to reduce complexity.

[1]: http://www.cloudera.com/content/cloudera-content/cloudera-docs/ImpalaBeta/0.7/Installing-and-Using-Impala/ciiu_topic_2_1.html
[2]: http://blog.cloudera.com/blog/2012/10/cloudera-impala-real-time-queries-in-apache-hadoop-for-real/
[3]: http://blog.cloudera.com/blog/2013/03/one-users-impala-experience-at-data-hacking-day/
[4]: http://shark.cs.berkeley.edu/