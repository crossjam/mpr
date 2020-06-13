Title: Whatabouts
Date: 2015-11-24 17:13
Author: crossjam
Category: Uncategorized
Slug: whatabouts
Status: published

Stuff I’m currently interested in and will probably frequently comment on here. First off on the technical front:

<!--more-->

* Processing of streaming data. On the day job, I’ve deeply embraced [Apache Kafka][1]. We haven’t had much success doing the actual data processing, but the [Googlish][3] ([among others][4]) concepts of [*unbounded processing*][2] are attractive.
* Speaking of which [Apache Spark][5] *(Go Bears!)*, is still of high attention, especially Spark Streaming.
* [Distributed consensus algorithms][6], ala Paxos, ZAB, Raft, et. al. Also toolkits such as [Zookeeper][7], [Consul][8], [etcd][9] which leverage these algorithms to additionally enable service discovery.
* [Containerization][11], principally [Docker][10] but also getting back to [LXC][12] and [BSD jails][13], the originals. [Unikernels][14] fall into the same space although I’m still trying to make sense of them.
* Programming languages. Still primarily a Pythonista, actually [contributed some Go][17] to an open source project, getting dragged into Scala and back into Java due to Spark/Kafka, soft spot always for Common Lisp, Scheme and their ancestors
* Dev tools and practices. The day job has made me a passable [git][18] user, an emerging test driven developer, and well aware of continuous integration and continuous deployment practices. Planning to actually top up my skills on modern SW development environments.
* Performance monitoring and analysis. I’ve gladly joined the cult of [Brendan Gregg][19]. It’s a very interesting and underserved area, that integrates a lot of interesting technologies, engineering techniques, and analysis methodologies. Proficiency in this domain seems to be a bit of a superpower.

The overall technical theme is what I’ll term “distributed programming in the small”. I’ve come to grips with the realization that my dreams of becoming a massive scale systems builder are probably not going to come true. Google, Amazon, Facebook, Netflix et. al. have moved the goal posts so far out that unless you work at one of those places, or a scientific computing institution, you’re pretty much an amateur. However, there are plenty of use cases that can exploit key technologies from that crowd to build *reliable* and dynamic data processing systems even without having to reach global scale. Plenty of problems still out there that force you to use more than one computer at a time. But when you go that route, to the extent reasonable, do what the pros do.

Musically still diggin’ on House, DnB, downtempo, trip-hop, and breaks DJ mixes. Find myself going retro a bit more into 80’s, less so 90’s, pop and dance through a [Spotify Premium][15] account. I pay for mixes and subscribe for singles.

Crate diggin’ through all the old material I have in the form of old blog posts, RSS feed stars, Twitter faves *(F likes)*, and [pinboard bookmarks][22]. Having been around for a while now affords me the space to do some reflection in addition to observation.

Not so much:

* TV. Cut off [the national drip][21] about a year ago. Mental and emotional health much improved.
* Sports. **Really** dialed it back. It mostly went out the window with the One Eyed Monster. Basically do audio streams of games while conducting other activities, visit the Verizon Center to watch The Wiz with my dad, and check scores on my phone every now and then. Finding the NFL and NCAA despicable.
* Science fiction reading. It’s become intermittent due to Life (TM). If I get back on the bandwagon it’ll make a return but “underpromise and overdeliver”.
* Movie stuff. Ditto. In the last two calendar years, I’ve seen exactly one feature film in the theater: [*Mad Max: Fury Road*][16]. Highly recommended but again, I don’t get out for entertainment much. There’s a plethora of on-demand at my disposal, but can’t muster the energy to take advantage.
* Social media. I’ve been around long enough to remember when the notion of “IRL: In Real Life” made sense and we called it [“social software”][20]. Now it’s All Real Life, All The Time and increasingly disruptive of our social fabric, (*not in a good way*).
* Celebrity. You can get plenty of that in other venues.

Consider yourselves, ... warned.

[1]: http://kafka.apache.org/
[2]: http://radar.oreilly.com/2015/08/the-world-beyond-batch-streaming-101.html
[3]: http://radar.oreilly.com/2015/11/building-systems-for-massive-scale-data-applications.html
[4]: https://flink.apache.org/
[5]: http://spark.apache.org/
[6]: http://blog.acolyer.org/2015/03/01/cant-we-all-just-agree/
[7]: http://zookeeper.apache.org/
[8]: https://www.consul.io/
[9]: https://github.com/coreos/etcd
[10]: http://www.docker.com/
[11]: http://thenewstack.io/tag/the-docker-and-container-ecosystem/
[12]: https://linuxcontainers.org/
[13]: http://phk.freebsd.dk/sagas/jails.html
[14]: https://ma.ttias.be/what-is-a-unikernel/
[15]: https://www.spotify.com/us/premium/
[16]: http://www.imdb.com/title/tt1392190/
[17]: https://github.com/nsqio/nsq/releases/tag/v0.2.29
[18]: http://git-scm.org/
[19]: http://www.brendangregg.com/index.html
[20]: http://crossjam.net/wp/nmh/archives/000251
[21]: https://en.wikipedia.org/wiki/The_Disposable_Heroes_of_Hiphoprisy
[22]: https://pinboard.in/u:crossjam