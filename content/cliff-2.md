Title: cliff
Date: 2012-07-20 18:46
Author: crossjam
Category: Uncategorized
Slug: cliff-2
Status: published

In the past I’ve written my own Python command line processing module to emulate what I call command shell frameworks ala git, Mercurial, and Subversion. Sucked.

I tried [the `pyCLI` module][1] but it didn’t quite work for me.

After a few hitches, [Doug Hellmann’s `cliff` module][2] did the trick. Need a longer test drive, but so far it’s been highly useful. I don’t quite love the use of `distribute` hooks but I can live with it until I find a better solution. The baked in command REPL is a nice to have. 

Using `cliff` has been a good way to paper over some fairly complex processing with a power user grade UI. Also quite easy to add new features with quick turnaround.

[1]: http://packages.python.org/pyCLI/
[2]: http://cliff.readthedocs.org/en/latest/