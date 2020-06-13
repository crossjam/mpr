Title: Blaze Expressions
Date: 2014-09-03 22:50
Author: crossjam
Category: Uncategorized
Slug: blaze-expressions
Status: published

**“tl;dr Blaze abstracts tabular computation, providing uniform access to a variety of database technologies”**

Haven’t gotten a chance to dig in yet, but [Continuum Analytics’ new Blaze Expressions library][1] is worthy of further inspection:
> Occasionally we run across a dataset that is too big to fit in our computer’s memory. In this case NumPy and Pandas don’t fit our needs and we look to other tools to manage and analyze our data. Popular choices include databases like Postgres and MongoDB, out-of-disk storage systems like PyTables and BColz and the menagerie of tools on top of the Hadoop File System (Hadoop, Spark, Impala and derivatives.) Each of these systems has their own strengths and weaknesses and an experienced data analyst will choose the right tool for the problem at hand. Unfortunately learning how each system works and pushing data into the proper form often takes most of the data scientist’s time.

> **The startup costs of learning to munge and migrate data between new technologies often dominate biggish-data analytics.**

> Blaze strives to reduce this friction. Blaze provides a uniform interface to a variety of database technologies and abstractions for migrating data.

I especially like the notion of exploiting multiple different  frameworks such as in-memory (Pandas), SQL, NoSQL (MongoDB),  and Big Data (Apache Spark) for tabular backend engines.

[1]: http://continuum.io/blog/blaze-expressions