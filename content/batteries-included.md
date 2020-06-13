Title: Batteries Included
Date: 2011-11-11 22:08
Author: crossjam
Category: Uncategorized
Slug: batteries-included
Status: published

<img src="http://crossjam.net/wp/mpr/wp-content/uploads/2011/08/python-logo.gif" alt="Python logo" border="0" width="211" height="71" align="right" style="margin: 10px;" /> At work, I was thinking up a Python script to stream through a bunch of compressed text files. I was starting to devise the logic to run through a list of filenames and present it as one input stream, when I thought *"maybe There's One Obvious Way To Do It already"*. 

A little Googling and voila! Python's [`fileinput` module][1]. Does exactly what I need it to do, right down to being able to detect and decompress `gzip` compressed files. Even better Doug Hellmann has done a Python Module of the Week [(PyMOTW) entry][2] for `fileinput`, meaning there's clear usage examples on top of the excellent documentation.

I had a script to cleanly zip through a 100+ Mb of compressed data in under a hour. Python, it's a beautiful thing.

[1]: http://docs.python.org/library/fileinput.html
[2]: http://www.doughellmann.com/PyMOTW/fileinput/