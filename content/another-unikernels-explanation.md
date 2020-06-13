Title: Another Unikernels Explanation
Date: 2017-07-07 20:08
Author: crossjam
Category: Uncategorized
Slug: another-unikernels-explanation
Status: published

I enjoyed this Datanauts podcast, [“Unikernels Vs. Containers,”][1] which dove into what unikernels are and why they matter. The interview guest, Adam Wick, really had a depth of knowledge from real working experience researching and using unikernel technology. He basically had the most concise explanation of unikernels I’ve heard yet. To paraphrase:

1. Build your application for a kernel
2. Turn the kernel into a library
3. Combine your application and the library
4. Throw away the stuff you don’t need in the library
5. Congratulations! You’ve got a unikernel! 
6. Now just launch it on a hypervisor or even bare metal. It should be relatively secure and resource constrained.

I need to listen to that episode again as I was distractedly tuning out for certain segments. Sounded like there was some good discussion of when unikernels are actually a good use case fit.

Also, from examining the archives, the [Datanauts Podcast][2] looks right up my alley.

[1]: http://packetpushers.net/podcast/podcasts/datanauts-063-unikernels-vs-containers/
[2]: http://packetpushers.net/series/datanauts-podcast/