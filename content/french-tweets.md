Title: French Tweets
Date: 2012-08-29 20:12
Author: crossjam
Category: Uncategorized
Slug: french-tweets
Status: published

Between casual personal hacking and work responsibilities, I'm going on close to a year of serious Twitter data collection activities. So I’m always interested to see other folks’ case studies of their Twitter data hacking. Laurent Luce describes, in exquisite detail, a recent effort to [track French politician mentions][1] in the Twittersphere during their 2012 election.
> This post describes how Pytolab was designed to process Tweets related to the 2012 French presidential election, in real-time. This post also goes over some of the statistics computed over a period of 9 months.

I must be a vet now since I saw their number of 8 million tweets and thought “is that all?” But even at that scale there’s something to be learned from their processing architecture although I was surprised that they ran into peak performance issues with an Amazon EC2 micro instance. A lot of the work I do is on nominally equivalent hardware and it seems up to the task. Maybe it’s the virtualization tax.

[1]: http://www.laurentluce.com/posts/python-twitter-statistics-and-the-2012-french-presidential-election/