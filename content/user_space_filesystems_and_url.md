Title: User Space Filesystems and URL Routing
Date: 2010-07-16 17:24
Author: crossjam
Category: Uncategorized
Slug: user_space_filesystems_and_url
Status: published

Nice post by Evan Broder discussing [an interesting approach to implementing user space file systems][1]. The key trick is to treat filesystem request handling similar to URL request routing.

Linux, and other UNIX like operating systems, have long had support for implementing

[filesystems in user space][2]. This allows hackers to hide all kinds of interesting computation and services behind a *(the?)* core UNIX abstraction. Performance and [support *(a.k.a. FUSE)*][3] on modern machines has gotten so good, you can even [implement filesystems using Python][4].

As part of implementing the filesystem, a module has to translate request against pathnames into responses. Sounds remarkably familiar. HTTP servers have to do the same thing. Even better, web application frameworks and stacks like Djangon and Ruby on Rails do as well. Thus, there's been a significant amount of effort put in by the developer community to come up with idiomatic ways to cleanly and flexibly deal with this dispatch. For example, Python's [Routes][5] module.

Smooshing the URL routing concept into FUSE support leads to [RouteFS][6], "A FUSE API wrapper based on URL routing". Broder then goes on to demonstrates a toy virtual filesystem that accesses github, but also points to his virtual machine work on [Invirt][7] as a more serious usage of the approach.

*[Moby][8] hack!*

[1]: http://blog.ksplice.com/2010/07/building-filesystems-the-way-you-build-web-apps/

[2]: http://en.wikipedia.org/wiki/Filesystem_in_Userspace

[3]: http://fuse.sourceforge.net/

[4]: http://code.google.com/p/fusepy/

[5]: http://pypi.python.org/pypi/Routes

[6]: http://pypi.python.org/pypi/RouteFS

[7]: http://invirt.mit.edu/

[8]: http://www.outpost9.com/reference/jargon/jargon_28.html#TAG1157

