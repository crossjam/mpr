Title: sqlite-comprehend
Date: 2022-07-12
Author: C. Ross Jam
Status: Published

Per usual Simon Willison has pushed out yet another impressive SQLite
oriented tool: [sqlite-comprehend][1]

> I built a new tool this week: sqlite-comprehend, which passes text
> from a SQLite database through the AWS Comprehend entity extraction
> service and stores the returned entities.

My attention was caught by multiple aspects:

* The usage of many pieces of his toolkit but especially
  [db-to-sqlite][2] to grab data out of PostgreSQL, since I have some
  interesting data in guess what ... PostgreSQL
* Outsourcing entity extraction out to [AWS Comprehend][3]
* The application of [SQLite’s full text search capabilities][4]
* And of course Simon’s way of writing this all up, which I aspire to
  emulate. I’m getting there with potential content.
  
Bottom line, I think it’s eminently possible to take my Discogs tables
and [Fabric views][5], export them into a single SQLite / Datasette
instance, and have an easily searchable Discogs artifact that’s simple
to distribute as one SQLite file on a CDN. 

Don’t know if anyone else would use it, but it’s an itch I’d like to
scratch.
  

[1]: https://simonwillison.net/2022/Jul/11/sqlite-comprehend/
[2]: https://datasette.io/tools/db-to-sqlite
[3]: https://aws.amazon.com/comprehend/
[4]: https://www.sqlite.org/fts3.html
[5]: {filename}/discogs_sql_views.md
