Title: Discogs and Data
Author: crossjam
Category: discogs
Status: published
Date: 2021-09-20

[For the longest time][5], I’ve just been piling up [data from Discogs.com][1]
and not really doing anything with it. Finally, I have a motivating
project.

The fine folks at [London’s Fabric nightclub][7] have two great series of
DJ mix releases, [Fabric][3] and [FabricLive][2]. Recently I made a
bulk purchase of digital versions of 20 mixes. They arrived as .wav
files with no metadata attached (that I can tell). Adding all the
track metadata is something a computer should do, not a human. No
problem, all of that data should be in the Discogs data. I’d also like
to create playlists or a playlist DB to start noodling around with
[MPD][4] as a playlist shuffling jukebox. (_Why does the world hate
playlists so much?_).

So of course this means lots of data munging, wrangling, and
management. Which is totally fine. I need some data side projects to
help build a data portfolio.

_Link parkin’ [discogs-xml2db v2][6] as the way to get the Discogs data
into a PosgreSQL db for querying._


[1]: http://data.discogs.com/
[2]: https://www.discogs.com/label/348990-FabricLive
[3]: https://www.discogs.com/label/1115423-Fabric-3
[4]: https://www.musicpd.org/
[5]: {filename}/discogs-data-micro-redux.md
[6]: https://github.com/philipmat/discogs-xml2db
[7]: https://fabriclondon.com/
