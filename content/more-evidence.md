Title: More Evidence
Date: 2013-01-22 22:08
Author: crossjam
Category: Uncategorized
Slug: more-evidence
Status: published

In-memory data processing of massive data needs a catchy nickname. I hearby christen thee **Big RAM (™)**. Probably won’t stick but maybe I can find some unsuspecting proposal to slap it into. Unfortunately close to *bigram* to be distinctively visible in search engines. Might be able to make some useful social media handles out of that.

In any event, herewith two more nuggets regarding the march of the RAM/SSD combo architecture. First [a bit of a rant on SSDs][1], from the not disinterested Brian Bulkowski:

> The economics of flash memory are staggering. If you’re not using SSD, you are doing it wrong. 

> Not quite true, but close. Some small applications fit entirely in memory – less than 100GB – great for in-memory solutions. There’s a place for rotational drives (HDD) in massive streaming analytics and petabytes of data. But for the vast space between, flash has become the only sensible option.

My quick scan of the comments didn’t see anyone unearthing blinding fundamental errors, other than relying on Dell Enterprise SSD pricing as a baseline, but read with an appropriate grain of salt.

Then today, [yet another announcement][2] from Amazon Web Services:

> Our new High Memory Cluster Eight Extra Large (cr1.8xlarge) instance type is designed to host applications that have a voracious need for compute power, memory, and network bandwidth such as in-memory databases, graph databases, and memory intensive HPC.

> Here are the specs:

>    * Two Intel E5-2670 processors running at 2.6 GHz with Intel Turbo Boost and NUMA support.
>    * 244 GiB of RAM.
>    * Two 120 GB SSD for instance storage.
>    * 10 Gigabit networking with support for Cluster Placement Groups.
>    * HVM virtualization only.
>    * Support for EBS-backed AMIs only.

> This is a real workhorse instance, with a total of 88 ECU (EC2 Compute Units). You can use it to run applications that are hungry for lots of memory and that can take advantage of 32 Hyperthreaded cores (16 per processor). We expect this instance type to be a great fit for in-memory analytics systems like SAP HANA and memory-hungry scientific problems such as genome assembly.

At $3.50 an hour, rent 6 for $21/hour, and get off on eight hours of 192 cores with an aggregate 1TB of RAM, 1TB of SSD, and $168 out of your pocket. 

Now that would be a fun day at the office!

[1]: http://highscalability.com/blog/2012/12/10/switch-your-databases-to-flash-storage-now-or-youre-doing-it.html
[2]: http://aws.typepad.com/aws/2013/01/ec2-for-in-memory-computing-the-high-memory-cluster-eight-extra-large.html