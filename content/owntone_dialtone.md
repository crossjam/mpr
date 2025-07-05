Title: Owntone Dialtone
Date: 2025-07-05
Author: C. Ross Jam
Status: published

For the longest time, I’ve been dreaming of a hackable solution to
drive my multiple Sonos speaker setup. A while back, I thought I could
cobble something together based upon [Music Player Daemon
(mpd)][1]. Didn’t really have time to dig deep into setting things
up. The other bit is that getting Sonos to pick up streams from mpd
seemed a bit kludgey.

I kept plugging away doing background research and discovered
[OwnTone][2]

> [OwnTone][3] is a media server that lets you play audio sources such
> as local files, Spotify, pipe input or internet radio to AirPlay 1
> and 2 receivers, Chromecast receivers, Roku Soundbridge, a browser
> or the server’s own sound system. Or you can listen to your music
> via any client that supports mp3 streaming.

> You control the server via a web interface, Apple Remote, an Android
> remote (e.g. Retune), an MPD client, json API or DACP. 

> OwnTone also serves local files via the Digital Audio Access
> Protocol (DAAP) to iTunes (Windows), Apple Music (macOS) and
> Rhythmbox (Linux), and via the Roku Server Protocol (RSP) to Roku
> devices. 

Did some holiday hunkering down and got an OwnTone server deployed on
my homeLAN. Had some challenges doing a build under Linux on a mini-PC
but I found [a community package][4] that worked out well. _Turns out
I had some Linuxbrew stuff causing conflicts._ After that it was a
little bit of firewall configuration aaaand ...

![crossjam’s OwnTone server dashboard]({static}/images/owntone-screencap.png)

The frontend is nice while OwnTone also provides an mpd facade that’s
controllable with mpd clients like [mpc][6]. There’s also a good
looking [JSON API][7]. Plus it supports LastFM integration although
I’ll keep on with my [soco-scribbler][8] work.  Even more beautiful is the
fact that it’s reachable over my TailScale network. All in all, a side
project hacker’s delight.

Some burn-in needs to happen with a full play list run, but this is
promising. Given the protocols that OwnTone is designed to service
([DAAP][5] and AirPlay), it shouldn’t be a surprise it does an excellent
job of finding my AirPlay 2 speakers as output targets. I also have a
pair of Homepod Minis that are only lightly used. Maybe this will give
them renewed life.


[1]: https://www.musicpd.org
[2]: https://owntone.github.io/owntone-server
[3]: https://github.com/owntone/owntone-server
[4]: https://www.sudo.is/docs/builds/owntone/
[5]: https://en.wikipedia.org/wiki/Digital_Audio_Access_Protocol
[6]: https://www.musicpd.org/doc/mpc/html/
[7]: https://owntone.github.io/owntone-server/json-api/
[8]: https://github.com/crossjam/soco-scribbler
