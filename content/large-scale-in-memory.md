Title: Large-Scale In-Memory
Date: 2012-05-17 19:32
Author: crossjam
Category: Uncategorized
Slug: large-scale-in-memory
Status: published

Amund Tveit attended [Accel’s Big Data Conference][2] and came away with [some interesting takeaways][3]. This spurred him to do [a mental exercise][1] on what it would take to store a year’s worth of Twitter’s tweets **in RAM**:
> *Keeping 1 year worth of tweets (including metadata) and (a crude) index of them in-memory is costly, but not too bad. I.e. 1.36 Million USD to keep 1 years worth of tweets (124 billion tweets) for 1 year in an (distributed) in-memory hashtable (or the same amount of tweets stored in the same hashtable for one day costs approximately 3732 USD).*

> *Q: So, is it time to reconsider using hard drives and SSDs and consider going for RAM instead*

> *A: yes, at least consider it and combine with Hadoop. …*

Obviously $1.36 million dollars is a heap ‘o kale, but there are probably businesses with that scale of data and a competitive need for that speed of processing. It‘s extreme now, but 15 years ago buying terabytes off the Costco shelf was unimaginable to most people.

Other nuggets that struck me between the two posts include the fact that Twitter sees 340 million tweets per day and that realtime processing is a hot topic. I personally had the feeling that “realtime at scale” is the new frontier but this is a shred of confirming evidence.

Don’t know about that “combine with Hadoop” comment though. The more I find out about Hadoop the less impressed I am.
 
[1]: http://atbrox.com/2012/05/16/a-large-scale-in-memory-storage-example/
[2]: http://www.accelbdc.com/
[3]: http://atbrox.com/2012/05/14/main-takeaways-from-accels-big-data-conference/