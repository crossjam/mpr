Title: Snow Leopard Update and DNS
Date: 2010-03-29 22:14
Author: crossjam
Category: Uncategorized
Slug: snow_leopard_update_and_dns
Status: published

Apple released a whopper of an update for Snow Leopard today. There's lots of [in-depth coverage][1] in various places.

All I know is that this update is supposed to fix this [pain in the ass DNS bug][2]. The short story is that Apple pushed DNS resolution facilities completely into the `mDNSResponder` daemon. Problem was that if a DNS server would occasionally time out, `mDNSResponder` would adjust the order in which it would solicit DNS servers. This can cause problems where you use a local DNS server to resolve machines on your LAN, then an ISP or [public DNS server][3] backs up your local server. Eventually errors like this would pop-up:

<blockquote><code>

ssh: Could not resolve hostname nightcrawler: nodename nor servname provided, or not known

</code></blockquote>

The bug wasn't a heinous show stopper, renewing your DHCP lease seemed to fix it, but it was still a major irritant.

There's allegedly [a fix to support this DNS situation][4]  according to [Apple's update notes][5]. Hopefully if anyone else is still suffering from this pest, this post can point them in the right direction.

[1]: http://www.macworld.com/article/150143/2010/03/inside1063.html

[2]: http://discussions.apple.com/thread.jspa?threadID=2132856

[3]: http://code.google.com/speed/public-dns/

[4]: http://support.apple.com/kb/HT4030

[5]: http://support.apple.com/kb/HT4014

