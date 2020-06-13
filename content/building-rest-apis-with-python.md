Title: Building REST APIs with Python
Date: 2012-08-04 21:58
Author: crossjam
Category: Uncategorized
Slug: building-rest-apis-with-python
Status: published

In my Copious Spare Time ™, I’m thinking about how one can rapidly build, lightweight, fast REST APIs using Python. I may [revisit Django approaches][1] again, but the heavy dependency on an RDBMS and a model-based Object-Relational Manager (ORM) makes it feel like I’m fighting against the toolkit. The key issue is that to get performance for some aspects, I’m anticipating the need for other data stores such as a [full-text index][2] or [a NoSQL repository][3]. Thinking one of the Python web micro-frameworks, possibly [Flask][4], might be the right fit.

*Wow! It’s been a long time since I talked about [Redis][5]. It’s up to version 2.4.x now.*

[1]: http://crossjam.net/wp/mpr/2012/05/django-api-frameworks/ 
[2]: http://crossjam.net/wp/mpr/2012/01/i-heart-sphinx/
[3]: http://crossjam.net/wp/mpr/2009/11/redis_key-datastructure_store/
[4]: http://flask.pocoo.org/
[5]: http://redis.io/