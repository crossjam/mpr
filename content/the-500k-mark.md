Title: The 500K+ Mark
Date: 2011-10-19 21:36
Author: crossjam
Category: Uncategorized
Slug: the-500k-mark
Status: published
Attachments: wp/mpr/wp-content/uploads/2011/10/MongoDB-Logo.png

[<img src="http://crossjam.net/wp/mpr/wp-content/uploads/2011/10/MongoDB-Logo.png" alt="MongoDB Logo" border="0" width="168" height="79" align="right" style="margin: 10px;" />][1] Passed the 500K mark in tweets collected. Halfway home. I'm not so much amazed that I've gotten this far, but that there haven't been more bumps. Basically, I've had a single script running for well over a week. That script has only needed to launch two child processes and only recover once from a child failure. The same script is a paltry 51 lines of code **including** empty and comment lines. Meanwhile the data file is now well over 1GB.

That's a testament to 1) Python's concision, 2) Linux/UNIX's simple clean design, 3) Twitter's clean [streaming API][3] and 4) [`curl`][4]'s robustness. I've just glued a bunch of really solid parts together to good effect.

Now that I'm on the downhill, I'm starting to think of datastores to hold, index, and query the data with. [MongoDB][1] seems like it might be the best fit of the NoSQL camp since the Twitter streaming API pumps data out in [JSON][2]. MongoDB also seems to have a nice query language, to have indexing for time along with geography, and to be production ready at scale.

[1]: http://www.mongodb.org/
[2]: http://json.org/
[3]: https://dev.twitter.com/docs/streaming-api/methods
[4]: http://curl.haxx.se/