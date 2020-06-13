Title: pluggin’ away
Date: 2013-01-10 19:44
Author: crossjam
Category: Uncategorized
Slug: pluggin-away
Status: published

As I get more experience building “command shells” in Python, I’ve become interested in making them easily extensible. In the same way [cliff][2] is my [goto command line building toolkit][3] maybe [stevedore][1] can plug this hole:
> Python makes loading code dynamically easy, allowing you to configure
and extend your application by discovering and loading extensions
("plugins") at runtime. Many applications implement their own
library for doing this, using __import__ or
importlib. stevedore avoids creating yet another extension
mechanism by building on top of setuptools entry points. The code
for managing entry points tends to be repetitive, though, so stevedore
provides manager classes for implementing common patterns for using
dynamically loaded extensions.

[1]: http://blog.doughellmann.com/2013/01/stevedore-08.html
[2]: http://cliff.readthedocs.org/en/latest/index.html
[3]: http://crossjam.net/wp/mpr/2012/07/cliff-2/