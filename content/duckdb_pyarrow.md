Title: DuckDB and PyArrow
Date: 2022-05-13
Author: crossjam
Status: published

I previously link parked [DuckDB][2] as an embedded, high speed, OLAP
engine. Gerard Bentley has [some nice examples][1] of using DuckDB, Arrow, and
Python. Even though the combo isn’t definitively better than Pandas
and Arrow, I like how seamless the integration between DuckDB and
Arrow data appears. Simply referencing a Python variable from a DuckDB
query is a neat trick. Wonder how that’s implemented under the covers.

Related [_DuckDB quacks Arrow: A zero-copy data integration between Apache Arrow and DuckDB_][3]

[1]: https://tech.gerardbentley.com/python/data/intermediate/2022/04/26/holy-duck.html
[2]: https://duckdb.org/
[3]: https://arrow.apache.org/blog/2021/12/03/arrow-duckdb/
