Title: A Minor Mystery Solved
Date: 2009-12-14 22:10
Author: crossjam
Category: Uncategorized
Slug: a_minor_mystery_solved
Status: published

[<img src="http://crossjam.net/mpr/media/xemacs logo.gif" alt="xemacs logo.gif" border="0" width="200" height="75" align="left" style="margin: 10px;" />][1] I have a lot of hand built XEmacs installations across my personal and work machines. In recent builds there's been this really irritating error on XEmacs boot. I would always get this message about "`symbol's value as variable is void: default-menubar`". The error really didn't break anything, it was just supremely annoying.

Well a few weeks ago, I finally got around to digging in and debugging this little critter. Pernicious little devil, but I finally tracked it to XEmacs' initial package load.

Then by brute-force process of elimination I chased it down to the `guided-tour` package. The package was trying to hook into a menubar system that didn't exist since I compile my XEmacsen for console mode only.

And here's the fix:<br/>

`(setq guided-tour-insinuate-menubar nil)

`

Dump it in your `init.el` and kill the irritation.

[1]: http://xemacs.org/

