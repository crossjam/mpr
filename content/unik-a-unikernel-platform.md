Title: Unik, A Unikernel Platform
Date: 2017-08-13 21:02
Author: crossjam
Category: Uncategorized
Slug: unik-a-unikernel-platform
Status: published

Link parkin’. [UniK: The Unikernel Compilation and Deployment Platform][1]

From [an introductory blog post][2] on Unik:

> UniK (pronounced you-neek) is a tool for compiling application sources into unikernels -- lightweight bootable disk images -- rather than binaries. UniK runs and manages instances of compiled images across a variety of cloud providers as well as locally on Virtualbox. UniK utilizes a simple docker-like command line interface, making building unikernels as easy as building containers. UniK is built to be easily extensible, allowing - and encouraging - adding support for unikernel compilers and cloud providers.

Integrates with most of the major orchestration engines, deploys to multiple unikernel types (rump, OSv, IncludeOS, MirageOS) and provides polyglot language support including Javascript (Node.js), Go, Java, C/C++ and Python3.

[1]: https://github.com/cf-unik/unik
[2]: https://github.com/cf-unik/unik/wiki/UniK:-Build-and-Run-Unikernels-with-Ease