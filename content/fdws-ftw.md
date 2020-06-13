Title: FDWs FTW
Date: 2012-10-19 19:10
Author: crossjam
Category: Uncategorized
Slug: fdws-ftw
Status: published

Craig Kerstiens on putting [Redis in Postgres][1]
> SQL is an expressive language, though people are often okay with accessing Mongo data through its own ORM. The real value is that you could actually query the data from within Postgres then join across your data stores, without having to do some ETL process to move data around.

From experience, here be dragons, but used judiciously [Postgres’ Foreign Data Wrappers][2] are a great feature.

[1]: http://www.craigkerstiens.com/2012/10/18/connecting_to_redis_from_postgres/
[2]: http://crossjam.net/wp/mpr/2011/12/pgsql-fdw/