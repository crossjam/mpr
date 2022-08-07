Title: NetNewsWire SQLite Schema
Date: 2022-07-09
Author: C. Ross Jam
Status: published

Just for giggles, following up on [my pondering][1] regarding the SQLite
schema within NetNewsWire, I poked around in the DB and pulled the
schemas:

<!-- PELICAN_END_SUMMARY -->

	:::sql
	SQLite version 3.37.0 2021-12-09 01:34:53
	Enter ".help" for usage hints.
	sqlite> .schema
	CREATE TABLE articles (articleID TEXT NOT NULL PRIMARY KEY, feedID TEXT NOT NULL, uniqueID TEXT NOT NULL, title TEXT, contentHTML TEXT, contentText TEXT, url TEXT, externalURL TEXT, summary TEXT, imageURL TEXT, bannerImageURL TEXT, datePublished DATE, dateModified DATE, searchRowID INTEGER);
	CREATE TABLE statuses (articleID TEXT NOT NULL PRIMARY KEY, read BOOL NOT NULL DEFAULT 0, starred BOOL NOT NULL DEFAULT 0, dateArrived DATE NOT NULL DEFAULT 0);
	CREATE TABLE authors (authorID TEXT NOT NULL PRIMARY KEY, name TEXT, url TEXT, avatarURL TEXT, emailAddress TEXT);
	CREATE TABLE authorsLookup (authorID TEXT NOT NULL, articleID TEXT NOT NULL, PRIMARY KEY(authorID, articleID));
	CREATE INDEX articles_feedID_datePublished_articleID on articles (feedID, datePublished, articleID);
	CREATE INDEX statuses_starred_index on statuses (starred);
	CREATE VIRTUAL TABLE search using fts4(title, body)
	/* search(title,body) */;
	CREATE TABLE IF NOT EXISTS 'search_content'(docid INTEGER PRIMARY KEY, 'c0title', 'c1body');
	CREATE TABLE IF NOT EXISTS 'search_segments'(blockid INTEGER PRIMARY KEY, block BLOB);
	CREATE TABLE IF NOT EXISTS 'search_segdir'(level INTEGER,idx INTEGER,start_block INTEGER,leaves_end_block INTEGER,end_block INTEGER,root BLOB,PRIMARY KEY(level, idx));
	CREATE TABLE IF NOT EXISTS 'search_docsize'(docid INTEGER PRIMARY KEY, size BLOB);
	CREATE TABLE IF NOT EXISTS 'search_stat'(id INTEGER PRIMARY KEY, value BLOB);
	CREATE TRIGGER articles_after_delete_trigger_delete_search_text after delete on articles begin delete from search where rowid = OLD.searchRowID; end;
	CREATE INDEX articles_searchRowID on articles(searchRowID);
	sqlite>
	
So there you go. There’s another layer down of indexes, triggers,
views, and virtual tables but I’ll leave that for another day.

[1]: {filename}/feedbin_to_sqlite.md
