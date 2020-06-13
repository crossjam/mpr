Title: Rendering The World
Date: 2012-05-05 14:05
Author: crossjam
Category: Uncategorized
Slug: rendering-the-world
Status: published
Attachments: wp/mpr/wp-content/uploads/2012/05/MapBox-Logo.png

[<img src="http://crossjam.net/wp/mpr/wp-content/uploads/2012/05/MapBox-Logo.png" alt="MapBox Logo" border="0" width="222" height="55" align="right" style="margin: 10px;" />](http://mapbox.com/) Interesting post by Young Hahn of MapBox on [*“Rendering The World”*][1]. The problem Hahn discusses is the rendering of map tiles at high zoom levels for the entire world. The obvious and straightforward way quickly becomes unscalable for the zoom levels MapBox wants to achieve due to exponential, recursive explosion. 

Turns out the actual space of unique tiles, by content, is orders of magnitude smaller than the number of tiles needed a.k.a. there’s a high level of redundancy. For example, many tiles at any zoom level simply represent all blue patches of water. Capturing and exploiting this redundancy is the key to getting scalable performance.

This page had been sitting in my Chrome tabs for quite some time, but it was well worth the read once I got around to it.

[1]: http://mapbox.com/blog/rendering-the-world/