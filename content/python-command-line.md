Title: Python Command Line
Date: 2011-10-13 20:55
Author: crossjam
Category: Uncategorized
Slug: python-command-line
Status: published

<img src="http://crossjam.net/wp/mpr/wp-content/uploads/2011/08/python-logo.gif" alt="Python logo" border="0" width="211" height="71" align="left" style="margin: 10px;" /> Intermittently over the past few years, I've been writing various command line apps in Python. Things like [`split`][4], but with a little more complexity and in a higher level language. 

I've often felt I wasn't quite writing these in a Pythonic fashion. I'd stashed away Guido van Rossum's BDFL blessed [idiom for main][2], but never really put it to use.

Steve Lott has a much better and simpler style of [writing Python main functions][1], that seems more easy to ingest and adopt. He even includes a nice example of how to tie option parsing into logging.

Now it would be great if someone could come up with a cookbook for using the [`argparse` module][3].

[1]: http://slott-softwarearchitect.blogspot.com/2011/10/command-line-applications.html
[2]: http://metalinguist.wordpress.com/2008/02/13/a-different-way-to-main/
[3]: http://docs.python.org/dev/library/argparse.html
[4]: http://crossjam.net/wp/mpr/2011/10/unix-split/