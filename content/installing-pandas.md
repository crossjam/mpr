Title: Installing Pandas
Date: 2012-07-09 22:14
Author: crossjam
Category: Uncategorized
Slug: installing-pandas
Status: published

Recently I went through the process of installing [pandas][2] Mac OS X and had a similar [experience][1] to Grig Gheorghiu,
> I tried to install the pandas Python library a while ago using easy_install/pip and I hit some roadblocks when it came to installing all the dependencies. So I tried it again, but this time I tried to install most of the required packages from source. Here are my notes, hopefully they'll be useful to somebody out there. 

It wasn’t a truly heinous effort, but a lot less clean than I expected. Like Grig, HDF5 and PyTables were the worst, being the only ones I couldn’t pip my way through. However, I already had gfortran installed.

I’m really looking forward to putting pandas to the test, but this exercise makes using something like the [Enthought Python Edition][3] really attractive.

[1]: http://agiletesting.blogspot.com/2012/07/installing-statistics-packages-on-ubuntu.html
[2]: http://pandas.pydata.org/
[3]: http://www.enthought.com/products/epd.php