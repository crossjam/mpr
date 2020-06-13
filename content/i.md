Title: I 
Date: 2013-04-07 16:04
Author: crossjam
Category: Uncategorized
Slug: i
Status: published

The situation.

Disk A. 95% full with Postgres data.

Disk B. 75% full with archival data.

What to do about Disk A?

Move data from disk B to another drive, getting it down to 20% full. Use [Postgres’ `CREATE TABLESPACE` data definition statement][1] to make a new one on Disk B. Run a series of  `ALTER TABLE`s and `ALTER INDEX`s to safely  move half of the Postgres data to Drive B.

Now both drives are at about 60% full and I’m a happy camper with plenty of disk headroom going forward. **Bonus**, both A and B are SSDs, so with an hour or so of effort, all my data stays fast and my queries might even get a little boost from disk parallelism to boot.

[1]: http://www.postgresql.org/docs/9.2/static/manage-ag-tablespaces.html