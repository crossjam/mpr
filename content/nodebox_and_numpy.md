Title: NodeBox and Numpy
Date: 2009-09-19 19:22
Author: crossjam
Category: Uncategorized
Slug: nodebox_and_numpy
Status: published

[<img src="http://crossjam.net/mpr/media/nodeboxicon.png" alt="nodeboxicon.png" border="0" width="64" height="64" align="left" style="margin: 10px;" />][1]

So I made a comment about [plastering together some Python modules][2] to get "[NodeBox][1] plus a high end image processing substrate." Turns out NodeBox already has [Numpy baked in][3] as of version 1.9.3. Should have done a little background research.

Looks like there's some wheels I won't have to reinvent. Would be nice if NodeBox had the [Python Imaging Library][4] included. This would make loading a wide variety of image formats into [Numpy][5] arrays quite easy. But incorporating that module into NodeBox will make a nice little personal project.

It'll be good to build on a solid foundation with an active user community. The only limitation of NodeBox for me, relative to [processing][7], is a handful of [bitblt][6] operations.

[1]: http://nodebox.net/
[2]: http://crossjam.net/wp/mpr/2009/09/unbusting_python/
[3]: http://nodebox.net/code/index.php/shared_2008-02-05-16-31-09
[4]: http://www.pythonware.com/products/pil/
[5]: http://numpy.scipy.org/
[6]: http://en.wikipedia.org/wiki/Bitblt
[7]: http://processing.org/

