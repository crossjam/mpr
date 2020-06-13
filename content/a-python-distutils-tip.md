Title: A Python Distutils Tip
Date: 2012-12-18 21:14
Author: crossjam
Category: Uncategorized
Slug: a-python-distutils-tip
Status: published

Parkin’ this in case it helps someone else, including me in the future. Oddly difficult to find documentation on the feature, the closest being [an aside on distutils config files][1].

When building a Python package that has a C extension you can build the extension separately, using the `build_ext` command. This allows you to control the include directories, link directories, and link libraries. Handy for those ornery libraries that you just can’t install in `/usr/lib` or thereabouts. I recently needed it for [geos][2] and [Shapely][3].

[1]: http://docs.python.org/2/distutils/configfile.html
[2]: http://trac.osgeo.org/geos/
[3]: http://pypi.python.org/pypi/Shapely