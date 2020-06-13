Title: I Heart Sphinx
Date: 2012-01-28 22:30
Author: crossjam
Category: Uncategorized
Slug: i-heart-sphinx
Status: published

It's ornery and has sharp pointy teeth, but I'm coming to appreciate the [Sphinx full text indexing and search engine][1]. Might not have the greatest documentation or APIs but damn does it index like a bat out of hell.

I've personally seen it rip through approximately 4 Gb of data on a 5 year old server with only 8 Gb of RAM, said data on a suboptimal Linux ext3 filesystem, on top of an untuned kernel, and with no thought given to the IO and HD subsystems. Grand total of 21 minutes.

That is a nice capability to have.

I know [Lucene][2] with [Solr][3] on top is sort of the default open source choice for full text indexing, but if you're in the market Sphinx is worth a tire kick.

[1]: http://www.sphinxsearch.com/
[2]: http://lucene.apache.org/java/docs/index.html
[3]: http://lucene.apache.org/solr/