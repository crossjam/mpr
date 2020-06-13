Title: elasticsearch Cool?
Date: 2012-09-28 19:40
Author: crossjam
Category: Uncategorized
Slug: elasticsearch-cool
Status: published

I’ve had an eye on [elasticsearch][4] for a while now but didn’t really have a good reason to use the Lucene based search engine. Until today that is, when at work I was looking at the use cases I was applying MongoDB towards. I’m not a hater, but MongoDB jus wasn’t fitting the bill.

Time to give elasticsearch a shot. At least [Luca Cava ][1] of [orange11][2] thinks [elasticsearch is cool][3]:
> First of all, what you'll notice as soon as you start up is how easy elasticsearch is to use. You index your JSON documents, then you can make a query and retrieve them, with no configuration needed. One of the reasons is that it's schema-less, which means it uses some nice defaults to index your data unless you specify your own mapping. For more precision it has an automatic type guessing mechanism which detects the type of the fields you are indexing, and it uses by default the Lucene StandardAnalyzer while indexing the string fields.

> If you need something beyond the standard choices you can always define your own mapping, simply using the Put Mapping API. In fact every feature is exposed as a REST API.

Seems auspicious, but we’ll put the engine to the test.

[1]: http://blog.orange11.nl/author/luca/
[2]: http://www.orange11.nl/en/home/about-us
[3]: http://blog.orange11.nl/2012/09/25/whats-so-cool-about-elasticsearch/
[4]: http://elasticsearch.org/