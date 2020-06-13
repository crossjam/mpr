Title: rqlite
Date: 2017-06-20 20:27
Author: crossjam
Category: Uncategorized
Slug: rqlite
Status: published

Just because I dig the many cool uses [SQLite][2] has been put to:

> [rqlite][1] is a distributed relational database, which uses SQLite as its storage engine. rqlite uses Raft to achieve consensus across all the instances of the SQLite databases, ensuring that every change made to the system is made to a quorum of SQLite databases, or none at all. It also gracefully handles leader elections, and tolerates failures of machines, including the leader. rqlite is available for Linux, OSX, and Microsoft Windows.

[1]: https://github.com/rqlite/rqlite
[2]: http://www.sqlite.org