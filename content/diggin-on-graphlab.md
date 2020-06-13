Title: Diggin’ On GraphLab
Date: 2013-01-11 21:30
Author: crossjam
Category: Uncategorized
Slug: diggin-on-graphlab
Status: published

What is [GraphLab][1]?

> GraphLab is a graph-based, high performance, distributed computation framework written in C++.  While GraphLab was originally developed for Machine Learning tasks, it has found great success at a broad range of other data-mining tasks; out-performing other abstractions by orders of magnitude.

In the process of experimenting with alternatives to Hadoop for work, I revisited GraphLab. It’s come a long way since it’s 1.0 release. A lot more usable and the performance is off the charts. Let me put it to you this way, I’m able to run graph algorithms on graphs with over 60 million nodes and 1 **billion** edges that complete in minutes. Often in the time it would take a Hadoop job to even get started.

And often on a 2 year old Dell Optiplex with 2 lousy cores and desktop grade I/O. *Okay, it can’t do billions of edges fast, but an order of magnitude down is quite reasonable.*

You can do a lot of damage with a decent amount of RAM and a handful of cheap, stock SSDs. The floor at which you really need to buy into distributed, horizontal scaling is much higher than a lot of people think.

[1]: http://graphlab.org/home/