Title: Pure GeoIndexing
Date: 2012-04-14 21:36
Author: crossjam
Category: Uncategorized
Slug: pure-geoindexing
Status: published

LazyWeb I beseech you.

I could use a pure geographic bounding box library or server that does for geoqueries what [Sphinx][2] does for full text search. Maybe a bit prickly, idiosyncratically extensible, horizontally scalable, and **fast as hell by default**. Throw in uniquely identified polygons, take queries for all intersections or all contains, return ids. That is all. No transformations or manipulations, just insert, delete, index and answer queries. 

[PostGIS][1] is great, but the performance of the geographic indexing seems opaque and hard to optimize, at least to this simple soul.

[1]: http://postgis.refractions.net/
[2]: http://sphinxsearch.com/