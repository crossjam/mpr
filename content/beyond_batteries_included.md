Title: Beyond Batteries Included
Date: 2009-03-29 16:04
Author: crossjam
Category: Uncategorized
Slug: beyond_batteries_included
Status: published

[<img src="http://crossjam.net/mpr/media/python-logo.gif" alt="python-logo.gif" border="0" width="211" height="71" align="left" style="margin: 10px;" />](http://www.python.org/) [Python](http://www.python.org/) is my current favorite programming language. I don't switch favorites often, but I have an appreciation for many other languages. Heck,  as an undergraduate I actually wrote code on [TI Explorer](http://en.wikipedia.org/wiki/TI_Explorer) Lisp machines.

One of the Python community's mantras is "batteries included." There's a belief that any decent programmer should be able to build fairly sophisticated applications with the stock Python interpreter. Translation, [a large standard library](http://docs.python.org/modindex.html).

Even so, over the years I've found myself installing a bunch of different 3rd party libraries every time I go through a new Python implementation. I've had to do a few of these over the last couple of days. A core set of post-"batteries" essentials have coaleseced. Here they are in no particular order:

* [Numpy](http://numpy.scipy.org/), for array and matrix operations

* [Scipy](http://www.scipy.org/), which includes Numpy, for advanced matrix operations and signal processing

* [lxml](http://codespeak.net/lxml/), for high speed, standards conformant XML processing using the Python-centric [ElementTree API](http://effbot.org/zone/element-index.htm)

* PIL, the [Python Imaging Library](http://www.pythonware.com/products/pil/), for munging images of all formats

* [networkx](http://networkx.lanl.gov/) to conduct various network/graph generation and processing experiments

* The [Universal Feed Parser](http://www.feedparser.org/) since you never know when you need to slurp down and process an RSS or Atom feed

* [virtualenv](http://pypi.python.org/pypi/virtualenv) to easily create customized, isolated versions of a stock Python intepreter

*Python logo cribbed from the [Python](http://www.python.org/) website, copyright the [Python Software Foundation](http://www.python.org/psf).*

