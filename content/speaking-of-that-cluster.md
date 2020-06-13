Title: Speaking of That Cluster...
Date: 2018-07-03 16:32
Author: crossjam
Category: Uncategorized
Slug: speaking-of-that-cluster
Status: published
Attachments: wp/mpr/wp-content/uploads/2018/07/RPi-Cluster.jpg

Last November, [I threatened to build][1] a Kubernetes cluster out of Raspberry Pi 3s. Well I actually did it starting during the December holidays and finishing up in January. Here’s a picture of it:

<img style="display:block; margin-left:auto; margin-right:auto;" src="https://crossjam.net/wp/mpr/wp-content/uploads/2018/07/RPi-Cluster.jpg" alt="Raspberry Pi k8s Cluster" title="RPi Cluster.JPG" border="0" width="300" height="208" />

The one warning, that’s not obvious from [the construction guide][2], is that the Raspberry Pi ARM processor architecture typically doesn’t have popular Docker images publicly available. This makes it somewhat challenging to do anything further usefully non-trivial. All-in-all, while not cheap, it was still a fun project and handy to have a k8s lab at home to play with.

[1]: https://crossjam.net/wp/mpr/2017/11/raspberry-k8s-pi-cluster/
[2]: https://www.hanselman.com/blog/HowToBuildAKubernetesClusterWithARMRaspberryPiThenRunNETCoreOnOpenFaas.aspx