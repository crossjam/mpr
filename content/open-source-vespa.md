Title: Open Source Vespa
Date: 2017-09-27 20:14
Author: crossjam
Category: Uncategorized
Slug: open-source-vespa
Status: published

At first I was set to be disappointed [when hearing of][2] a new, open source, big data platform named [Vespa][3]. Then I read this graf from [the team’s announcement blog post][1]:

> Serving often involves more than looking up items by ID or computing a few numbers from a model. Many applications need to compute over large datasets at serving time. Two well-known examples are search and recommendation. To deliver a search result or a list of recommended articles to a user, you need to find all the items matching the query, determine how good each item is for the particular request using a relevance/recommendation model, organize the matches to remove duplicates, add navigation aids, and then return a response to the user. As these computations depend on features of the request, such as the user’s query or interests, it won’t do to compute the result upfront. It must be done at serving time, and since a user is waiting, it has to be done fast. Combining speedy completion of the aforementioned operations with the ability to perform them over large amounts of data requires a lot of infrastructure – distributed algorithms, data distribution and management, efficient data structures and memory management, and more. This is what Vespa provides in a neatly-packaged and easy to use engine.

Check out the blog post. It also details how Vespa actually impacted the bottom line, in a big way, of a number of Oath (neé Yahoo!) properties. 

[1]: http://blog.vespa.ai/post/165763618906/open-sourcing-vespa-yahoos-big-data-processing
[2]: https://www.oreilly.com/ideas/four-short-links-27-september-2017
[3]: http://vespa.ai/