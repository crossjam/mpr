Title: plv8
Date: 2011-12-07 21:59
Author: crossjam
Category: Uncategorized
Slug: plv8
Status: published

Given I'm aware of [Python as an embedded procedural language][4] in PostgreSQL, I should have anticipated that someone would stuff JavaScript into PGSQL. Enter [plv8][1]:

> *plv8 is shared library that provides a PostgreSQL procedual language powered by V8 JavaScript Engine. With this program you can write in JavaScript your function that is callable from SQL.*

In the context of PostgreSQL, this means you have a surprisingly useful [durable document store you didn't know you had][2]. The previous link focuses on XML in Postgres, but with plv8 there are plenty of [JSON tricks][3] you can do inside a sophisticated relational data management system.

Don't know how mature plv8 is, but I have a few big piles of Tweet data in JSON format that might be subject to the extension's charms.

*Hat tip to [Hacker News][5]*

[1]: http://code.google.com/p/plv8js/wiki/PLV8
[2]: http://robots.thoughtbot.com/post/13829210385/the-durable-document-store-you-didnt-know-you-had-but
[3]: http://pgeu-plv8.herokuapp.com/
[4]: http://www.postgresql.org/docs/9.1/static/plpython.html
[5]: http://news.ycombinator.com/item?id=3320054