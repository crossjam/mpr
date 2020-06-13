Title: PGSQL FDW
Date: 2011-12-05 22:33
Author: crossjam
Category: Uncategorized
Slug: pgsql-fdw
Status: published

<img src="http://crossjam.net/wp/mpr/wp-content/uploads/2011/09/PostgreSQL-Logo.png" alt="PostgreSQL Logo" border="0" width="120" height="120" align="right" style="margin: 10px;" /> Link parkin': [PostgreSQL Foreign Data Wrappers][1].

When this link first started kicking around, I thought it was just a gimmicky way to pull data into Postgres (PGSQL), destined to be slow and finicky. Boy was I wrong! Turns out [Foreign Data Wrappers (FDW) are an SQL standard][3] that the latest version of Postgres, 9.1, heavily supports. Turns out there are all sorts of interesting uses for FDWs. Turns out that [Multicorn][2] makes writing the wrappers in Python relatively straightforward.

At work, I've got some hairy data ingest challenges for Postgres. Maybe FDWs can help solve them.

*Hat tip, Ben Lorica's [Big Data][4] Twitter stream*

[1]: http://wiki.postgresql.org/wiki/Foreign_data_wrappers
[2]: http://multicorn.org/
[3]: http://wiki.postgresql.org/wiki/SQL/MED
[4]: https://twitter.com/#!/bigdata/