Title: Fabric or Capistrano?
Date: 2013-03-16 23:02
Author: crossjam
Category: Uncategorized
Slug: fabric-or-capistrano
Status: published

So at this point in my multi-vm explorations, it’s pretty clear I’ll need some configuration automation beyond provisioning. Sometimes you just need to shut down and restart services across a bunch of machines in a certain order. SSHing into each one and doing it by hand is now sufficiently painful to consider how the pros do it.

[Capistrano][1] has the advantage of getting me deeper into Ruby. [Fabric][2], based on Python, means an easier learning curve. Choices, choices.

[1]: https://github.com/capistrano/capistrano
[2]: http://fabfile.org/