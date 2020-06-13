Title: Why HDFS
Date: 2012-08-05 18:36
Author: crossjam
Category: Uncategorized
Slug: why-hdfs
Status: published

<img src="http://crossjam.net/wp/mpr/wp-content/uploads/2011/12/Hadoop-Logo.jpg" alt="Hadoop Logo" border="0" width="200" height="150" align="right" style="margin: 10px;" /> Charles Zedlewski makes [an interesting analogy][1] between [HDFS ™][2], the Hadoop Distributed File System, and the Linux operating system. Stealing the punchline: 
> It’s rare when you get to see history repeat itself so completely as it is with HDFS.  Today HDFS may not be the best filesystem for content addressable storage or nearline archive.  But then 15 years ago who would have thought Linux would find its way into laptops, routers, mobile phones and airport kiosks?

> Linux drew us the map.  The smart money is already following it.

We’ll see how it plays out, but given the entrenched nature of HDFS he might be right. HDFS’ open source nature, and maybe more importantly community, means just about any good  distributed file system idea can be quickly embraced and extended.

There is probably one area where HDFS could be radically updated or face displacement. Real-time streaming datasets don’t fit the HDFS model particularly well.  Doesn’t mean someone smart can’t come along and fix it up. 

Zedlewski also heavily invokes the nice support for Map/Reduce processing that HDFS provides. Map/Reduce is clearly successful, but these other processing demands may eventually lead to other programming models that fit less well with HDFS.

But I’m of a mind that Zedlewski is mostly right, and that HDFS is a nice solid foundation to build on going forward.

[1]: http://www.cloudera.com/blog/2012/07/why-we-build-our-platform-on-hdfs/
[2]: http://hadoop.apache.org/hdfs/