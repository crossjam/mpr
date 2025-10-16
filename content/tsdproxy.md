---
title: "TSDProxy"
date: 2025-10-16
author: "C. Ross Jam"
status: published
---

Link parkin’: [TSDProxy][1]

> TSDProxy is an application that automatically creates a proxy to
> virtual addresses in your Tailscale network. Easy to configure and
> deploy, based on Docker container labels or a simple proxy list
> file. It simplifies traffic redirection to services running inside
> Docker containers, without the need for a separate Tailscale
> container for each service. 

I landed on TSDProxy via exploration of incorporating [dokku][2] into
my [tailnet][3]. On cursory examination, here be dragons. The tricky
bit is if you want to serve SSL traffic from a container, which then
requires some DNS and cert jujitsu. There is also a [dokku tailscale
plugin][4] but the same configuration caveats apply.

Seems like an adventure worth diving into.

[1]: https://almeidapaulopt.github.io/tsdproxy/
[2]: https://dokku.com/
[3]: https://tailscale.com/kb/1136/tailnet
[4]: https://github.com/andrew-womeldorf/dokku-tailscale
