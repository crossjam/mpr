Title: The Pushbutton Web and Mobility
Date: 2009-08-23 18:51
Author: crossjam
Category: Uncategorized
Slug: the_pushbutton_web_and_mobilit
Status: published

[<img src="http://crossjam.net/mpr/media/PubSubHubbub Logo.png" alt="PubSubHubbub Logo.png" border="0" width="113" height="38" align="left" style="margin: 10px;" />][1] I find Anil Dash's concept of ["The Pushbutton Web"][2] a nice condensing of an intriguing emergent phenomenon on the web. The general concept is that clients establish Web native callbacks or subscriptions where "realtime" notifications can be sent. Then various services, e.g. standing search, can "push" information to the clients without the client having to continuously poll for new information.

There seems to be a strong effort in Google to push this along with their [PubSubHubbub protocol and toolkit][1]. They've even enabled a number of their services to provide [pushbutton notifications through PubSubHubbub][3]. Similarly, the [rssCloud][5] folks are doing some interesting tinkering.

This stuff isn't exactly new or groundbreaking, I remember [Bob Wyman's PubSub][4] trying to make a viable business out of "realtime search". However, given the growth of Twitter, Facebook, and the general use of Ajax for in-page realtime updates, the right time may have arrived for a loosely coupled, collaborative buildout to support this capability. Interestingly I had a prescient thought about this topic, [*NMH: Daily Me is Here*][6], on New Media Hack, back in 2004.

One fly in the ointment might be integrating the humongous population of mobile devices out there, which will probably never have continuous connectivity. The pushbutton protocols I've seen so far assume a reliably upstanding Web server. Otherwise the "pushing" services typically drop the subscription, often relatively quickly. If you use some kind of proxy, how long does the proxy keep old notifications? Do you even need to keep old notifications? Or is this something that the client should determine? I wonder how [Research in Motion](http://www.rim.com) deals with this for the BlackBerry.

So what to do in the face of disconnected clients? I think that's going to be a major challenge for The Pushbutton Web.

[1]: http://code.google.com/apis/pubsubhubbub

[2]: http://dashes.com/anil/2009/07/the-pushbutton-web-realtime-becomes-real.html

[3]: http://googlecode.blogspot.com/2009/08/towards-programmable-web-pubsubhubbub.html

[4]: http://bob.wyman.us/main/pubsub/

[5]: http://rsscloud.org/

[6]: http://crossjam.net/nmh/archives/000870.html

