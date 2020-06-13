Title: PostGIS Index Selectivity
Date: 2012-02-22 21:42
Author: crossjam
Category: Uncategorized
Slug: postgis-index-selectivity
Status: published

[<img src="http://crossjam.net/wp/mpr/wp-content/uploads/2011/10/PostGIS-Logo-Small.png" alt="PostGIS Logo Small" border="0" width="120" height="120" align="left" style="margin: 10px;" />][2] Maybe I'm doing something wrong, but I find I'm fighting PostGIS's query planner way too often. The problem is that I have a table with a lot of records, the planner incorrectly thinks a geospatial filter will eliminate a lot of the rows, and then decides to do an index scan across the entire table. This happens even when I pair the geo filter with a highly selective date range query. Seems like [a known problem with GIST indexes][1].

Reworking the query to use a subselect, wrapping the geo select around the date filtered select, seems to do the trick. But when you're working against the system either you're doing something the system wasn't designed to do, or you don't understand the system. Or both.

More investigation needed.

[1]: http://forums.postgresql.com.au/viewtopic.php?f=30&t=104461
[2]: http://www.postgis.org/