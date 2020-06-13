Title: Very Tastypie
Date: 2012-02-15 20:27
Author: crossjam
Category: Uncategorized
Slug: very-tastypie
Status: published

[Previously][1] I had posted about tire kicking [Tastypie][2], a toolkit for creating RESTful APIs in Django. Well after a few kicks I think I can recommend it as a good solution for exposing data repositories as Web services. I'm currently using it strictly for read-only access to a relatively simple, but large, database, but getting going was insanely easy. And tastypie turns your Django models into full on REST resources, not a poor RPC over HTTP knockoff.

What really won me over is that I ran into a problem where the default behavior led to a `SELECT COUNT(*)` from a very large table. That’s a no-no in PostgreSQL. Overriding one method to do some raw SQL into a summary table solved the issue.

Bonus, works very nicely with [GeoDjango’s][3] geospatial extensions, which also surprised me with it’s ease of use. Helps that the geobjects have  “convert to JSON methods” that just do the right thing. Worked straight out of the box.

[1]: http://crossjam.net/wp/mpr/2012/02/resting-django/
[2]: http://django-tastypie.readthedocs.org/en/latest/index.html
[3]: http://geodjango.org/