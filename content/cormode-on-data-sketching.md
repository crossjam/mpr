Title: Cormode on Data Sketching
Date: 2017-06-02 20:58
Author: crossjam
Category: Uncategorized
Slug: cormode-on-data-sketching
Status: published

[Graham Cormode][2], who is probably one of the most knowledgeable people in the world on the topic, has written [an insanely good article on *data sketching*][1]

> The aim of this article has been to introduce a selection of recent techniques that provide approximate answers to some general questions that often occur in data analysis and manipulation. In all cases, simple alternative approaches can provide exact answers, at the expense of keeping complete information. The examples shown here have illustrated, however, that in many cases the approximate approach can be faster and more space efficient. The use of these methods is growing. Bloom filters are sometimes said to be one of the core technologies that "big data experts" must know. At the very least, it is important to be aware of sketching techniques to test claims that solving a problem a certain way is the only option. Often, fast approximate sketch-based techniques can provide a different tradeoff.

I say “insanely good” because there is some seriously hairy math behind these techniques. Yet Cormode makes the principles easily accessible to a general, admittedly already technically inclined, audience. As a former instructor, this is an article you could give to a bunch of upperclassmen and then spend two good lectures working through details and implications. No mean feat. Plus, these types of data structures are increasingly important to know about.


[1]: http://queue.acm.org/detail.cfm?id=3104030
[2]: https://www2.warwick.ac.uk/fac/sci/dcs/people/graham_cormode/