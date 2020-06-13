Title: Simple Tools
Date: 2011-11-25 19:00
Author: crossjam
Category: Uncategorized
Slug: simple-tools
Status: published
Attachments: wp/mpr/wp-content/uploads/2011/11/curl-logo.png

[<img src="http://crossjam.net/wp/mpr/wp-content/uploads/2011/11/curl-logo.png" alt="Curl logo" border="0" width="99" height="37" align="left" style="margin: 10px;" />][3] Even though I've been using UNIX for over 20 years, there are some simple, elegant, tools that I'm really now coming to appreciate:

* [`cron` and `crontab`][1] for automatically running things at scheduled times, especially the GNU extension that supports `@reboot` allowing normal users to run scripts at machine startup
* [`logrotate`][2] lets me keep dumping data into a single file, but break it into smaller, more manageable chunks. Combined with `crontab` I can easily collect gigabytes of data in a straightforward manner, but have the results in well organized, compressed multi-megabyte units. That expedition with [Python and `argparse`][4]? That was driven by usage of `logrotate`.
* [`curl`][3] for grabbing anything off the Web. Okay, it's simple and elegant like a Swiss Army Chainsaw, but it always works, never crashes, and can be configured six ways to Sunday.

[1]: http://en.wikipedia.org/wiki/Cron
[2]: http://linuxcommand.org/man_pages/logrotate8.html
[3]: http://curl.haxx.se/
[4]: http://crossjam.net/wp/mpr/2011/11/python-argparse-append/