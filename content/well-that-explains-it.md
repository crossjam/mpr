Title: Well That Explains It
Date: 2015-01-18 13:35
Author: crossjam
Category: Uncategorized
Slug: well-that-explains-it
Status: published

I’ve been seeing some weird host naming issues on my Mac OS X machine for work. Thought it was an honest to gosh conflict with another machine but it turns out [there’s glitchiness in Apple’s latest DNS servers][1]:

> Duplicate machine names. We use an old Mac named "nirrti" as a file- and iTunes server. In the pre-10.10 days, once in a blue moon nirrti would rename herself to "nirrti (2)", presumably because it looked like another machine was already using the name "nirrti". Under 10.10, this now happens a lot, sometimes getting all the way to nirrti (7). Changing back the computer name in the Sharing pane of the System Preferences usually doesn't take. Apart from looking bad, this also makes opening network connections and playing iTunes content harder, as you need to connect to the right version of the name or nothing happens.

Good to know, but I wouldn’t go so far as to attempt the modifications described in the article. Seems like a recipe for later pain on further application and operating system upgrades.

[1]: http://arstechnica.com/apple/2015/01/why-dns-in-os-x-10-10-is-broken-and-what-you-can-do-to-fix-it/