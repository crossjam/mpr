Title: HDFS Gets Snakebitten
Date: 2013-05-18 16:35
Author: crossjam
Category: Uncategorized
Slug: hdfs-gets-snakebitten
Status: published

[!embed](https://twitter.com/pypi/status/335412456396558336)

Another good find from the PyPi Twitter stream. Had to do a quick Google search to get [the real details][1] on [snakebite][2], a pure Python library for interacting with Hadoop’s HDFS:
> Another annoyance we had with Hadoop (and in particular HDFS) is that interacting with it is quite slow. For example, when you run `hadoop fs -ls /`, a Java virtual machine is started, a lot of Hadoop JARs are loaded and the communication with the NameNode is done, before displaying the result. This takes at least a couple of seconds and can become slightly annoying. This gets even worse when you do a lot of existence checks on HDFS; something we do a lot with luigi, to see if output of a jobs exist.

> ...

> So, to circumvent slow interaction with HDFS and having a native solution for Python, we’ve created Snakebite, a pure Python HDFS client that only uses Protocol Buffers to communicate with HDFS. And since this might be interesting for others, we decided to Open Source it at [http://github.com/spotify/snakebite][2].

Roger that on the annoyingly slow response of `hadoop fs`. Thanks Spotify.

[1]: http://labs.spotify.com/2013/05/07/snakebite/
[2]: http://github.com/spotify/snakebite