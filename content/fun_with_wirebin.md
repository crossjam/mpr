Title: Fun With wirebin
Date: 2010-07-09 17:42
Author: crossjam
Category: Uncategorized
Slug: fun_with_wirebin
Status: published

Today I did some really simple timing runs, can't even glorify them as experiments, with [wirebin][1], which I grabbed from [Slide's open source][2] repository. Initial indications are that wirebin is pretty freaking fast.

I generated a Python list of 1 million random integers, ranging from 1 to 1 million.  wirebin can serialize that datastructure in 43 milliseconds and deserialize in 51 milliseconds. This is on my bottom of the line, going on two years old, MacBook. A round trip of such a list, representing an edge list for a node in a graph say, would take roughly a tenth of second. Keep in mind, this is a pretty big edge list for a single node. For most real world graphs, you're probably looking at four or five orders of magnitude smaller.

So I did the quick and dirty timings for lists of 100 integers. We're talking about 8 **microseconds** for a serialize/deserialize cycle, which would be over 120000 updates per second.

Where is this going? Getting back to my [mental canoodling][3] about Python, prefuse, and SQLite, one issue is representing graphs with tables. prefuse stores edge lists directly in the tables so it doesn't have to do an expensive "SQL" query to find all the edges in or out of a node. A cheap id lookup can be used to pull out the edge list.

If you're going to do the same trick with python and SQLite, an obvious route is to store Python lists in SQLite. But that's not supported natively. Luckily the Python SQLite module allows you to easily extend a database connection with custom object serialization and deserialization. Thanks to wirebin, that looks like it wouldn't be a performance bottleneck.

More to come...

[1]: http://github.com/slideinc/wirebin

[2]: http://slideinc.github.com/

[3]: http://crossjam.net/mpr/2010/06/prefuse-python-and-sqlite.html

