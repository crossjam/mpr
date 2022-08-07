Title: Mopidy Mystery
Date: 2022-07-22
Author: C. Ross Jam
Status: published

I was hoping to fool around with [Mopidy][1] as an audio playback
engine because it’s written in Python and supports the MPD protocol
according to the [documentation][2]. When I went to install it using
`homebrew` on my MacBook Air, the latest version had problems with
its plugins, wherein I discovered there was already [an outstanding
issue][3] on GitHub. Unfortunately, a solution didn’t look promising,
but at least I chimed in my interest.

So off I go, working on other things and forgetting about the
problem. Lo and behold, [another user reports][4] the real source of
the issue and a convenient fix. With an `export
GST_PLUGIN_PATH=/opt/homebrew/lib/gstreamer-1.0/` now my Mopidy server
works perfectly and can playback audio on my MacBook. Score one for
just registering interest on GitHub!!

Mystery solved. Onwards to implementing my own database driven,
dynamically created playlists.


[1]: https://mopidy.com/
[2]: https://docs.mopidy.com/en/latest/
[3]: https://github.com/mopidy/homebrew-mopidy/issues/41
[4]: https://github.com/mopidy/homebrew-mopidy/issues/41#issuecomment-1191589325
