Title: PostgreSQL Table Functions
Date: 2012-02-25 22:35
Author: crossjam
Category: Uncategorized
Slug: postgresql-table-functions
Status: published

<img src="http://crossjam.net/wp/mpr/wp-content/uploads/2011/09/PostgreSQL-Logo.png" alt="PostgreSQL Logo" border="0" width="120" height="120" align="right" style="margin: 10px;" /> PostgreSQL's [table functions][1] are a pretty handy feature:

> *Table functions are functions that produce a set of rows, made up of either base (scalar) data types, or composite (multi-column) data types. They are used like a table, view, or subselect in the FROM clause of a query. Columns returned by table functions may be included in SELECT, JOIN, or WHERE clauses in the same manner as a table, view, or subselect column.*

Especially when combined with the embedded [procedural languages][2] one can fold a lot of external functionality into typical SQL idioms. Of course I'm sort of partial to the fact that PostgreSQL supports [Python as a procedural language][3] straight out of the box.

[1]: http://www.postgresql.org/docs/9.1/static/queries-table-expressions.html#QUERIES-TABLEFUNCTIONS
[2]: http://www.postgresql.org/docs/9.1/static/xplang.html
[3]: http://www.postgresql.org/docs/9.1/static/plpython.html