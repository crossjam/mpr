Title: 250K Tweets
Date: 2011-10-05 23:10
Author: crossjam
Category: Uncategorized
Slug: 250k-tweets
Status: published

About a week and a half ago I got possessed with the luny notion to collect 1 million tweets. I've worked with the [Twitter streaming api][1] in the past, so thought it would simply be a matter of keeping the connection up for an extended period of time. 

I started with the simplest possible thing that might work, directly from the Twitter streaming API documentation:

> `curl -d @locations https://stream.twitter.com/1/statuses/filter.json -uAnyTwitterUser:Password.`

First couple of cracks didn't quite work. As documented, the HTTP connection is subject to various disruptions, so I wrapped the `curl` invocation in a Python script that would re-execute as needed.

So now the script has been running for about 5 days now. I've got about 647 Mb of data totaling north of 250,000 tweets. I can't tell if the script has needed to do a restart, but I'm impressed it's lived this long.

And 250K tweets, with metadata, should make for some interesting analysis.

[1]: https://dev.twitter.com/docs/streaming-api/methods