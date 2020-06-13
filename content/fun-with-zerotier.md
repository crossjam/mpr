Title: Fun With ZeroTier
Date: 2018-07-02 20:08
Author: crossjam
Category: Uncategorized
Slug: fun-with-zerotier
Status: published

I swear I’ve written about [ZeroTier][1] somewhere else before, but apparently not on this blog. The company and technology first came across my radar in a [PacketPushers podcast episode][2] that was a really deep technical dive. From the current front page of the website:

> ZeroTier delivers the capabilities of VPNs, SDN, and SD-WAN with a single system. Manage all your connected resources across both local and wide area networks as if the whole world is a single data center.

Behind the scenes, ZeroTier uses [software defined networking][3] and cryptographic techniques to build secure, planetary-scale, virtual Ethernet networks. For the administrator, installation and setup is a relatively painless experience as these things go. Meanwhile, devices in a ZeroTier network can interconnect as if they were on the same local-area network (LAN) wherever they are. ZeroTier endpoints conveniently figure out ways to punch through firewalls and other network obstructions. Sort of like VPNs with 90% less hassle and a 90% more fun from a networking perspective.

Recently I setup ZeroTier on my personal laptop and a home Raspberry Pi 3 cluster. The cluster is behind the firewall of a wireless router and my service provider, but it’s been pretty seamless to remotely SSH into the cluster from just about anywhere.

The only potential downer, if you’re really into this stuff, is that the free service relies on a kernel of centralized infrastructure maintained by the ZeroTier company. Using the service thus places trust in ZeroTier’s security, infrastructure capabilities, technical competence, etc. etc. A not negligible concern to an entity’s business processes. This is counterbalanced by an open source codebase and a commercial option for on-prem deployment if full accountability is needed.

For me though, ZeroTier has worked better than expected and there’s some interesting underlying tech below the surface.

[1]: https://www.zerotier.com/
[2]: https://packetpushers.net/podcast/podcasts/pq-134-meet-zerotier-open-source-networking/
[3]: https://en.wikipedia.org/wiki/Software-defined_networking