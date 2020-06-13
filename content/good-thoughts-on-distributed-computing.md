Title: Good Thoughts on Distributed Computing
Date: 2017-08-25 19:45
Author: crossjam
Category: Uncategorized
Slug: good-thoughts-on-distributed-computing
Status: published

[Ken Birman][1] is a giant of Systems research. 

> I've really worked in Cloud Computing for most of my career, although it obviously wasn't called cloud computing in the early days. As a result, our papers in this area date back to 1985. Some examples of mission-critical systems on which my software was used in the past include the New York Stock Exchange and Swiss Exchange, the French Air Traffic Control system, the AEGIS warship and a wide range of applications in settings like factory process control and telephony. In fact, every stock quote or trade on the NYSE from 1995 until early 2006 was reported to the overhead trading consoles through software I personally implemented - a cool (but also scary) image, for me at least! During the ten years this system was running, many computers crashed during the trading day, and many network problems have occurred - but the design we developed and implemented has managed to reconfigure itself automatically and kept the overall system up, without exception. They didn't have a single trading disruption during the entire period. As far as I know, the other organizations listed above have similar stories to report.

So what mission critical system has your work ended up in?

Don’t know why I happened to be trawling his Cornell website recently, but it turns out he’s been [publishing a series of essays on the Web][2]. First off, Birman [writes **really** well][3]. This is advanced technical material but fairly accessible. Second, if he says [RDMA is a big deal][4], I’ll just get on the bandwagon and buckle my seatbelt. Actually, the more of his essays I read the more I’m convinced of his position. If the trajectory is right, HPC grade network interconnects will be commoditized and made accessible to average programmers. Sort of like what Hadoop did for Map/Reduce.

If you are at all interested in Systems research, I strongly encourage you to work your way through Ken Birman’s “...Thoughts on Distributed Computing."

[1]: http://www.cs.cornell.edu/ken/
[2]: http://thinkingaboutdistributedsystems.blogspot.com/
[3]: http://thinkingaboutdistributedsystems.blogspot.com/2016/12/hi-im-cornell-faculty-member-who-has.html
[4]: http://thinkingaboutdistributedsystems.blogspot.com/2016/12/rdma2-cutting-through-noise-what-does.html