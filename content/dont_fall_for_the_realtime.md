Title: Don't Fall For the Realtime
Date: 2009-09-28 23:20
Author: crossjam
Category: Uncategorized
Slug: dont_fall_for_the_realtime
Status: published

[<img src="http://crossjam.net/mpr/media/PubSubHubbub Logo.png" alt="PubSubHubbub Logo.png" border="0" width="113" height="38" align="left" style="margin: 10px;" />][1] I've been doing a little more thinking about decentalized, Web scale, publish/subscribe, a.k.a [the PushButton Web][2]. Often "realtime" is used in conjunction with this term which is a bit of a red herring.

First, most PushButton Web advocates are savvy enough to realize that TCP, and HTTP on top of it, in no way have realtime guarantees. TCP explictly trades realtime for reliable delivery.

Which leads to my second point. The underlying goal of all this Web style decentralization is to remove a single point of failure, Twitter, and increase reliability of tweet delivery.

This epiphany came to me partially because all the Web fantasy football leagues I'm in provide "realtime" scoring tools. Yahoo!'s scoreboard goes a bit hinky from time to time, but they're all updated remarkably quickly, typically within seconds of a play's conclusion. I don't know exactly how many users have these tools up at any given time but if it's even a small percentage of league participants that's probably still a big number. So if realtime is that big a deal, there are tools and techniques in existence to build upon.

I also had a hard time coming up with a compelling use case for realtime tweets or other web notifications. Then again, I may just not have enough vision, as I'm definitely **NOT** a hardcore, full time, always on, Twitter user.

If a pretty good, best effort, Web scale, Web style, pub/sub infrastructure emerges, without any real "realtime", that's still a good thing.

Just thinking out loud.

[1]: http://code.google.com/apis/pubsubhubbub

[2]: http://dashes.com/anil/2009/07/the-pushbutton-web-realtime-becomes-real.html

