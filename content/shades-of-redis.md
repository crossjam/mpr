Title: Shades of Redis
Date: 2015-05-27 20:40
Author: crossjam
Category: Uncategorized
Slug: shades-of-redis
Status: published

Good piece from Charles Leifer highlighting [a couple of alternative takes][2] on the [redis][1] key/datastructure store:

> Recently I've learned about a few new Redis-like databases: Rlite, Vedis and LedisDB. Each of these projects offers a slightly different take on the data-structure server you find in Redis, so I thought that I'd take some time and see how they worked. In this post I'll share what I've learned, and also show you how to use these databases with Walrus, as I've added support for them in the latest 0.3.0 release.

I’m particularly intrigued by the embedded [Rlite][3] store. Seems like something useful for situations slightly less relational than what SQLite can service.

[1]: http://redis.io
[2]: http://charlesleifer.com/blog/alternative-redis-like-databases-with-python/
[3]: https://github.com/seppo0010/rlite