Title: Processing A Billion Taxi Rides
Date: 2016-06-04 12:55
Author: crossjam
Category: Uncategorized
Slug: processing-a-billion-taxi-rides
Status: published

[Mark Litwintschik][2] has been doing yeoman’s work with the [New York City Taxi & Limousine Commission data][3]. Over a series of blog posts he’s taken this one dataset and processed it with a number of data management and “big data” technologies, including [purchasing an Amazon Redshift cluster][1]:

> Over the past few months I've been benchmarking a dataset of 1.1 billion taxi journeys made in New York City over a six year period on a number of data stores and cloud services. Among these has been AWS Redshift. Up until now I've been using their free-tier and single-compute node clusters. While these make Data Warehousing very inexpensive they aren't going to be representative of the incredible query speeds which can be achieved with Redshift.

> In this post I'll be looking at how fast a 6-node ds2.8xlarge Redshift Cluster can query over a billion records from the dataset I've put together.

Litwintschik’s admirable in how well he documents the steps he takes to actually running queries against such a large dataset. Just getting such data into the right place to work with is challenging. There are lots of places you can trip up doing this stuff and his work can save others a lot of trouble.

Something along these lines is what I’m aspiring to do with [Fun With Discogs Data][4].

[1]: http://tech.marksblogg.com/billion-nyc-taxi-rides-redshift-large-cluster.html
[2]: http://tech.marksblogg.com/
[3]: http://toddwschneider.com/posts/analyzing-1-1-billion-nyc-taxi-and-uber-trips-with-a-vengeance/
[4]: http://crossjam.net/wp/mpr/2016/05/fwdd-0-fun-with-discogs-data/