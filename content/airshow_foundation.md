Title: Airshow as a Foundation?
Date: 2024-12-13
Status: published
Author: crossjam

I mentioned [Airshow][1] as part of a foundation for
[`retrocast`][4]. It’s a podcast player from
[Feedbin.com](https://feedbin.com). The app can use Feedbin as a synch
mechanism. In principle, the podcast feeds of Airshow could be a
special part of the [Feedbin API][3], unifying RSS feeds and podcasts
within one service. Would be convenient for development purposes.

Unfortunately, it’s not looking particularly positive for [a distinct
Airshow API][2] segment of the feedbin API. There’s probably a few
ways to kludge it though, possibly by doing a podcast search on the
feed source url and eventually tagging podcasts with a specific
label. Might be a nudge to investigate a hackable open source feed
aggregator.

Alas, the Airshow app is driving me up a wall with a hyper sensitive
touch interface on iOS.

[1]: https://airshow.fm/
[2]: https://github.com/feedbin/feedbin-api/issues/64
[3]: https://github.com/feedbin/feedbin-api
[4]: {filename}/retrocast.md
