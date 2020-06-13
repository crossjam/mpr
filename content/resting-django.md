Title: RESTing Django
Date: 2012-02-10 21:21
Author: crossjam
Category: Uncategorized
Slug: resting-django
Status: published

Previously I had [posted about Sleepy.Mongoose][3], a module for making “RESTful” services out of MongoDB. Turns out Sleepy.Mongoose is really more RPC over HTTP then REST. Plus it seems to be a bit neglected.  I gave it a test drive at work and wasn't feeling very comfortable. So I'm giving Sleepy.Mongoose a pass.

I'm planning to use [Django][4] for some backstage Web administration tools, so thought I'd see if there's anything good for that framework. Ran across [*Tastypie*][2] and looks like it has potential. Especially since there's a clear example of how to wrap a non-Django ORM data sources. Along with continued maintenance and an active community. Kicking the tires this weekend.

Link parkin‘ [*Piston*][1] just in case Tastypie falls through.

[1]: https://bitbucket.org/jespern/django-piston/wiki/Home
[2]: http://django-tastypie.readthedocs.org/en/latest/index.html
[3]: http://crossjam.net/wp/mpr/2012/02/resting-mongodb/
[4]: http://www.djangoproject.com/