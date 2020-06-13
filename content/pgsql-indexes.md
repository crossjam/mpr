Title: PgSQL Indexes
Date: 2013-01-17 23:02
Author: crossjam
Category: Uncategorized
Slug: pgsql-indexes
Status: published

Two recent Postgres performance nuggets, both touching on indexes. 

First, Craig Kerstiens talks about [performance measurement with `pg_stat`][2], but lands on conditional indexes: 

> To further optimize this we would great a conditional OR composite index. A conditional would be where only current = true, where as the composite would index both values. A conditional is commonly more valuable when you have a smaller set of what the values may be, meanwhile the composite is when you have a high variability of values.

Next, the Instagram team illustrates some of how they’ve [scaled with Postgres][1]. They provide functional indexes as one of their tips:

> On some of our tables, we need to index strings (for example, 64 character base64 tokens) that are quite long, and creating an index on those strings ends up duplicating a lot of data. For these, Postgres’ functional index feature can be very helpful:

Both very good to know.

[1]: http://instagram-engineering.tumblr.com/post/40781627982/handling-growth-with-postgres-5-tips-from-instagram
[2]: http://craigkerstiens.com/2013/01/10/more-on-postgres-performance/