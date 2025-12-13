---
title: "A Lesson From 90,000 Scrobbles"
date: 2025-12-13 20:00
author: "C. Ross Jam"
---

![last.fm 90,000 Scrobbles Screen
Capture]({static}/images/ninety_thousand_scrobbles.png)

I recently reached [90,000 scrobbles][2] recorded on last.fm! That
spans a little over 20 years 😲, roughly 4,500 per year, approximately
12 tracks a day. Depending upon the style of music, that’s easily 1
complete CD / album / mix a day, every day, for 20 years.

Let’s dig in a bit ...

<!-- PELICAN_END_SUMMARY --> 

Okay, observant folks will notice a few gap years. Still, it’s
impressive that a [Web 2.0][6] poster child service has managed to
stick around this long. Using my [scrobbledb][3] side project, I was
able to download all 90,000 to a local sqlite db (27 MB in size if
you’re curious).

The key reason I was able to do this was that last.fm, while remaining
a going concern for 20+ years, has also managed to maintain it’s API
for all that time. But the [last.fm API][1] does have a design point
that feels curious. I did some minimal exploration of the data in the
terminal console. And discovered the API eschews user accessible
unique IDs in the endpoints!

If you take a peek at the docs for the [_track.getInfo_][4] endpoint,
the query is driven by the required _artist_ name and _track_ name
arguments. [_user.getRecentTracks_][5] is the primary way to access a
user’s historical scrobble record. The API response doesn’t include a
UID for the scrobbles. Based upon some sleuthing on my profile Web
pages, I’m pretty sure a UID exists, but it’s definitely not meant to
be available to end users. Other endpoints behave similarly. 

This could be an artifact of when the API was
developed. Alternatively, I could see it being a conscious design
choice. Scrobbles are self-reported data from often dubious sources:
dodgy file metadata, janky scrobbling clients, iffy app plugins. Not
attempting to consistently resolve that data might be a prudent design
choice that would not surprise me.

Apparently, last.fm does integrate [musicbrainz][6] data if entity
information can be resolved to an entry within that database, so some
of the data I downloaded includes MBID identifiers for tracks and
albums. Time to do some exploratory data analysis and find out what
the percentage covered.

My scrobble data might be out of the norm if not a full on outlier. I
listen to **a lot** of DJ mixes. There are lots of remixes, renames,
alternative versions, and DJ private white label releases with little
public information.  Track titles, albums, and artists are often quite
mangled. Playlists on Apple Music from live sets, which I’ve been
bingeing, exacerbate the issue.

Ultimately, I’d like to build an interactive, AI-driven, exploration
app on top of this data. Looks like there might be some data
integration challenges to address first. Might be a job for vector
search. 


[1]: https://www.last.fm/api
[2]: https://www.last.fm/user/crossjam/library
[3]: https://github.com/crossjam/scrobbledb
[4]: https://www.last.fm/api/show/track.getInfo
[5]: https://www.last.fm/api/show/user.getRecentTracks
[6]: https://en.wikipedia.org/wiki/Web_2.0
