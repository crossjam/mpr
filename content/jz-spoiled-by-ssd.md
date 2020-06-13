Title: JZ Spoiled By SSD
Date: 2013-04-07 15:52
Author: crossjam
Category: Uncategorized
Slug: jz-spoiled-by-ssd
Status: published

JZ would be one Jeremy Zawodny, engineer at Craigslist.
> But this particular task involves slurping ALL the data out of that cluster and onto a cluster of sharded Sphinx servers so I can re-index the roughly 3 billion documents. That’s all well and good, but since our MongoDB cluster isn’t terribly performance sensitive, it is built on old-fashioned (am I allowed to use that phrase?) spinning disks. And you know what that means, right?

> Yeah, seek time matters. A lot.

> If this was hitting our production MySQL clusters, I wouldn’t care nearly as much. Those all use one flavor or another of flash stoarge. In fact, we’ve been using SSDs long enough and in enough places that I’m spoiled at this point. I sort of cringe every time I have to deal with disk seeks. That’s so five years ago.

Zawodny does this at real scale for real money So if [Jeremy’s spoiled by SSD performance][1], the rest of us can start just follow the trend.

[1]: http://blog.zawodny.com/2013/04/04/seeking-sucks-spoiled-by-ssds/