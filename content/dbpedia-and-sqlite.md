Title: DBPedia and SQLite
Date: 2012-12-26 21:20
Author: crossjam
Category: Uncategorized
Slug: dbpedia-and-sqlite
Status: published

[DBpedia][1] has always felt like a great resource to me, but I’ve never taken the time to play with the data, being somewhat daunted by [RDF][2] and [triplestores][3].

Jean-Louis Fuchs has done yeoman’s work in creating [a repository of DBpedia infoboxes in SQLite][4] and releasing his import script. May have to grab and experiment with.
> When I learned about DBpedia, I wanted to have it installed locally, I read the tutorials on sparql and how to install DBpedia: that has to be simpler. I kind of worship Simple and I didn't want to learn yet another query language. So I hacked an SQLite import script for DBpedia types and infobox-properties in one evening. The script takes about 50 hours to read instance_types_en.nt and infobox_properties_en.nt. It creates a table per type and a table per property, after tables are created everything gets an index, the whole database is analyzed and finally vacuumed.

An aside thought, wonder if there’s a straightforward way to take DBpedia data and stuff it into a full text indexing system like ElasticSearch? You’d give up the reasoning properties of a SPARQL based triplestore, but would have quick and dirty access to a significant semi-structured knowledge repository.

[1]: http://dbpedia.org/About
[2]: http://en.wikipedia.org/wiki/Resource_Description_Framework
[3]: http://en.wikipedia.org/wiki/Triplestore
[4]: http://ganwellresource.blogspot.com/2012/12/dbpedia-in-sqlite.html