Title: ZeroTier Tutorials
Date: 2018-07-04 11:17
Author: crossjam
Category: Uncategorized
Slug: zerotier-tutorials
Status: published

Link parkin’

Since I’m a Digital Ocean customer, this article was quite handy. [*Getting Started with Software-Defined Networking and Creating a VPN with ZeroTier One*][1] by Sam Cater:

> [ZeroTier One][3] is an open-source application which uses some of the latest developments in SDN to allow users to create secure, manageable networks and treat connected devices as though they're in the same physical location. ZeroTier provides a web console for network management and endpoint software for the clients. It's an encrypted Peer-to-Peer technology, meaning that unlike traditional VPN solutions, communications don't need to pass through a central server or router — messages are sent directly from host to host. As a result it is very efficient and ensures minimal latency. Other benefits include ZeroTier's simple deployment and configuration process, straightforward maintenance, and that it allows for centralized registration and management of authorized nodes via the Web Console.

> By following this tutorial, you will connect a client and server together in a simple point-to-point network. Since Software-Defined Networking doesn't utilize the traditional client/server design, there is no central VPN server to install and configure; this streamlines deployment of the tool and the addition of any supplementary nodes. Once connectivity is established, you'll have the opportunity to utilize ZeroTier's VPN capability by using some clever Linux functionalities to allow traffic to leave your ZeroTier network from your server and instruct a client to send it's traffic in that direction.

The following was helpful in getting ZeroTier up and running on [my home k8s cluster][4]. [*Accessing your Raspberry Pi securely from the Internet using ZeroTier*][2] by Kelvin Zhang:

> When you need to access your Raspberry Pi from home, exposing your public IP/using dynamic DNS and opening ports can expose your Pi to potential security threats, especially if you’re using password-based authentication or running services behind these ports.

> The well-known method of doing it is to use a VPN. Whereas OpenVPN is a common solution, ZeroTier heavily outshines it. OpenVPN can be cumbersome to set up and maintain (especially if things go wrong), and provisioning new devices can be a pain with having to generate certificates. In comparison, ZeroTier can be installed with a single bash script, and your virtual network can be managed with their web panel which enables you to provision devices, assign static IPs and more.

Give ’em a read if this stuff interests you.

[1]: https://www.digitalocean.com/community/tutorials/getting-started-software-defined-networking-creating-vpn-zerotier-one
[2]: https://iamkelv.in/blog/2017/06/zerotier.html
[3]: https://www.zerotier.com/
[4]: https://crossjam.net/wp/mpr/2018/07/speaking-of-that-cluster/