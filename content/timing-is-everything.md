Title: Timing is Everything
Date: 2011-09-06 22:41
Author: crossjam
Category: Uncategorized
Slug: timing-is-everything
Status: published

Enjoyed Paul Lamere's [documenting][1] how he processed a very large music dataset using [Amazon S3][7] and [Amazon Elastic MapReduce][6]. Paul was hacking the [Million Song Dataset][2], but the info seems highly relevant to my noodlings with the [MemeTracker data][3]. It's pretty amazing anybody off the street can harness that much processing power for 10 bucks. And it finished for Lamere in 20 minutes.

One thing I've learned, munging a few tens of gigabytes, you start to time everything. Once things start taking longer than 10 minutes or so you want to 1) figure out if you're doing something stupid, and 2) figure out how to make it faster.

Personally, I've got a short term goal to get my data up onto S3. Then I'll be digging into [MrJob][4], which I've [run across previously][5].

[1]: http://musicmachinery.com/2011/09/04/how-to-process-a-million-songs-in-20-minutes/
[2]: http://labrosa.ee.columbia.edu/millionsong/
[3]: http://snap.stanford.edu/data/memetracker9.html
[4]: http://packages.python.org/mrjob/index.html
[5]: http://engineeringblog.yelp.com/2010/10/mrjob-distributed-computing-for-everybody.html
[6]: http://aws.amazon.com/elasticmapreduce/
[7]: http://aws.amazon.com/s3/