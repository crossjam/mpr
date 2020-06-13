Title: Pelican Search with Tipue
Date: 2020-05-31 21:00
Author: crossjam
Category: Uncategorized
Slug: pelican-search-with-tipue
Status: published

Inching my way towards using the Pelican static site generator for this blog, I realized that search is actually a must have. The path of least resistance seems to be to use the [Tipue Search plugin][1]. [Tipue Search][2] basically takes a statically generated search index as a big wad of JavaScript and does search client side. Not sure about the overall merits of this approach but it looks like a lot less hassle than deploying a parallel self-hosted search engine, especially after going to the trouble of static site generation to begin with. Then again, figuring the search part could be a fun side project.

Alternatively, looks like [incorporating Algolia][4] wouldn’t be too challenging.

*Hat tip to this [tutorial by Maxime Laboissonniere][3].*

[1]: https://github.com/getpelican/pelican-plugins/tree/master/tipue_search
[2]: https://tipue.com/search/
[3]: https://snipcart.com/blog/pelican-blog-tutorial-search-comments
[4]: https://devops.datenkollektiv.de/finally-pelican-with-algolia-search.html