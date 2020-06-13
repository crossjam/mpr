Title: QuickThought: MT and sqlite
Date: 2009-01-26 21:17
Author: crossjam
Category: Uncategorized
Slug: quickthought_mt_and_sqlite
Status: published

Because I'm tired of hassling with full-fledged DBMS systems like <a href="http://www.mysql.com/">MySQL</a> and <a href="http://www.postgresql.org/">PostgreSQL</a> for personal stuff, the database behind this blog is <a href="http://www.sqlite.org/">sqlite</a>. Data is stored in a simple single file, subject to all the utilities of a typical UNIX environment.

Between a simple db and generating static files with <a href="http://www.movabletype.org/">MT</a>, it should be relatively straightforward to use my laptop as a staging server for <a href="http://crossjam.net/mpr/">MPR</a>.

Also makes backups damn easy. A cron job and ssh should do the trick.

