Title: FAFO - Fork And Forge On
Date: 2026-08-15
Author: C. Ross Jam
Status: published

I have at least three projects based upon forking an open source repo
and just hacking away, usually with a coding agent.

[SocoScribbler] started out promising, but hasn’t gained much traction
in my coding attention. I think once I make some further progress on
data analysis in [scrobbledb] it’ll get going. I’m also seriously
contemplating ponying up for an Apple Developer account so I can
integrate my Apple Music online library.

[Humble Book ETL][hbetl] I just hacked up today in a couple of hours
using a combination of an [exe.dev] vm and exe’s [shelley]. As a
[HumbleBundle Book Bundle][] book addict, I need a one stop shop for
bundle metadata, especially so I can (coming soon) cross reference
with what I’ve already purchased. [Pedro "Dopeldev"
Gonzales][dopeldev] was the original creator and there’s a [public
facing deployment][humble-book-etl]. I forked his
[repo][dopeldev-humble-bundle], deployed it on my tailnet and
customized the web frontend.

[scrobbledb] is the poster child for what I really wanted to
say. [lastfm-to-sqlite] was a barebones tool to grab LastFM scrobbles
and stuff them into an sqlite db. The repo hasn’t seen a commit in 7
years. I think it’s fair to say I’ve scratched my own itch and pushed
the ball forward into the modern era. A lot of it with the help of
multiple different coding agents.

In all three cases, I detached my forked repo from the GitHub network
since I don’t expect to push my changes upstream. Although I wouldn’t
call these repos abandoned here hasn’t been a lot of action on any of
them recently. Also, I have a very particular and strong opinion on
how I want cli tools to work. I expect most of my commits wouldn’t be
welcome anyway.

Gonzales’ project filled a gap which I was **just** this side of
building something new from scratch involving a bunch of agentic
hoodoo. But with his well executed project, I only needed to fork and
forge on. Vive le software libre!

I’m convinced this will be a recurring pattern for me moving ahead. 

_Also, more to come on [exe.dev] and the delightful kit they’ve put
into the world._


[socoscribbler]: https://github.com/crossjam/soco-scribbler
[scrobbledb]: https://github.com/crossjam/scrobbledb
[hbetl]: https://github.com/crossjam/humble-book-etl
[exe.dev]: https://exe.dev
[shelley]: https://exe.dev/shelley
[humble-book-etl]: https://projects.dopeldev.com/humblebundlespider/
[dopeldev]: https://www.dopeldev.com
[dopeldev-humble-bundle]: https://github.com/dopelDev/humbleBundle
[lastfm-to-sqlite]: https://github.com/jacobian/lastfm-to-sqlite
