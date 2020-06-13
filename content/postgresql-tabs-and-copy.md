Title: PostgreSQL, Tabs, and COPY
Date: 2011-12-16 22:15
Author: crossjam
Category: Uncategorized
Slug: postgresql-tabs-and-copy
Status: published

[<img src="http://crossjam.net/wp/mpr/wp-content/uploads/2011/09/PostgreSQL-Logo.png" alt="PostgreSQL Logo" border="0" width="120" height="120" align="right" style="margin: 10px;" />](http://www.postgresql.org) Learned this the hard way, so maybe posting it will help someone else out.

PostgreSQL supports the SQL [COPY statement][1] which is a good way to bulk load a lot of data fast. Think a million tweets in JSON. Each row pulls out some of the key tweet fields into columns and the tweet JSON is also stored in a field just in case. The tricky part is that the bulk load input data, that's not already dumped from a Postgres DB, has to be in a text format that's akin to [CSV][2].

This isn't a big deal if your table fields are relatively simple, but as soon as they become arbitrary strings things get hairy. Escaping special characters and string encoding quickly bite you in the butt. 

I was generating a large number of bulk data files, in tab separated format, from a Python script. Thinking the task to be straightforward, I started to handle escaping the record separator using Python's `str.replace`. Tab escaping sort of worked, but then I had UTF-8 encoded strings. These strings are a pain to use `str.join` on and then write to an output file. Pretty much every data file generated would have some kind of import error within the first 100 records.

Too bad I didn't have a magic tool that knew how to write CSV files and deal with all the escaping issues.

Oh wait. I'm using Python. Batteries Included.

Busted out the [`csv` module][3]. Just picked apart my tweet data structure into a tuple, along with the tweet JSON source text. The Python documentation has a convenient example of how to handle the UTF-8 encoding. The ancient, Python 2.3 born, `csv` module magically handles all the separator and terminator escaping. The `csv.Writer.writerow` method had no problems writing out a mix of ASCII and Unicode data. And  Postgres happily slurped in every data file generated. I'm well on my way to ingesting multiple millions of tweet instances into a table that has 10+ fields.

The moral of the story? If you want to fast bulkload data into Postgres, find a `csv` compliant library and have it write your rows for you.

**Bonus hint**: If you've got geospatial data as well, maybe you're using PostGIS, grab the `shapely` module and get familiar with the [`wkt` attribute][4] of the shape objects. While the PostGIS documentation says WKT is an acceptable load form, I found that EWKT, essentially adding an SRID, was the only way to get a shape loaded. Assuming you have an established SRID this is a piece of cake.

[1]: http://www.postgresql.org/docs/9.1/static/sql-copy.html
[2]: http://en.wikipedia.org/wiki/Comma-separated_values
[3]: http://docs.python.org/library/csv.html
[4]: http://gispython.org/shapely/docs/1.2/manual.html#well-known-formats