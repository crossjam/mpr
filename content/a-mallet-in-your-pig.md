Title: A Mallet in Your Pig
Date: 2013-02-01 19:32
Author: crossjam
Category: Uncategorized
Slug: a-mallet-in-your-pig
Status: published

Diving deeper into the Hadoop ecosystem, I’m starting to appreciate languages like Hive and Pig much more. The ability to extend each with UDFs really expands their possibilities. 

Here’s an old, but still neat, [hack][1] from Jacob Perkins, [The Data Chef][2]. He’s folding the capabilities of Mallet, an open source topic modeling toolkit, into the Pig language:

> I'm going to use Apache Pig and Mallet, a java based machine learning and natural language processing library to discover topics in the 20 newsgroups data set. This corpus is nice since each document already belongs to a newsgroup (a topic) and so it gives us a way of checking how well our topic discovery is doing. …

> So it's clear that we're going to need a java udf to do the actual topic clustering. Right? This udf will operate on a DataBag of documents and return a DataBag containing the discovered topics.

Extensibility For The Win.

[1]: http://thedatachef.blogspot.com/2012/03/topic-discovery-with-apache-pig-and.html
[2]: https://twitter.com/TheDataChef