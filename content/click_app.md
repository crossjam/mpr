Title: Click App
Date: 2020-07-11
Status: published


Sometimes if you just wait long enough, the universe will provide what
you’ve been looking for.

I’m a heavy user of [Click][1], the Python library for creating
command line interfaces (CLIs). There are a lot of idiomatic ways that I
build my CLIs. For example, I’m a bit persnickety about logging
configuration. Timestamps should either be UTC ISO 8601 or UNIX epoch
if needed. And every CLI should have options for setting the logging
level. But I’ve never sat down and put all of my preferences
together in one easy to reuse place.

Simon Willison released [click-app][2], a "[Cookiecutter][3] template for
creating new Click command-line tools." Using Cookiecutter to roll up
all of my Click customizations has been on my to do list. I’ll
probably fork Simon’s repo but it’s already got 80% of the soluiton I
would have implemented myself.

[1]: https://click.palletsprojects.com/en/7.x/
[2]: https://github.com/simonw/click-app
[3]: https://cookiecutter.readthedocs.io/en/1.7.2/
