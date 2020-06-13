Title: Django API Frameworks
Date: 2012-05-15 21:57
Author: crossjam
Category: Uncategorized
Slug: django-api-frameworks
Status: published

Daniel Greenfeld compares and contrasts [Django toolkits for creating REST APIs][1]. I’m interested in other perspectives on this topic as I’ve [talked about tastypie before][2] and actually put it in practice at work. 

On site comments for the post and [over at HackerNews][3] are useful as well. In particular, I have to agree with a few folks that tastypie is pretty good for fairly standard Django models, but gets a little tricky for non-ORM or search based resources. In particular, dealing with object dehydration and response URIs was a bit opaque. I may be hallucinating, but when I first got started with tastypie, this [documentation node on the request/response cycle][4] didn’t exist. Maybe it’ll clear up my confusion.

I’d still recommend tastypie, but for advanced uses prepare to spend some time digging into module source code and doing a lot of experimentation to get the right results. As you’d expect!

[1]: http://pydanny.com/choosing-an-api-framework-for-django.html
[2]: http://crossjam.net/wp/mpr/2012/02/very-tastypie/
[3]: http://news.ycombinator.com/item?id=3954314
[4]: http://django-tastypie.readthedocs.org/en/latest/resources.html#flow-through-the-request-response-cycle