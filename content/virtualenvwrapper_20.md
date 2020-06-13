Title: virtualenvwrapper 2.0
Date: 2010-04-07 17:20
Author: crossjam
Category: Uncategorized
Slug: virtualenvwrapper_20
Status: published

If you use Python you should be using [`virtualenv`][3]. If you're using `virtualenv` you should be using [`virtualenvwrapper`][2].

The gist is that `virtualenv` creates clean, custom Python installations where you can muck up the installed extensions without messing up the global system wide install. `virtualenvwrapper` better integrates these virtual environments with your shell command line, among other things. Ultimately you can easily flow between various "versions" of Python with all sorts of weird extensions, without wrecking a default installation. And `virtualenvwrapper` is pluggable. So if you don't like how it works, or want something it doesn't do, you can fix it.

Doug Hellman, `virtualenvwrapper`'s author, recently cut loose [a major new release][1]. Go get it.

That is all!

[1]: http://blog.doughellmann.com/2010/04/major-new-release-of-virtualenvwrapper.html

[2]: http://www.doughellmann.com/projects/virtualenvwrapper/

[3]: http://pypi.python.org/pypi/virtualenv

