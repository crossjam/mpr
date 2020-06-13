Title: Boinging the Common Crawl
Date: 2012-12-31 14:54
Author: crossjam
Category: Uncategorized
Slug: boinging-the-common-crawl
Status: published

Here’s an interesting hack I don’t really don’t have time to execute on. Take a [BoingBoing data dump][1] and dissect either references to Boing Boing pages or outlinks from the archive using the [Common Crawl dataset][2]. Might be some interesting intersections, or you could trace out the patterns of BoingBoing influence.

Tangential side project, build up a set of [mrjob][3] modules to work with either dataset. The BoingBoing stuff comes in one big file so it might be useful for someone else to bust it up into some smaller units and stuff onto Amazon S3, or otherwise make publicly available.

[1]: http://boingboing.net/2011/01/25/eleven-years-worth-o.html
[2]: http://commoncrawl.org/data/accessing-the-data/
[3]: https://github.com/Yelp/mrjob