Title: LaunchBar, GDesktop, & Python
Date: 2009-02-16 22:57
Author: crossjam
Category: Uncategorized
Slug: launchbar_gdesktop_python
Status: published

[<img src="http://crossjam.net/mpr/media/Launchbar Logo.jpg" alt="Launchbar Logo.jpg" border="0" width="64" height="64" align="left" style="margin: 10px;" />][1] I'm getting really hooked on [LaunchBar][1]. So much so that I want to push as many keyboard commands as possible through the versatile launcher.

[1]: http://www.obdev.at/products/launchbar

[Google Desktop](http://desktop.google.com/) was bollocksing up things though with its too similar keyboard trigger. Not to mention the goofiness of showing Web results ahead of desktop results. When I go to my desktop search engine I'm looking for desktop results.

At first I thought a simple LaunchBar search template would do the trick except for a couple of issues:

1. Google Desktop can be reached in a browser through a URL. Unfortunately [the base of this URL](http://code.google.com/apis/desktop/docs/queryapi.html#httpxml) has an embedded token whose creation isn't documented anywhere.

2. Firefox is completely braindead when it comes to the Apple OpenScripting Architecture.

3. Getting LaunchBar to recognize your custom scripts and actions is a little tricky.

Mac OS X command line to the rescue.


<!--more-->
The Google Desktop url can be pulled out of Apple's system configuration variables using `defaults`. Firefox can be told to launch a URL using the `open` command. A [Python](http://www.python.org) script ties it all together by running the command to get the url, escaping the query args, creating the full url, and launching Firefox. Plop the script into `~/Library/Application Support/LaunchBar/Actions` and I'm in hotkey heaven.

It's not the fastest thing in the world, but it gets the right results in the right place. Not bad for a 1 hour hack, although it took a couple of hours of research. Here's the script:

#!/usr/bin/python

import urllib

import subprocess

DEFAULTS_CMD =

'defaults read com.google.Desktop.WebServer search_url'

def main(qargs):

output = subprocess.Popen(DEFAULTS_CMD, shell=True,

stdout=subprocess.PIPE).stdout

gdesktop_url = output.readline().strip()

url_txt = gdesktop_url + "&q=" + \

urllib.quote_plus(" ".join(args))

subprocess.check_call(["open", url_txt])

if __name__ == '__main__':

from optparse import OptionParser

op = OptionParser()

options, args = op.parse_args()

main(args)

Now to write that [Discogs.Com](http://www.discogs.com) search template for LaunchBar.

