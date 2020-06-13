Title: SpiderDuck Deep Dive
Date: 2011-11-15 21:14
Author: crossjam
Category: Uncategorized
Slug: spiderduck-deep-dive
Status: published

Once upon a time, I was developing a small scale RSS feed aggregator for hundreds to thousands of feeds. Man the intricacies of repeated HTTP fetching were hairy. Getting HTTP headers right, obeying `robots.txt`, throttling domain access, dealing with domain resolution, avoiding spider traps, scheduling revisits. Not to mention that if you surmounted all of those hurdles, you still had to deal with people's often ill-formed RSS. Good times!

While not a one-to-one mapping of concerns, I still found quite interesting this [deep dive][1] into the technical details of SpiderDuck, Twitter's scalable, real-time URL fetcher. They're not really crawling sites, just trying to fetch URLs as quickly as they flow through the Twittersphere, so Twitter doesn't have to worry about recursive fetching. Probably don't have to deal with revisits, but still have to throttle request rates to particular domains. I guarantee there are some twisted souls out there trying to suck their fetching into infinite URL traps.

A lot has changed since I was doing my half-baked tinkering. For example, the whole Hadoop/HDFS/Cassandra/Memcached scalable computing infrastructure flat out didn't exist. At the same time, a lot of the same issues are still there. The Web is still The Web, warts and all.

*Hat tip: [Nelson Minar's Pinboard][2]*

[1]: http://engineering.twitter.com/2011/11/spiderduck-twitters-real-time-url.html
[2]: http://pinboard.in/u:nelson