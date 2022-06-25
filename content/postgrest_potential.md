Title: PostgREST Potential
Date: 2022-06-06
Author: C. Ross Jam
Status: published

First off, I really need to generate some basic
<del>discriminative</del> descriptive statistics across all of this
Discogs data. Pick off the low hanging fruit.

Having said that, since I’ve got the data in a PostgreSQL instance,
including [my own custom views][2], some kind of HTTP based API to access
the data would provide an interesting prototype.

Enter [PostgREST][1]

> PostgREST is a standalone web server that turns your PostgreSQL
> database directly into a RESTful API. The structural constraints and
> permissions in the database determine the API endpoints and
> operations.

What would [oEmbed][3] cards look like for pure textual playlists?

[1]: https://postgrest.org/en/stable/
[2]: {filename}/discogs_sql_views.md
[3]: https://oembed.com/
