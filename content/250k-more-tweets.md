Title: 250K+ More Tweets
Date: 2011-10-16 21:18
Author: crossjam
Category: Uncategorized
Slug: 250k-more-tweets
Status: published

Actually, I've got over 335K tweets and counting captured on this collection. There were two keys to making progress over [my last effort][1]. First, I moved my collector to a personal [Linode](http://www.linode.com/) virtual private server (VPS). As opposed to my ancient home Linux workstation, the VPS can stay up and on the network for days and weeks at a time. No outages due to brief power shutdowns or arbitrary Verizon glitches. Second, my script actually recovered from a network hiccup that killed its child `curl` process. Picked up the right error code, forked off a new `curl`, and kept on trucking.

The back of the envelope rate of collection is about 60K+ tweets per 24 hours. At this rate, it'll take me about another week and a half to hit the million mark. I'm not holding my breath, but glad to see a significant advance over the last milestone.

**P.S.** After a few months, can thoroughly recommend Linode's services.

[1]: http://crossjam.net/wp/mpr/2011/10/250k-tweets/