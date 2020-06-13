Title: Harbor Image Registry
Date: 2018-07-06 20:23
Author: crossjam
Category: Uncategorized
Slug: harbor-image-registry
Status: published

One of the things about having an ARM-based RPi cluster is a need to serve custom images. Even though there are a number of well run, cloud stored image registries, including [Docker Hub][3] and [Google Container Registry][4], it feels like this is a homebrew style service that one should be able to host on their own. Straight [Docker Distribution][2] is surprisingly barebones. 

Meanwhile, VMWare has open-sourced [Harbor][1], an image registry which seems much more full featured:

> Project Harbor is an an open source trusted cloud native registry project that stores, signs, and scans content. Harbor extends the open source Docker Distribution by adding the functionalities usually required by users such as security, identity and management. Harbor supports advanced features such as user management, access control, activity monitoring, and replication between instances. Having a registry closer to the build and run environment can also improve image transfer efficiency.

[1]: http://vmware.github.io/harbor/
[2]: https://github.com/docker/distribution
[3]: https://hub.docker.com/
[4]: https://cloud.google.com/container-registry/