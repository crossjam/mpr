Title: vagrant and veewee
Date: 2013-02-25 18:44
Author: crossjam
Category: Uncategorized
Slug: vagrant-and-veewee
Status: published

As promised, I’m [getting up to speed on vagrant][2] at work. It’s working out about as well as expected, with an anticipated steep learning curve. The big hurdle is having to learn a bit of automated configuration management using [Puppet][3] at the same time. All in all I’m surprised at how quickly I’ve managed to get a multi-VM Hadoop virtual cluster going. 

There is one concern though, adequately stated, and solved by [the veewee project][1]:
> Vagrant is a great tool to test out new things or changes in a Virtual Machine (Virtualbox) using either chef or puppet.

> The first step to build a new Virtual Machine is to download an existing 'base box'.

> I believe this scares a lot of people as they don't know who or how this box was built. Therefore lots of people end up first building their own base box which is time consuming and often cumbersome.

> Veewee aims to automate all the steps for building base boxes and to collect best practices in a transparent way.

Veewee is next up on the stack of tools to learn.

[1]: https://github.com/jedi4ever/veewee
[2]: http://crossjam.net/wp/mpr/2013/01/time-to-learn-vagrant/
[3]: http://en.m.wikipedia.org/wiki/Puppet_(software)