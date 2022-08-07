Title: Feedbin to sqlite
Date: 2022-07-08
Author: C. Ross Jam
Status: published

Thinking out loud. With a nice library around [the Feedbin API][1] it
wouldn’t be too hard to grab the data and stuff it into
SQLite. Alternatively, a Feedbin account could be registered with
[NetNewsWire][3] and then [the underlying SQLite DB][2] inspected.

The former seems more elegant while the latter is radically pragmatic.

If for nothing else, poking around in the NetNewsWire SQLite DB
probably illustrates a highly performant SQL data model and schemas
for RSS data and feed management. Or even better, just read [the source code][4]

[1]: {filename}/feedbin_api.md
[2]: https://talk.macpowerusers.com/t/i-was-desperately-searching-for-a-way-to-export-my-netnewswire-entries-and-i-accidentally-learned-that-its-all-stored-in-an-sqlite-database/27858
[3]: https://netnewswire.com/
[4]: https://github.com/Ranchero-Software/NetNewsWire
