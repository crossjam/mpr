Title: A Chihuahua in Your Pig
Date: 2013-02-03 13:37
Author: crossjam
Category: Uncategorized
Slug: a-chihuahua-in-your-pig
Status: published

That would be [Pig][3] UDF for [GraphChi][2]. A complete [hack][1] of the best kind:

> Pig is a powerful query language for Hadoop commonly used for large scale data processing. Now it is possible to run GraphChi programs as parts of Pig-scripts, with just one line of script! This allows easy huge scale graph computation with data stored in HDFS (Hadoop File System). As GraphChi will ultimately execute only on a single Hadoop machine (see HowGraphChiForPigWorks), the size of the Hadoop Cluster is not a limiting factor.

> GraphChi for Pig is a viable alternative to Giraph, which is a distributed graph engine built on top of Hadoop. With GraphChi, you can develop your algorithms on your laptop (with realistically sized data) and then deploy them to run the big cluster. GraphChi will also often run faster and uses much less resources than alternatives.


[1]: http://code.google.com/p/graphchi-java/wiki/GraphChiForPig
[2]: http://graphlab.org/graphchi/
[3]: http://pig.apache.org/