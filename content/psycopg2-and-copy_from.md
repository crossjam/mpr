Title: psycopg2 and copy_from
Date: 2012-09-19 21:15
Author: crossjam
Category: Uncategorized
Slug: psycopg2-and-copy_from
Status: published

Yesterday I was developing some code to do bulk loading of data into PostgreSQL. The db’s COPY command is the best, if not exactly most inviting way to do this, modulo possible extensions, but those haven’t worked for me.

Unfortunately, COPY reads from files local to the server or over standard input. I was dreading having to jerry-rig something out of SSH when I revisited the [*psycopg2*][1] module. Turns out psycopg2 has a [`copy_from`][2] method that does what you’d expect local or remote DB. Python FTW yet again.

Probably should have been using psycopg2 from the get go.

[1]: http://initd.org/psycopg/
[2]: http://initd.org/psycopg/docs/usage.html#using-copy-to-and-copy-from