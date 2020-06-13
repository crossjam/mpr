Title: Continuum.io’s Anaconda
Date: 2013-03-18 21:01
Author: crossjam
Category: Uncategorized
Slug: coninuum-ios-anaconda
Status: published

Currently kicking the tires on [Anaconda][1], Continuum.io’s Python distribution focused on high performance compute processing:
> Completely free enterprise-ready Python distribution for large-scale data processing, predictive analytics, and scientific computing

Looks really nice and well put together although it doesn’t seem to play well with virtualenv and has its own [environment model][2] and tool, [conda][3]:
> … Our users need to work with different versions of Python, NumPy, SciPy, and a variety of other packages. Moreover, they must be able to easily share live, runnable versions of their work, including all supporting packages, to their colleagues or the general public.

> We created the conda package and environment management system to solve these problems. It allows users to install multiple versions of binary packages (and any required libraries) appropriate for their platform and easily switch between them, as well as easily download updates from an upstream repository. ...

Bit of shame as virtualenv is really a core part of the Python ecosystem and personally makes my life a lot easier. But I can understand the tradeoff.

Anyway, Continuum provides the baseline Anaconda, which feels pretty competitive with the [Enthought Python Distribution][4], for free and with [a reasonable *(YMMV)*, proprietary friendly][5] license.

[1]: https://store.continuum.io/cshop/anaconda
[2]: http://continuum.io/blog/conda
[3]: http://docs.continuum.io/conda/index.html
[4]: http://www.enthought.com/products/epd.php
[5]: http://docs.continuum.io/anaconda/eula.html