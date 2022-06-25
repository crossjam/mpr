Title: Messin' With Music.app Data
Date: 2022-06-13
Author: C. Ross Jam
Status: published

I wanted to start liberating my OS X Music.app data, noticing that you
can "Export... > iTunes Libray" to spit out XML to the file
system. Next stop was parsing the XML. Hang on, there’s gotta already
be a Python module(s) for that right?

[itunesLibrary][1] was the first port of call. It inhaled my 18 MB of
XML library file, but the object interface didn’t click with me. It
was sort of Pythonic dictionary like, but not quite.

Turns out the exported XML is just an Apple property list ([plist][3])
file and there’s [a plist parsing library][2] in the Python standard
library. [libpytunes][4] is a thin wrapper around [plistlib][2]. I
need to give it a longer test drive, but it seems a bit more complete
than itunesLibrary.

Beyond intermittently doing a manual slog through menus, I was hoping
there might be a way to automate this via Apple’s scripting
machinery. [Doug’s Applescripts][6] is the go to in this space, especially
for things related to the OS X Music app.  Apparently, [Doug is not
sanguine][5] on leveraging the XML format or Apple’s replacement:

> So anyway, the XML has finally gone away, effectively, since it is
> no longer automatically exported.

> I've been trying to incorporate the ITLibrary framework into my
> projects whenever I can, especially for apps that need to display
> lots of tracks or playlists (like Media Folder Files Not Added).

> But ITLibrary was apparently last updated for macOS 10.13. And now
> that iTunes has been split out into the media apps, it's usefulness
> over the XML file has not been improved.

> (And please. Don't let me hear anyone suggest some groovy way of
> exporting the XML automatically. Forget about the XML. Unless it's
> for backups or something.)

And mind, this was in October 2019. I suspect much hasn’t changed
since.

But for me, the XML is enough in the short term. If I ever get working
daily snapshots I’ll be happy. The real fun will begin when
transmogrifying the data into something ingestable into an SQL engine
and thence marrying with Discogs Data. 

_Apropos Elle Driver, "You know I’ve always liked that word
... ’sanguine’ ...  so rarely have an opportunity to use it in a
sentence."_

[1]: https://github.com/scholnicks/itunes-library
[2]: https://docs.python.org/3/library/plistlib.html
[3]: https://fileinfo.com/extension/plist
[4]: https://github.com/liamks/libpytunes
[5]: https://dougscripts.com/itunes/index.php?p=2993
[6]: https://dougscripts.com/itunes/index.php
