Title: Riak Tradeoffs
Date: 2011-12-30 22:00
Author: crossjam
Category: Uncategorized
Slug: riak-tradeoffs
Status: published
Attachments: wp/mpr/wp-content/uploads/2011/12/Riak-Logo.png

[<img src="http://crossjam.net/wp/mpr/wp-content/uploads/2011/12/Riak-Logo.png" alt="Riak Logo" border="0" width="200" height="76" align="left" style="margin: 10px;" />][2] What with the piles of data I have to process at work, I keep an eye out on the various storage, indexing, and query technologies. One product, [Riak][2], looks good but hasn't quite fit my use cases. There's a [nice overview on InfoQ][1], with Andy Gross and Mark Phillips of Basho Technlogies, on the tradeoffs that Riak provides.

The big downside for me has been the need for relatively sophisticated ad hoc querying. The Basho team points out that Riak isn't particularly good for that, being more of a building block towards that capability. The high availability, horizontal scalability, and good performance on greater than main memory working sets are attractive features though. 

May have to run some experiments at work just to baseline the Riak potential.

[1]: http://www.infoq.com/news/2011/12/andy-gross-riak-database
[2]: http://basho.com/products/riak-overview/