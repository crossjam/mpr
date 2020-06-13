Title: Python XML Processing
Date: 2013-05-13 21:22
Author: crossjam
Category: Uncategorized
Slug: python-xml-processing
Status: published

The [Discogs.com][1] data is in some humongous XML files, which is a little unruly for many data hacking tasks. Python has some great XML processing modules, but it’s always good to have a little guidance. Enter this oldie but goodie from Eli Bendersky on [*Processing XML in Python with ElementTree*][2]:
> As I mentioned in the beginning of this article, XML documents tend to get huge and libraries that read them wholly into memory may have a problem when parsing such documents is required. This is one of the reasons to use the SAX API as an alternative to DOM.

> We’ve just learned how to use ET to easily read XML into a in-memory tree and manipulate it. But doesn’t it suffer from the same memory hogging problem as DOM when parsing huge documents? Yes, it does. This is why the package provides a special tool for SAX-like, on the fly parsing of XML. This tool is iterparse.

> I will now use a complete example to demonstrate both how iterparse may be used, and also measure how it fares against standard tree parsing.

If I was going to update Bendersky’s post, I wouldn’t change much, other than to mention [lxml and lxml.etree][3] which provide high-performance streaming XML processing.

[1]: http://www.discogs.com/data/
[2]: http://eli.thegreenplace.net/2012/03/15/processing-xml-in-python-with-elementtree/
[3]: http://lxml.de/tutorial.html