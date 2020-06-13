Title: Jepp, CPython and Java
Date: 2013-05-17 17:58
Author: crossjam
Category: Uncategorized
Slug: jepp-cpython-and-java
Status: published

TIL about [Jepp][1]:
> Jepp embeds CPython in Java. It is safe to use in a heavily threaded environment, it is quite fast and its stability is a main feature and goal. 

Could be handy for cutting down performance overhead at some points in the Hadoop stack where Python and Java come together. I’m looking at you [Hadoop Streaming][2]. Also for helping Python out with the myriad of serialization formats that Java does oh so well.

[*Via Morten Petersen*][3]

[1]: http://jepp.sourceforge.net/
[2]: http://hadoop.apache.org/docs/stable/streaming.html
[3]: http://www.nidelven-it.no/weblogs/hosting/blog_entry?id=1368634033X37