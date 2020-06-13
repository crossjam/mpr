Title: Force Multiplying
Date: 2012-05-31 20:13
Author: crossjam
Category: Uncategorized
Slug: force-multiplying
Status: published

Once upon a time, I called [MapReduce and Sawzall “major force multipliers”][1]. At work, I’m learning the hard way about the Sawzall part of that combination. It’s great to have a scalable distributed programming model and massive data storage engines, but data querying and manipulation are the secret sauce where the magic happens. Trying to do querying type stuff at the Java API level is “teh suck”.

According to Wikipedia, [Sawzall][2] never hit the open source big time, but at least [Pig][3], [Hive][4], and [Cascalog][5] came to be. Pinin’ for a good open source, graph query language and runbtime baked into the Hadoop ecosystem though.

[1]: http://crossjam.net/wp/nmh/archives/001126
[2]: http://en.wikipedia.org/wiki/Sawzall_(programming_language)
[3]: http://pig.apache.org/
[4]: http://hive.apache.org/
[5]: https://github.com/nathanmarz/cascalog/wiki