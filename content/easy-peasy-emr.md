Title: Easy Peasy EMR
Date: 2012-06-08 23:31
Author: crossjam
Category: Uncategorized
Slug: easy-peasy-emr
Status: published

Holy smokes! I just ran my first ever [Elastic MapReduce (EMR)][1] job flow a few minutes ago. Surprisingly, it didn’t crash or fail to complete. Ran a bit slow, which had me thinking it was gonna bomb. But nope, my little hashtag extraction script, finished processing 100MB of data in about 7 minutes. Most of the time was spent shipping the 100MB up to the EMR Hadoop cluster once it got going

Key was the usage of [Yelp!’s mrjob][2] Python package. mrjob exploits Hadoop’s streaming mechanism to fit Python into the Java based processing pipeline. What that costs in performance is more than made up  for in flexibility and accessibility. At least for this big data hacking noob.

And I’m waiting to check the charges, but those will probably be on the order of pennies. Gotta leave having your own personal on-demand, dirt cheap cluster. 

[1]: http://aws.amazon.com/elasticmapreduce/
[2]: http://packages.python.org/mrjob/