Title: 1.1 Billion Taxi Rides on BrytlytDB
Date: 2017-07-31 21:18
Author: crossjam
Category: Uncategorized
Slug: 1-1-billion-taxi-rides-on-brytlytdb
Status: published

I’ve mentioned before [the fine work that Mark Litwintschik does][1] putting data management systems through their paces using a dataset of 1.1 billion taxi rides. He’s back with [another post][3] on [BrytlytDB][2].

> [BrytlytDB][2] is an in-GPU-memory database built on top of PostgreSQL. It's operated using many of PostgreSQL's command line utilities, it's wire protocol compatible so third-party PostgreSQL clients can connect to BrytlytDB and queries are even parsed, planned and optimised by PostgreSQL's regular codebase before the execution plan is passed off to GPU-optimised portions of code BrytlytDB offer.

There have been quite a few posts by Litwintschik since I noted his efforts. What caught my eye this time is the mention of the, new to me, BrytlytDB. BrytlytDB apparently leverages a lot of the core capabilities of the PostgreSQL code base and presents a lot of API compatibility. To quote from the homepage, “Brytlyt combines the power of GPUs with patent pending IP and integrates with PostgreSQL.”

I probably have a bit of myopia, but it feels like PostgreSQL essentially defines the baseline for commercial DBMS functionality these days.

And once again, I have to commend Litwintschik on the thoroughness of his reporting on these posts. One of the few technical bloggers who provides enough detail to actually approach “reproducibility.”

[1]: https://crossjam.net/wp/mpr/2016/06/processing-a-billion-taxi-rides/
[2]: http://www.brytlyt.com/
[3]: http://tech.marksblogg.com/billion-nyc-taxi-rides-aws-ec2-p2-16xlarge-brytlytdb.html