Title: sqlite-utils
Date: 2022-06-24
Author: C. Ross Jam
Status: published

Link parkin’: [sqlite-utils][1]. 

> _CLI tool and Python utility functions for manipulating SQLite databases_

> This library and command-line utility helps create SQLite databases
> from an existing collection of data.

Can’t believe I haven’t stashed Simon Willison’s insanely useful
toolkit on this here blog. Makes it insanely easy to do stuff with
[sqlite][2] databases [from the command line][3] and [from within
Python][4]. [For example][5]

> If you have data as JSON, you can use `sqlite-utils insert tablename`
> to insert it into a database. The table will be created with the
> correct (automatically detected) columns if it does not already
> exist.

[1]: https://sqlite-utils.datasette.io/
[2]: https://sqlite.org/
[3]: https://sqlite-utils.datasette.io/en/stable/cli.html#
[4]: https://sqlite-utils.datasette.io/en/stable/python-api.html
[5]: https://sqlite-utils.datasette.io/en/stable/cli.html#inserting-json-data
