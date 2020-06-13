Title: Dadgum PostGIS!!
Date: 2012-11-02 07:48
Author: crossjam
Category: Uncategorized
Slug: dadgum-postgis
Status: published

<img src="http://crossjam.net/wp/mpr/wp-content/uploads/2011/10/PostGIS-Logo-Small.png" alt="PostGIS Logo Small" border="0" width="120" height="120" align="right" style="margin: 10px;" /> I’ve been enjoying the power of [PostGIS][1] at work, although it confounds me to no end. Given the amount of data I’m trying to query against, typically upwards of 10s of millions of rows, I haven‘t found writing efficient spatial queries to be straightforward. This week provided an opportunity to develop a hypothesis about why.

On one machine, I have my spatial DB on a traditional spinning disk HD drive. A query I wrote took about 6 hours. I’ve taken up the radical experiment *(for our research org, we move hella fast  ;-/)*  putting the same DB on a consumer grade Solidstate Storage Disk to see what would happen. Query time dropped to about 10 minutes. My back of the envelope calculation shows a 36x improvement. Caveat this with the understanding that I have in no way conducted a scientific comparison. Apples to oranges and all that.

Still the query went from doable to damn useful. Why? My guess is that spatial data and indexing are hard to lay out for good sequential access. Random disk seeks wind up being the order of the day. Thus, the advantages of SSDs really start to shine.
 
Just a hunch, but I really need to conduct some deeper investigation. And maybe attend some [local][2] geo [meetups][3] to commiserate with fellow travelers.

[1]: http://postgis.refractions.net/
[2]: http://www.meetup.com/Geo-DC/
[3]: http://www.meetup.com/Geo-NoVA/