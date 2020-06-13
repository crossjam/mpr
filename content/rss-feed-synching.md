Title: RSS Feed Synching
Date: 2011-12-12 23:44
Author: crossjam
Category: Uncategorized
Slug: rss-feed-synching
Status: published
Attachments: wp/mpr/wp-content/uploads/2011/12/RSS-Feed-Icon-64x64.png

<img src="http://crossjam.net/wp/mpr/wp-content/uploads/2011/12/RSS-Feed-Icon-64x64.png" alt="RSS Feed Icon 64x64" border="0" width="64" height="64" align="left" style="margin: 10px;" /> A while ago there was a lot of [consternation][4] when Google Reader [changed its user interface][5]. Along with that [Google axed a number of projects][6]. Seeing as it's not obvious if or how Google Reader generates revenue, people were duly concerned.

The big issue is that Google Reader seems to have become the de facto infrastructure for synching reading lists across devices. Longtime (but now ex) developer of NetNewsWire, [Brent Simmons](http://inessential.com) clearly chronicles [the issue with Google Reader and synching][2]. Based upon his experience he drills down into some of the [key RSS synching technical challenges][1].

As a computer scientist, I understand the issues. But it seems to me that this is such a classic distributed systems problem, there has to be a clean solution already. To my eye [distributed version control systems][3], like [git](http://git-scm.com/), have most of the answer. Many differences between distributed files are easily handled, and conflicts have to be resolved by a human. Now obviously that would be a pain for an RSS reader but maybe a few simple resolution policies, designated by a human, could do the trick.

Just thinking out loud, because I heart RSS and feed reading.

[1]: http://inessential.com/2011/10/25/why_just_store_the_app_data_on_dropbo
[2]: http://inessential.com/2011/10/24/google_reader_and_mac_ios_rss_readers_th
[3]: http://en.wikipedia.org/wiki/Distributed_Version_Control_System
[4]: http://massless.org/?p=174
[5]: http://fury.com/2011/11/my-offer-to-google-reader/
[6]: http://googleblog.blogspot.com/2011/11/more-spring-cleaning-out-of-season.html