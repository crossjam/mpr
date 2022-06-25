Title: Discogs Data CSV
Author: C. Ross Jam
Status: published

So I took the [`discogs-xml2db`][1] tool and ran it against the
[Discogs Data, May 2022 release][2]. I got back 8.1 Gb, 😱, of csv data to
ingest into PostgreSQL. I’ve done it for previous months and it’s
ingested just fine, but there’s some interesting exploration that can
be done with the csv data, before, and after ingest. But I’m gonna
need a few tools:

* [VisiData][3], _"VisiData is an interactive multitool for tabular data."_
* [xsv][4], _"xsv is a command line program for indexing, slicing, analyzing, splitting and joining CSV files. "_
* [Data Fluent for PostgreSQL][5], _"Build a better understanding of your data in PostgreSQL."_

[1]: https://github.com/philipmat/discogs-xml2db
[2]: http://data.discogs.com/?prefix=data/2022/
[3]: https://www.visidata.org/
[4]: https://github.com/BurntSushi/xsv
[5]: https://tech.marksblogg.com/data-fluent-for-postgresql.html
