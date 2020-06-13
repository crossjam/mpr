Title: basebox
Date: 2013-03-06 20:08
Author: crossjam
Category: Uncategorized
Slug: basebox
Status: published

I’ve managed to use [veewee][1] to successfully build baseboxes for vagrant, but didn’t exactly find the experience pleasant. Mainly because the veewee post install scripts are totally isolated within the vm. I really wanted to replace the default ssh keys for the default vagrant account which are hardwired to be downloaded from a public url on the net. Feels like a recipe for disaster to me, but I could only come up with kludgy post basebox build fixup-script to solve the problem.

Maybe the Python based [basebox][1] can make this a little cleaner:
> Basebox is a small Python library for building and interacting with Vagrant boxes using Fabric. Its goals are somewhat similar to the veewee project, but is specifically geared toward developing and testing Fabric deployments.

[1]: https://github.com/davehughes/basebox
[2]: https://github.com/jedi4ever/veewee