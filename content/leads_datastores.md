Title: LEADS - The League of Embeddable, Alternative DataStores
Date: 2022-06-23
Author: C. Ross Jam
Status: published

[PostgreSQL][1] is totally awesome. But sometimes it’s more useful to
have pure file(s) storage and query for your data. Herewith a
collection of data storage engines that somewhat cover the space of
more well-known engines:

<!-- PELICAN_END_SUMMARY -->

* [sqlite][2], _PostgreSQL_, "SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. SQLite is the most used database engine in the world."
* [vedis][3], _Redis_, "Vedis is an embeddable datastore C library
  built with over 70 commands similar in concept to Redis but without
  the networking layer since Vedis run in the same process of the host
  application."
* [xapian][11], _Lucene/Solr/ElasticSearch_, "Xapian is an Open Source
  Search Engine Library, released under the GPL v2+. It's written in
  C++, with bindings to allow use from Perl, Python 2, Python 3, PHP
  5, PHP 7, Java, Tcl, C#, Ruby, Lua, Erlang, Node.js and R (so far!)" [Full text search in SQLite][8] is also [quite powerful][9].
* [whoosh][4], _Lucene/Solr/ElasticSearch_, "Whoosh is a fast, pure
  Python search engine library." Fudging a little here but definitely
  embeddable in Python applications 🤣.
  * [UnQLite][5], _MongoDB and others_, "UnQLite is a in-process software library
  which implements a self-contained, serverless, zero-configuration,
  transactional NoSQL database engine. UnQLite is a document store
  database similar to MongoDB, Redis, CouchDB etc. as well a standard
  Key/Value store similar to BerkeleyDB, LevelDB, etc."
* [Mongita][6], _MongoDB_, "Mongita is a lightweight embedded document database that implements a commonly-used subset of the MongoDB/PyMongo interface."
* [DuckDB][7], _ClickHouse_, "DuckDB is an in-process SQL OLAP
  database management system"

Of course these libraries come with limitations relative to their
analogs, SQLite is not a like-for-like Postgres replacement, but they
each have their place and time. Most of all, you can go a long way
with many of these before having to go full client/server model.

Big shout out to [Charles Leifer][10] who did a wonderful job blogging
about Python and many of these stores. Along with Simon Willison, his
writings taught me a ton about the capabilities of lesser known
datastores, especially SQLite. Too bad his blogging seems to be on
hiatus.

[1]: https://postgresql.org/
[2]: https://sqlite.org/
[3]: https://vedis.symisc.net/
[4]: https://whoosh.readthedocs.io/
[5]: https://unqlite.org
[6]: https://github.com/scottrogowski/mongita
[7]: https://duckdb.org/
[8]: https://charlesleifer.com/blog/using-the-sqlite-json1-and-fts5-extensions-with-python/
[9]: https://simonwillison.net/2019/Jan/7/exploring-search-relevance-algorithms-sqlite/
[10]: https://charlesleifer.com/
[11]: https://xapian.org/
