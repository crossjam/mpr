Title: Hadoop Munging OSM
Date: 2013-02-21 20:37
Author: crossjam
Category: Uncategorized
Slug: hadoop-munging-osm
Status: published

Michal Migurski crisply documents his [Hadoop/Elastic Map Reduce process for working with Open Street Map data][1]:
> Usable line generalization for OSM roads and routes has been a hobby project of mine for several years now, since I argued for it at the first U.S. State of the Map conference in Atlanta, 2010. I’ve finally put the last piece of this project in place with the use of Hadoop to parallelize the geometry processing.

> I’ve learned a lot about moving geographic data between Postgres and Hadoop. The result is available at Streets and Routes. 

> …

> The end result is something I’m super happy about: a complete worldwide dataset of simplified roads and routes that’s suitable for high-quality labels and route shields. 

A couple of punch lines to that final statement. First, Migurski was a relative newbie to Hadoop, and didn’t use anything more sophisticated than Hadoop Streaming and straight Python with [Shapely][2]. Second, his *expensive* run cost him $9.40 and 7 hours of waiting.

[1]: http://mike.teczno.com/notes/elephants-osm-hadoop.html
[2]: http://toblerity.github.com/shapely/