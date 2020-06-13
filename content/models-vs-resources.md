Title: Models vs Resources
Date: 2012-12-08 16:22
Author: crossjam
Category: Uncategorized
Slug: models-vs-resources
Status: published

This [nugget from Jacob Kaplan-Moss][1] is a bit old, and from a Django-centric perspective, but captures what’s been tripping me up with Python web app frameworks and building RESTful APIs:
> **Conflating models and resources**

> In the REST world, the resource is key, and it’s really tempting to simply look at a Django model and make a direct link between resources and models — one model, one resource. This fails, though, as soon as you need to provide any sort of aggregated resource, and it really fails with highly denormalized models. Think about a Superhero model: a single `GET /heros/superman/`ought to return all his vital stats along with a list of related Power objects, a list of his related Friend objects, etc. So the data associated with a resource might actually come out of a bunch of models. Think `select_related()`, except arbitrary.

[1]: http://jacobian.org/writing/rest-worst-practices/