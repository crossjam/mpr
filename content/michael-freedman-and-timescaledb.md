Title: Michael Freedman and TimescaleDB
Date: 2017-06-26 21:32
Author: crossjam
Category: Uncategorized
Slug: michael-freedman-and-timescaledb
Status: published

I’ve already [noted][2] the interesting [TimescaleDB][3] project. Recently, Michael Freedman, a co-founder of the Timescale company and a full professor at Princeton University, did [a podcast interview with Ben Lorica][1]. I found it to be quite enjoyable, diving into how and why TimescaleDB came to be:

> We initially were developing a platform to collect and store and analyze IoT data, and certainly a lot of IoT data is time-series in nature. We found ourselves struggling. The reason a lot of people adopt NoSQL was they thought it offered scale in the ways that more traditional relational databases did not—yet, they often gave up a lot of the rich query language, optimized complex queries, joins, and an ecosystem that you get in these more traditional relational databases. Customers who were using our platform kept wanting all these ways to query the data, and we couldn't do it with the existing NoSQL database we were using. It just didn't support those types of queries.

What I didn’t know is how [accomplished a systems researcher][4] is Freedman. His research contributions go all the way back to turn of the millennium peer-to-peer stuff and he was talking “eventual consistency” before people got CAPed. Blame it on my Berkeley blinders.

[1]: http://practicalquant.blogspot.com/2017/06/a-scalable-time-series-database-that-supports-sql.html
[2]: http://crossjam.net/wp/mpr/2017/06/timescaledb/
[3]: http://www.timescale.com/
[4]: http://www.cs.princeton.edu/~mfreed/publications/