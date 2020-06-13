Title: The Next Data Challenge
Date: 2012-01-02 22:00
Author: crossjam
Category: Uncategorized
Slug: the-next-data-challenge
Status: published

Now that I've honed my Twitter data collection skills a bit, a couple of new ones are coming to mind. Interestingly, I like starting them as home hacking projects and then transferring the experience to work as needed.

<!--more-->






First, collecting a million Tweets per day using the [Streaming API][1] doesn't seem completely unreasonable. Now I don't have enough home storage to handle that amount of data but I do have [Amazon S3][2]. I was getting hung up on having continuous query and analysis capabilities available. That would reauire an expensive VPS in the  cloud or another machine to worry about in the basement. But simply storing a small window of the data on a cheap VPS, pushing the data into S3, and then batch processing with Elastic MapReduce is eminently feasible. Probably good for the resume too. And with a little automation this can operate while I'm sleeping and run for days at a time. That quickly means tens to hundreds of millions of tweets. You're talking real Big Data at that point.

Second, I'm still not seeing any interesting data collection experiments from systems like Instagram or FourSquare. Maybe I'm looking in the wrong places, but seems like an opportunity to me.

Third, adaptive query specification for the Streaming API. Currently all my collection just sets up a bunch of geo boundaries and leaves them alone. Two issues here. Dynamic determination of the queries and dynamic update of the query spec. The latter isn't too hard but the former is open territory.

[1]: https://dev.twitter.com/docs/streaming-api/concepts
[2]: http://aws.amazon.com/s3/