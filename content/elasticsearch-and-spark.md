Title: Elasticsearch and Spark
Date: 2015-01-03 22:51
Author: crossjam
Category: Uncategorized
Slug: elasticsearch-and-spark
Status: published
Attachments: wp/mpr/wp-content/uploads/2015/01/Apache-Spark-Logo.png

[<img src="http://crossjam.net/wp/mpr/wp-content/uploads/2015/01/Apache-Spark-Logo.png" alt="Apache Spark Logo" border="0" width="206" height="109" align="right" style="margin: 10px;" />][2] In the day job, I was casting about for ways to integrate [Apache Spark][2] with the open source search engine [Elasticsearch][1]. Basically, I had some megawads of JSON data which Elasticsearch happily inhales, but I needed a compute platform to work with the data. Spark is my weapon of choice.

Turns out there’s a really nice [Elasticsearch Hadoop toolkit][4] that [includes making Spark RDDs][5] out of Elasticsearch searches. I have to thank Sloan Ahrens for tipping me off with [a nice clear explanation][3] of putting the connector in action:

> In this post we're going to continue setting up some basic tools for doing data science. The ultimate goal is to be able to run machine learning classification algorithms against large data sets using Apache Spark™ and Elasticsearch clusters in the cloud. 

> … we will continue where we left off, by installing Spark on our previously-prepared VM, then doing some simple operations that illustrate reading data from an Elasticsearch index, doing some transformations on it, and writing the results to another Elasticsearch index.

[1]: http://www.elasticsearch.org/
[2]: http://spark.apache.org/
[3]: http://blog.qbox.io/elasticsearch-in-apache-spark-python
[4]: http://www.elasticsearch.org/overview/hadoop/
[5]: http://www.elasticsearch.org/guide/en/elasticsearch/hadoop/current/spark.html