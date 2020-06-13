Title: Python Hadooping
Date: 2013-01-07 23:04
Author: crossjam
Category: Uncategorized
Slug: python-hadooping
Status: published

In my day job, I’ve been using [Yelp!’s mrjob framework][2] to run a lot of Hadoop Map-Reduce jobs. Takes a lot of the Java pain away. So it was with quite a bit of interest that I dug into Uri Laserson’s [*A Guide to Python Frameworks for Hadoop*][1]:

> I recently joined Cloudera after working in computational biology/genomics for close to a decade. My analytical work is primarily performed in Python, along with its fantastic scientific stack. It was quite jarring to find out that the Apache Hadoop ecosystem is primarily written in/for Java. So my first order of business was to investigate some of the options that exist for working with Hadoop from Python.

> In this post, I will provide an unscientific, ad hoc review of my experiences with some of the Python frameworks that exist for working with Hadoop, including:

His bottom line is that straight Hadoop Streaming with Python has the best performance. Meanwhile, mrjob is well maintained, active, and quite productive, but comes with a significant performance hit.

A small sample size, but worth reading to know all your options if you’re into mixing elephants and snakes.

[1]: http://blog.cloudera.com/blog/2013/01/a-guide-to-python-frameworks-for-hadoop/
[2]: https://github.com/Yelp/mrjob