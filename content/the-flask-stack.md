Title: The Flask Stack
Date: 2012-10-12 22:19
Author: crossjam
Category: Uncategorized
Slug: the-flask-stack
Status: published

At work, I’ve been giving [Flask][1] a whirl, with a focus on building a REST based API emitting JSON responses. A much different approach from [Django][2], much more amenable to building an API to my mind. Much less magic, but much lighter weight. And at least for me, a bit easier to understand how to generate RESTful responses.

The biggest part of the learning curve has been [SQLAlchemy][3]. Between the SQL Core for building DB queries, to the object relational mapper *(with two styles of declaring schemas no less)*, to engines, to sessions, there’s a lot going on. Using PostGIS is exacerbating the issue as 1) the geo part needs extensions like [GeoAlchemy][4], and 2) I take advantage of Postgres’ range types, which aren’t baked into SQLAlchemy and are best used with a non-standard operator *(@>)*. So imagine coming to this Swiss Army chainsaw of object relational mapping system and you’re immediately into figuring how to extend the framework. Fun!

Some helpful Flask extensions: [Flask-Restless][5] and [Flask-SQLAlchemy][6]

[1]: http://flask.pocoo.org/
[2]: https://www.djangoproject.com/
[3]: http://www.sqlalchemy.org/
[4]: http://www.geoalchemy.org/
[5]: http://flask-restless.readthedocs.org/en/latest/
[6]: http://github.com/mitsuhiko/flask-sqlalchemy/