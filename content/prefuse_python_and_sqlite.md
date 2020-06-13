Title: Prefuse, Python and Sqlite
Date: 2010-06-23 23:01
Author: crossjam
Category: Uncategorized
Slug: prefuse_python_and_sqlite
Status: published

[<img src="http://crossjam.net/mpr/media/Prefuse Logo.gif" alt="Prefuse Logo.gif" border="0" width="185" height="43" align="left" style="margin: 10px;" />][1] In a previous life, I was [early on the bandwagon][2] of [prefuse][1], an innovative information visualization toolkit implemented in Java. A key element was the programming model that systematically [organized the transformation of data][3] into graphical elements. Subsequent work identified and extracted [information visualization design patterns][4], including the usage of structured tables and SQL-like query facilities.

[<img src="http://crossjam.net/mpr/media/SQLite Logo.gif" alt="SQLite Logo.gif" border="0" width="125" height="37" align="left" style="margin: 10px;" />][5]

While it would be hard to top the quality of prefuse as a Java toolkit, I've always wondered what a Python adaptation would look like. The graphic primitives aren't that big a deal, and Python is rich enough to easily emulate any of prefuse's control flow mechanisms. The structured tables and SQL facilities always bugged me though, because it seemed to me that you could easily use an embedded relational engine, like [SQLite][5], to support those capabilities. The embedded DB could provide a richer query language than prefuse's, higher performance querying, and persistent storage allowing you to work with bigger datasets.

I've been mentally kicking this issue around and digging into the prefuse source code to see what exactly was implemented. I think I've got a relatively straightforward way to emulate prefuse's table facilities in a stock Python install. This is starting to feel like a worthy side project.

[<img src="http://crossjam.net/mpr/media/python-logo.gif" alt="python-logo.gif" border="0" width="211" height="71" align="right" style="margin: 10px;" />](http://www.python.org) The result wouldn't be completely superfluous as I think there are some unexplored issues in terms of the prefuse model and interaction. Also, the combo with [Python](http://www.python.org/) might lead to some increased flexibility due to the language change, and a higher level of accessibility due to an interactive command loop and Python's batteries included. Of course you'd lose the ability to generate applets, but frankly that's probably a small loss.

[1]: http://prefuse.org/

[2]: http://crossjam.net/nmh/archives/000646.html

[3]: http://vis.berkeley.edu/papers/prefuse/

[4]: http://vis.berkeley.edu/papers/infovis_design_patterns/

[5]: http://www.sqlite.org/

