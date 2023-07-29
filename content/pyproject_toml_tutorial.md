Title: A pyproject.toml Tutorial
Date: 2022-12-11
Author: C. Ross Jam
Status: published


In starting a new Python module for mucking around with the [Feedbin
API][2], I wanted to modernize a little and update to the latest Python
practices for packaging. In particular, I’d been hearing a bit about
`pyproject.toml` as the way to configure Python build tools. Rogier
van der Greer has [an excellent overview][1]:

> About three years ago I wrote a blog post about using setup.py to
> set up your python projects. Since then a lot has changed, mostly
> due to PEP 517, PEP 518 and the introduction of the pyproject.toml
> file. 

> The goal of this file is to allow you to define what build tools are
> needed in order to build your package – no longer assuming it must
> be Setuptools. This makes it easier to use alternatives to
> Setuptools, which means that Setuptools does no longer have to be
> the one build tool that can do everything. 

> Nevertheless, I like the feature set of Setuptools, and would like
> to continue to use it in the foreseeable future. But while
> documentation for using for example Poetry or Flit together with a
> pyproject.toml is easy to find, it is more difficult to find similar
> documentation for Setuptools. So let me help you out. 

[1]: https://godatadriven.com/blog/a-practical-guide-to-setuptools-and-pyproject-toml/
[2]: https://github.com/feedbin/feedbin-api
