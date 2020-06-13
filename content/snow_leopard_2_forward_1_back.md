Title: Snow Leopard: 2 Forward, 1 Back
Date: 2009-09-07 21:35
Author: crossjam
Category: Uncategorized
Slug: snow_leopard_2_forward_1_back
Status: published

[ <img src="http://crossjam.net/mpr/media/saft logo.gif" alt="saft logo.gif" border="0" width="128" height="128" align="left" style="margin: 10px;" />][1] So my installation of Snow Leopard is much less [busted][2]. [Saft][1] now works once again, although I'm a bit chuffed. I had to fork over another $8 when I only bought my Leopard license 2 months ago. Oh well. I also installed the dev tools, so I should be able to build various programs and libraries from source.

I say **should** because Snow Leopard has introduced a couple of points of confusion. First, is the whole [64 bit transition][3], which is causing some heartburn in terms of old codebases and old libraries. The second is that the new dev compiler is gcc-4.2, but the old gcc-4.0 compiler is not installed by default. Once it is installed, then you've got two compilers available, which is one too many. In general, commercially developed apps seem to be doing fine though.

Apple's gone and busted up my Python however. I had a 2.6.2 Framework build with a bunch of extensions. Now I can't build any new modules for it. I also use [virtualenv][4] a lot, but you can't turn off 64 bitness for python binaries in such environments. Plus, all of the 2D graphics libraries (wxPython, pygame, PyQT) seem to be in a touch of disarray due to libraries that use APIs eliminated in Snow Leopard. I was planning on doing [my 100 hours project][5] based on some of these modules. Now that's all in doubt.

Grumble.

[1]: http://haoli.dnsalias.com/Saft/
[2]: http://crossjam.net/wp/mpr/2009/09/busted_by_snow_leopard/
[3]: http://arstechnica.com/apple/reviews/2009/08/mac-os-x-10-6.ars/5
[4]: http://iamzed.com/2009/05/07/a-primer-on-virtualenv/
[5]: http://crossjam.net/wp/mpr/2009/07/100_million_hours

