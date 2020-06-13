Title: Docker Containers and Signals
Date: 2017-07-17 21:15
Author: crossjam
Category: Uncategorized
Slug: docker-containers-and-signals
Status: published

Here be dragons. I know from personal experience but [Hynek Schlawack explains why][1] way better than me.

> Proper cleanup when terminating your application isn’t less important when it’s running inside of a Docker container. Although it only comes down to making sure signals reach your application and handling them, there’s a bunch of things that can go wrong.

Really, as Hynek says, “Avoid being PID 1.”

[1]: https://hynek.me/articles/docker-signals/