Title: NodeBox Image Processing
Date: 2009-09-24 22:51
Author: crossjam
Category: Uncategorized
Slug: nodebox_image_processing
Status: published

<img src="http://crossjam.net/mpr/media/nodebox plus PIL.png" alt="nodebox plus PIL.png" border="0" width="254" height="320" align="right" style="margin: 10px;" /> The image capture to the right is the result of my building the [Python Imaging Library][1] such that it can be imported within [NodeBox][2]. Basically I'm showing that the module can be imported, used to load an image, and that image can be turned into a Numpy array. Remember, this was going to be [a little personal achievement][3].

Well, just like last time, I learned that NodeBox already has the capability I was looking for. NodeBox has not one, but two, image processing extension libraries. The first is [PhotoBot][4], which is essentially PIL 1.1.4 for NodeBox, and deprecated. So while I was ignorant at least it was ignorance of dusty old code that would have  need some revival effort.

The second library, [Core Image][5], is a direct poke in the eye. A MacOS only extension, it uses the os's built-in image processing facilities. Core Image provides an object model similar to PhotoShop's where an image is built out of layers that can be individually processed and collectively composited. Since the image processing code is a part of the os, and presumably heavily used, it's been highly optimized **AND** should take advantage of any GPU speed boosts.

Basically, Core Image looks like what I was looking for if I had only looked a little more carefully.

No worries though. This is all about spare time hacking and learning.

[1]: http://www.pythonware.com/products/pil/
[2]: http://nodebox.net/
[3]: http://crossjam.net/wp/mpr/2009/09/nodebox_and_numpy/
[4]: http://nodebox.net/code/index.php/PhotoBot
[5]: http://nodebox.net/code/index.php/Core_Image

