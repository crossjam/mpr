Title: RESTful or Restless?
Date: 2012-10-27 19:01
Author: crossjam
Category: Uncategorized
Slug: restful-or-restless
Status: published

In my REST API expeditions at work, I’ve been using [Flask-Restless][1]. Now, via [Python Weekly][3], I find out about [Flask-RESTful][2]. Normally I’d just scan and move on, but RESTful is from folks at Twilio and may have a bit more polish. To wit:

> While Flask provides easy access to request data (i.e. querysting or POST form encoded data), it’s still a pain to validate form data. Flask-RESTful has built-in support for request data validation using a library similar to argparse.

The only hitch I see is no examples of connecting with ORM based models, admittedly after only 10 minutes with the docs. Restless actually handles this use case pretty well.

Alternative approaches are always good to know about.

Also have to say thumbs up on Python Weekly. Once a week to my Inbox, an easy read, at least one good link.

[1]: https://flask-restless.readthedocs.org/en/latest/
[2]: http://flask-restful.readthedocs.org/en/latest/
[3]: http://www.pythonweekly.com/