Title: Strata Trip Reports
Date: 2013-03-04 21:03
Author: crossjam
Category: Uncategorized
Slug: strata-trip-reports
Status: published

Michael Malak does yeoman’s work writing up his observations ([Days 0 & 1][1], [Day 2][2], [Day 3][3]) of the Strata Conference Santa Clara. First knock on Storm I’ve heard of:
> Spark streaming, according to the presented, beats its competitor Storm at calculating metrics on the fly as they come off a queue like Kafka or Flume because Spark has fault-tolerance through node redundancy and because Spark avoids Storm's problem of double-counting events by maintaining full historical data in memory for the specified desired window (e.g. 10 minutes). He said there is a layer over Storm that can prevent double-counting, but it achieves it by wrapping each individual event in its own transaction, and most users just abandon that solution for being non-performant.

> ...

> In a barely audible aside during the presentation, they confirmed the weakness of Storm that was stated during the previous day's Spark Streaming presentation, which is that the layer on top of Storm, Trident, that prevents double-counting is not performant.

[1]: http://www.meetup.com/Data-Science-Business-Analytics/messages/boards/thread/31886742
[2]: http://www.meetup.com/Data-Science-Business-Analytics/messages/boards/thread/31927912
[3]: http://www.meetup.com/Data-Science-Business-Analytics/messages/boards/thread/31966292