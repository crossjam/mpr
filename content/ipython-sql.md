Title: ipython-sql
Date: 2013-03-30 13:50
Author: crossjam
Category: Uncategorized
Slug: ipython-sql
Status: published

Neat [extension hack of iPython][1] by [Catherine Devlin][2]:
> *RDBMS access via IPython*

> Introduces a %sql (or %%sql) magic.

> Connect to a database, using SQLAlchemy connect strings, then issue SQL commands within IPython or IPython Notebook.

Granted there’s a lot of magic going on, but this speaks to another great feature of iPython, the ability to build up and embed domain specific languages within a nice interactive environment. Knock on effects easily follow, such as rapidly [stuffing SQL query results into pandas][3] for data analytics.

[1]: https://pypi.python.org/pypi/ipython-sql
[2]: http://catherinedevlin.blogspot.com/2013/03/released-sql-magic-for-ipython.html
[3]: http://catherinedevlin.blogspot.com/2013/03/sql-to-pandas.html