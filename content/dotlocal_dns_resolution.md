Title: Locally Resolving .local
Date: 2025-06-09
Author: C. Ross Jam
Status: published

Link parkin’ a [GitHub gist][1], because it leads to some fun pure local
configuration and I can’t quite find anything similar in a web page or
blog post.

> <script src="https://gist.github.com/eloypnd/5efc3b590e7c738630fdcf0c10b68072.js"></script>

The rub is that you can configure macOS DNS to direct resolution of domains by
doing a bit of file tweaking in `/etc/resolver`. For example, `.test`
by adding an entry in `/etc/resolver/test` that points to 127.0.0.1
for a DNS nameserver. Then if you install and
configure [dnsmasqn][2] to listen for DNS requests on your machine, it can take over the resolution of
a domain and point entries to services anywhere, but your machine in
particular. This includes wildcarding subdomains. A tricky bit is
closely reading the dnsmasq docs on the `--address` option and knowing
you can use that in a `dnsmasq.conf` file.

What’s this good for? I used it when working with [Dokku][3] which
allocates subdomains under a root domain for services it dynamically
builds and creates. Configured to use `.test` as
its root, all the services resolved nicely thanks to `dnsmasq`
pointing back to my laptop. This makes local experimentation and
demonstration of "push to deploy", PaaS services easy, fun, and
portable. YMMV.

Of note, there’s a new(ish) PaaS on the block that I’d like to try
out: [coolify][4]

[1]: https://gist.github.com/eloypnd/5efc3b590e7c738630fdcf0c10b68072
[2]: https://thekelleys.org.uk/dnsmasq/doc.html
[3]: https://dokku.com
[4]: https://coolify.io

