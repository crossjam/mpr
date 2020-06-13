Title: Fear of an OAuth Planet
Date: 2012-09-04 16:15
Author: crossjam
Category: Uncategorized
Slug: fear-of-an-oauth-planet
Status: published

<img src="http://crossjam.net/wp/mpr/wp-content/uploads/2011/12/Twitter-Bird-Small.png" alt="Twitter Bird Small" border="0" width="100" height="100" align="right" style="margin: 10px;" /> For the final third of the year, I’m resurrecting my Twitter data collection project on a grander scale. More cities, more data, more processing, more analysis. The only major delta is that Twitter is seriously threatening to [apply OAuth to all of its API endpoints][1]. Since my little project isn’t really a Web application per se, the thought of having to do [a 3-Legged OAuth handshake][4] seemed daunting especially for the little ’ole Streaming API.

Fortunately, Peter Hoffman teed up [an easy authentication workaround][3] by just generating the tokens for the consumer and app through Twitter. Then you simply stash them away and appropriately sign your initial connection request.

Meanwhile, Greg Roodt at The Mosh Pit, goes the full Monty, explaining how even with the complete 3-Legged handshake, [authenticating streaming with OAuth][2] isn’t really that bad. Bonus props for pointing to [a GitHub repository of sample code][5] that can be conveniently forked and extended.

[1]: https://dev.twitter.com/blog/changes-coming-to-twitter-api
[2]: http://tech.mindcandy.com/2011/08/accessing-the-twitter-streaming-api-with-oauth/
[3]: http://peter-hoffmann.com/2012/simple-twitter-streaming-api-access-with-python-and-oauth.html
[4]: https://dev.twitter.com/docs/auth/3-legged-authorization
[5]: https://github.com/groodt/twitter-oauth-streaming