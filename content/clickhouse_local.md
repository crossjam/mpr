Title: Working Locally with Clickhouse
Date: 2023-01-08
Status: published

[ClickHouse][1] is a database tool I haven’t had a chance to sink my
teeth into but heard good things about. [_Extracting, converting, and
querying data in local files using clickhouse-local_][2] is an
overview of using ClickHouse to work on data hosted on a node.

> Sometimes we have to work with files, like CSV or Parquet, resident
> locally on our computers, readily accessible in S3, or easily
> exportable from MySQL or Postgres databases. Wouldn’t it be nice to
> have a tool to analyze and transform the data in those files using
> the power of SQL, and all of the ClickHouse functions, but without
> having to deploy a whole database server or write custom Python
> code? 

> Fortunately, this is precisely why clickhouse-local was created! The
> name “local” indicates that it is designed and optimized for data
> analysis using the local compute resources on your laptop or
> workstation. In this blog post, we’ll give you an overview of the
> capabilities of clickhouse-local and how it can increase the
> productivity of data scientists and engineers working with data in
> these scenarios. 

Also noting yet another database with embedded HTTP request capabilities.

[1]: https://clickhouse.com
[2]: https://clickhouse.com/blog/extracting-converting-querying-local-files-with-sql-clickhouse-local
