Title: Vagrant DSTK
Date: 2013-03-04 20:42
Author: crossjam
Category: Uncategorized
Slug: vagrant-dstk
Status: published

Pete Warden built [a Data Science Toolkit Vagrant basebox][1]:
> I have fallen in love with Vagrant over the last year, it turns an entire logical computer as a single unit of software. In simple terms, you can easily set up, run, and maintain a virtual machine image with all the frameworks and data dependencies pre-installed. You can wipe it, copy it to a different system, branch it to run experimental changes, keep multiple versions around, easily share it with other people, and quickly deploy multiple copies when you need to scale up. It's as revolutionary as the introduction of distributed source control systems, you're suddenly free to innovate because mistakes can be painlessly rolled back, and you can collaborate other people without worrying that anything will be overwritten.

> Before I discovered Vagrant, I'd attempted to do something similar with my Data Science Toolkit package, distributing a VMware image of a full linux system with all the software and data it required pre-installed. It was a large download, and a lot of people used it, but the setup took more work than I liked. Vagrant solved a lot of the usability problems around downloading VMs, so I've been eager to create a compatible version of the DSTK image. I finally had a chance to get that working over the weekend, so you can create your own local geocoding server just by running:

> **vagrant box add dstk http://static.datasciencetoolkit.org/dstk_0.41.box**

> **vagrant init**

Cool! I’m becoming more of a fan of vagrant as well. This may have to be the first basebox I try out on Ye ’Olde MacBook. I was thinking a [CartoDB 2.0][3] basebox build would be fun to do, but someone already [beat me to it][2].

[1]: http://petewarden.typepad.com/searchbrowser/2013/01/the-data-science-toolkit-is-now-on-vagrant.html
[2]: https://github.com/zhm/geobox
[3]: https://github.com/CartoDB/cartodb20