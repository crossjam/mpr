Title: Container-Based Network Emulation
Date: 2017-08-09 20:38
Author: crossjam
Category: Uncategorized
Slug: container-based-network-emulation
Status: published

As is my wont, I sometimes prowl around old proceedings of systems conferences. Today I landed on [the program for ACM CoNEXT 2012][1], with a paper interestingly titled, [*“Reproducible Network Experiments Using Container-Based Emulation” (PDF)*][2]

> In an ideal world, all research papers would be runnable: simply click to replicate all results, using the same setup as the authors. One approach to enable runnable network systems papers is Container-Based Emulation (CBE), where an environment of virtual hosts, switches, and links runs on a modern multicore server, using real application and kernel code with software-emulated network elements. CBE combines many of the best features of software simulators and hardware testbeds, but its performance fidelity is unproven.

> In this paper, we put CBE to the test, using our prototype, Mininet-HiFi, to reproduce key results from published network experiments such as DCTCP, Hedera, and router buffer sizing. We report lessons learned from a graduate networking class at Stanford, where 37 students used our platform to replicate 16 published results of their own choosing. Our experiences suggest that CBE makes research results easier to reproduce and build upon.

Obviously containers, even [Linux containers][3], are fairly old, but I’m just amused that an impactful research paper involving containers was published 5 years ago, with the work essentially done 10 months before the uber-hyped Docker was open sourced. The future is already here, just unevenly distributed and all that jazz.

Ditto for all the computational, reproducible, publication hoohah around web-based scientific notebooks, such as Jupyter.

*Bonus entertainment! Check out [the accompanying presentation slides (PDF)][4], especially slide 60. I always tell people, at some point in the process getting a PhD really sucks. No exceptions!*

[1]: http://conferences.sigcomm.org/co-next/2012/program.html
[2]: http://conferences.sigcomm.org/co-next/2012/eproceedings/conext/p253.pdf 
[3]: https://en.wikipedia.org/wiki/LXC
[4]: http://conferences.sigcomm.org/co-next/2012/slides/Heller_156.pdf