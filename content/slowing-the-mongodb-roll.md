Title: Slowing the MongoDB Roll
Date: 2011-11-06 16:15
Author: crossjam
Category: Uncategorized
Slug: slowing-the-mongodb-roll
Status: published

<div style="text-align:center;"><iframe src=http://www.xtranormal.com/xtraplayr/6995033/mongo-db-is-web-scale width=252 height=156 frameborder=0></iframe></div>

I liked what [I've read so far][3] about [MongoDB](http://mongodb.org), but that doesn't mean the actual experience will match in practice. Just to temper my enthusiasm, I've been keeping an eye out for critical commentary on the NoSQL database.

The [comical animated short][1] above takes down some of the common fanboisms at a high level. Meanwhile, Michael Susens-Schurter has [a deeper critique of MongoDB][2] with more technical detail from down in the trenches.

I still think MongoDB might be the best fit for [my Twitter data noodling][4], mainly because the streaming data comes out in JSON format. Even if MongoDB fails on a few core DB capabilities, it seems so tuned to storing and querying JSON the reward might be worth the risk. And besides, I'm not doing anything mission critical or at *Web Scale*.

[1]: http://www.xtranormal.com/watch/6995033/mongo-db-is-web-scale
[2]: http://blog.schmichael.com/2011/11/05/failing-with-mongodb/
[3]: http://crossjam.net/wp/mpr/2011/11/mongodb-and-python/
[4]: http://crossjam.net/wp/mpr/2011/10/2mm-lines/