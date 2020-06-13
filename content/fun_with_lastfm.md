Title: Fun With last.fm
Date: 2009-03-13 22:09
Author: crossjam
Category: Uncategorized
Slug: fun_with_lastfm
Status: published

[<img src="http://crossjam.net/mpr/media/Last.fm_Logo_Red.jpg" alt="Last.fm_Logo_Red.jpg" border="0" width="200" height="60" align="left" style="margin: 10px;" />](http://last.fm) Since I started listening to more music through iTunes on my Macbook and with my iPod Mini, I decided to reconnect with [Audioscrobbler](http://www.audioscrobbler.net) or technically [last.fm](http://last.fm).  I had used the old Audioscrobbler for a short while back in 2005, but they have since been absorbed and redeployed as the [last.fm web services API](http://www.last.fm/api).

<img src="http://crossjam.net/mpr/media/lastfmlogo.jpg" alt="lastfmlogo.jpg" border="0" width="48" height="47" align="right" style="margin: 10px;" /> Audioscrobbler plugs in to your media player, scrobbles your tracks a.k.a records what you listen to, and then uploads that data to last.fm. From there, last.fm taps you in to a social network of other digital music listeners. This has turned out be surprisingly interesting, as there are connections to playlists from similar users, videos for many songs that I didn't think had one, and even free music.

Even better, I've found that my jury-rigged home MP3 jukebox can be hooked in as well. I've put a bunch of MP3s on an old Linux box. I run [MPD](http://mpd.wikia.com/wiki/Music_Player_Daemon_Wiki) as a remotely controllable, media player. MPD feeds an [Icecast](http://www.icecast.org/) server which I can securely connect to over SSH tunnels. Comes in handy when trying to listen from work.

Just to be a completist, since I do a lot of listening in the office, I wanted tracks played through the above concoction to be scrobbled as well. MPD doesn't directly support scrobbling, but there are a handful of supporting applications that listen to MPD's playlist and scrobble the results. At first I gave [mpdscribble](http://mpd.wikia.com/wiki/Client:Mpdscribble) a shot, thinking a stable C application would be pretty reliable. For whatever reason, mpdscribble often timed out uploading scrobble data. I switched to the Python based [lastfmsubmitd](http://www.red-bean.com/decklin/lastfmsubmitd/) and now things work great.

Finally lastfmsubmitd is a nice elegant piece of code that relies on basic UNIX principles to get the job done. It cleanly forks daemon processes for the MPD listener and the last.fm submitter, and uses the filesystem to record its data. Plus it logs nicely and feels very Pythonic. Excellent job!!

I'll post more later specifically about the last.fm experience.

