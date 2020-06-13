Title: 2 mrjob Thoughts
Date: 2012-12-25 19:49
Author: crossjam
Category: Uncategorized
Slug: 2-mrjob-thoughts
Status: published

I’ve been putting [mrjob][1] to the task quite a bit recently. Two quick thoughts on a highly useful package.

First, [Map/Reduce][2] is a fairly handy data processing framework even if you don’t need a ton of scalability. Any complex UNIX text file processing involving transforms, filters, and aggregations might be more easily expressed as a Map/Reduce computation. mrjob makes that quite   simple to do on a single machine at a high level.

Second, mrjob supports the bundling and uploading of custom code and data to support the job. I’ve mainly been using it to add Python extension modules, but there’s no reason one couldn’t include supplemental data in a binary form, like a Python pickle, or an SQLite DB. Very handy for map side augmentation or filtering presuming the data set isn’t too large.

[1]: https://github.com/Yelp/mrjob
[2]: http://en.wikipedia.org/wiki/MapReduce