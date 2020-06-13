Title: Materialize
Date: 2020-06-04 21:10
Author: crossjam
Category: Uncategorized
Slug: materialize
Status: published

Link parkin’: [Materialize][1]
> The simplicity of SQL queries, but with millisecond-level latency for real-time data. That is Materialize, the only true SQL streaming database for building internal tools, interactive dashboards, and customer-facing experiences.

Wire format compatible with PostgreSQL, so you can use the `psql` command line tool, even though there’s not a Postgres database underneath. Possibly a worthy challenger to [ksqlDB][4] 

Principally brought to you by [that guy][3] who wrote [“Scalability! But at what COST?"][2]

[1]: https://materialize.io/about/
[2]: https://crossjam.net/wp/mpr/2015/01/at-what-cost/
[3]: https://github.com/frankmcsherry/blog
[4]: https://ksqldb.io