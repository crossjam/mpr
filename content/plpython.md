Title: PL/Python
Date: 2011-09-30 21:59
Author: crossjam
Category: Uncategorized
Slug: plpython
Status: published
Attachments: wp/mpr/wp-content/uploads/2011/09/PostgreSQL-Logo.png

[<img src="http://crossjam.net/wp/mpr/wp-content/uploads/2011/09/PostgreSQL-Logo.png" alt="PostgreSQL Logo" border="0" width="120" height="120" align="right" style="margin: 10px;" />][1] Been noodling around with [PostgreSQL][1] at work. Great relational database system. Glad I got a chance to get back to it. Gets even better with age.

For the longest time, I'd never really used stored procedures in an RDBMS because the languages to write the procedures were unappealing. However, PostgreSQL has embedded scripting languages, [including Python][2], as procedural languages. Makes things a lot more fun.

One caveat, it was pretty tricky to convince the PostgreSQL build process on MacOS Lion to not use the system Python. An important point if you don't have root privileges to install modules, which comes in handy. I'll have to look up the mods and post them since it could save someone a little bit of time.

[1]: http://www.postgresql.org/
[2]: http://www.postgresql.org/docs/9.1/interactive/plpython.html