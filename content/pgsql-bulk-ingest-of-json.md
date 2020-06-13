Title: PgSQL Bulk Ingest of JSON
Date: 2012-12-29 19:36
Author: crossjam
Category: Uncategorized
Slug: pgsql-bulk-ingest-of-json
Status: published

After months of sometimes painful experimentation here’s a technique others may find useful. This is for those who need to ingest millions of JSON objects, collected from the wild, stored as line ordered text files, into a PostgreSQL table.

1. Transform your JSON lines into base64 hex encoded lines
2. Start a transaction
3. Create a temp table that deletes on commit
4. COPY from your hex encoded file into the temp table
5. Run an INSERT into your destination table that draws from a SELECT that base64 decodes the JSON column
6. COMMIT, dropping the the temp table
7. Profit!!
8. For bonus points, use the temp table to delete duplicate records or other cleanup

The benefit of this approach is that it saves you from dealing with escaping and encoding horrors. Basically, JSON can contain any character so it’s almost impossible to safely outsmart stupid users and PgSQL strictness. Once you’re over a million records, you’ll get bit by one or the other.

Reliably applied to over 300 million Tweets from the Twitter streaming API.

**Update**. If you’re doing this with Python make sure to use psycopg2 since you can control the transaction isolation and it supports COPY.