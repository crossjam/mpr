Title: Python API Building
Date: 2012-10-20 19:37
Author: crossjam
Category: Uncategorized
Slug: python-api-building
Status: published

Nice 4 step tutorial on [building a RESTful API][1] using Python, by K. P. Kaiser. The best tip was a pointer to [elasticutils][2], an ElasticSearch library:
> It’s always a good idea to see what your options are in a library. Initially, when I was building this integration I saw pyes, a very well written library, but the code to use it seemed a bit ugly for my tastes.

> Luckily, after a bit more searching, I found elasticutils, which is, in my opinion, a much cleaner interface to the very simple elasticsearch server. It always pays to take a few minutes to read the introduction, and example code before deciding on a library. Elasticutils actually uses pyes under the covers.

[1]: http://www.kpkaiser.com/articles/building-and-deploying-your-first-api-in-python/
[2]: http://elasticutils.readthedocs.org/en/latest/index.html