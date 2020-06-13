Title: EPD and virtualenv
Date: 2012-08-19 13:23
Author: crossjam
Category: Uncategorized
Slug: epd-and-virtualenv
Status: published

Parking this nugget in case it can help someone else discover it with Google.

EPD, [the Enthought Python Distribution][2], is a nice packaging of a lot of scientific and high performance computing modules. In particular, it takes away the hassle of building from source on persnickety platforms like Mac OS X.

[virtualenv][1] is an indispensable Python tool for creating isolated, customizable, and easily disposable Python environments. You can initialize these environments from a specific Python installation allowing experimentation with multiple Python versions in parallel, e.g. EPD and the stock install on your machine.

EPD and virtualenv weren’t working well together for me on my MacBook. Here’s what worked for me:

* Make sure you have a recent version of virtualenv, 1.7.2 seems good.
* Use the `--system-site-packages` argument to make sure you pick up the EPD extensions. You can also hack up postactivate and postdeactivate to fix up PYTHONPATH.
* Here’s an example of creating a new virtual environment:

> <small>`mkvirtualenv -p /Library/Frameworks/EPD64.framework/Versions/Current/bin/python --system-site-packages epd64`</small>

So far so good. You’ll need the [`virtualenvwrapper`][3] package to use `mkvirtualenv`.

[1]: http://www.virtualenv.org/en/latest/index.html
[2]: http://www.enthought.com/products/epd.php
[3]: http://www.doughellmann.com/projects/virtualenvwrapper/