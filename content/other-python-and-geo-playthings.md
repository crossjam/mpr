Title: Other Python and Geo Playthings
Date: 2013-02-07 21:58
Author: crossjam
Category: Uncategorized
Slug: other-python-and-geo-playthings
Status: published

Some other things that caught my fancy recently

[Geobases][1]
> This project provides tools to play with geographical data. It also works with non-geographical data, except for map visualizations :).

[Glue][2]
> Glue is a Python library to explore relationships within and among related datasets.

On [the current state of reverse geocoding][3]:
> At Flickr we spent a while working on turning the point where a photo was set on map (or whose GPS coordinates were shoved into the EXIF) into a place. The work of reverse geocoding is about taking a point, and finding out which polygon its in. This is a well solved problem. With two caveats:

> 1. places don’t have neat boundaries, but overlap all over each other. And people disagree about the overlaps

> 2. even if places had neat boundaries, and people agreed on them, availability of information about those boundaries is variable at best.

Once I made [a request for a pure geo indexing capability][4]. Ask and [ye shall receive][5].
> A Java reverse geocoder that uses Geotools and JTS to index Flickr Shapefiles to map (latitude, longitude) to WOEID.

> The code has no external server dependencies and runs in memory. You may have to specify a larger max heap size if you use the largest files (e.g. the localities dataset uses around 450Mb on my Mac).

[1]: https://github.com/opentraveldata/geobases
[2]: http://www.glueviz.org/en/latest/
[3]: http://laughingmeme.org/2013/02/03/are-you-here-a-feature-on-the-side/
[4]: http://crossjam.net/wp/mpr/2012/04/pure-geoindexing/
[5]: https://github.com/mattb/flickrgeocoder-java