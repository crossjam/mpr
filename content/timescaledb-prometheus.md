Title: TimescaleDB + Prometheus
Date: 2018-07-15 22:09
Author: crossjam
Category: Uncategorized
Slug: timescaledb-prometheus
Status: published

I’ve been tracking the progress of [TimescaleDB][2] for [a while][3] now. One thing that really stands out is the company’s pragmatic nature. Sure they came up with an innovative way to scale time series data storage, management, and querying. But it seems like they’ve really caught traction by meeting many customers where they’re at: relational DB knowledgeable and okay with using PostgreSQL. In a number of recent podcasts, I haven’t really heard the founders geek out about the underlying techniques but instead focus on how **the product**, not the technology, addresses customer pain points.

To wit, [a recent company blog post][1] on marrying TimescaleDB with the popular [Prometheus][5] monitoring and metrics platform:

> By using Prometheus and TimescaleDB together, you can combine the simplicity of Prometheus with the reliability, power, flexibility, and scalability of TimescaleDB, and pick the approach that makes most sense for the task at hand. In particular, it is because Prometheus and TimescaleDB are so different that they become the perfect match, with each complementing the other. For example, as mentioned earlier, you can use either PromQL or full SQL for your queries, or both.

In particular, TimescaleDB engineers have done some of heavy lifting in creating a PostgreSQL connector for the [Grafana][4] metrics visualization framework. That’s putting skin in the game that customers can see.

Also, “It’s just Postgres," is a great talking point.

I like where these guys are going.

[1]: https://blog.timescale.com/sql-nosql-data-storage-for-prometheus-devops-monitoring-postgresql-timescaledb-time-series-3cde27fd1e07
[2]: https://timescaledb.com/
[3]: https://crossjam.net/wp/mpr/2017/06/michael-freedman-and-timescaledb/
[4]: https://grafana.com/
[5]: https://prometheus.io/