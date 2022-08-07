Title: Discogs View Cleanup
Date: 2022-07-10
Author: C. Ross Jam
Status: published

This week I learned about PostgreSQL’s [conditional expressions][2] in
general and the COALESCE expression in particular. A big part of the
grungingess of my [Discogs Postgres views][1] is dealing with the
data’s usage of `alternative name variations` or `anvs` in the
`fabric_track_artists` view which are
quite often NULL. This propagates into a crappy ad hoc value for the
`track_artists` via abuse of `concat_ws`. I’ve got a pretty good
feeling that can be handled more elegantly with a COALESCE.

A couple of other things that need investigating:

1. The regexps for fabric vs fabriclive should be collapsed into one
2. Rename the `fabric_live` column to a more general `fabric_series`
   and compute it from the `title` column
3. Reexamine the UNION statements to see if they can be handled by a
   more appropriate join

Lots of redundancy that can be cleaned up.

[1]: {filename}/discogs_sql_views.md
[2]: https://www.postgresql.org/docs/current/functions-conditional.html
