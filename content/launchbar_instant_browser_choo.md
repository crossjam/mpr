Title: LaunchBar Instant Browser Choosing
Date: 2010-05-01 16:43
Author: crossjam
Category: Uncategorized
Slug: launchbar_instant_browser_choo
Status: published

[<img src="http://crossjam.net/mpr/media/Launchbar Logo.jpg" alt="Launchbar Logo.jpg" border="0" width="64" height="64" align="left" style="margin: 10px;" />][1] With [my increased usage][3] of Chrome, I send URLs between browsers more frequently. This just at the time my trial license of [Choosy][2] has expired.

The thought occurred to me that maybe this is a problem that [LaunchBar][1] could solve, if I just dug in a little bit. Turns out LaunchBar is easily up to the task. Here's the sequence:

* `Copy` the URL to the clipboard (Control-click on the link in the browser)

* `Option-Command-\ `, should bring up the clipboard history with the copied URL first at the top of the list (Key sequence may have been customized in your LaunchBar, check under Preferences > Clipboard)

* `Tab`, browser selections come up

* `Return`, opens in the selected library

One more gesture, link to clipboard, than Choosy, but it's a start.

I'm also thinking there's probably a way to use scripting to send the currently selected URL to LaunchBar's "Open Location" action. The key part is to get the URL to a point where you can actually select from the various installed browsers. Turns out LaunchBar's provision for browser selection (you can just Tab when a URL is the current target object), works pretty well. And it's handy all throughout LaunchBar.

[1]: http://www.obdev.at/products/launchbar/index.html
[2]: http://www.choosyosx.com/
[3]: http://crossjam.net/wp/mpr/2010/04/starting_to_enjoy_chrome/

