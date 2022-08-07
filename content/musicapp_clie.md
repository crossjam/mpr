Title: musicapp cli
Author: C. Ross Jam
Date: 2022-06-26
Status: published

It’s a small start, but my [`musicapp`][1] command line utility, for
working with XML out of Apple’s Music.app, can be used in a one liner
with `sqlite-utils`:

<!-- PELICAN_END_SUMMARY -->

	:::bash
	xonsh 🐚 > ~/D/Fabric > ! > musicapp --log-level debug fabric missing --fmt csv | \
		sqlite-utils insert missing.db missing - --csv
	xonsh 🐚 > ~/D/Fabric > sqlite3 missing.db
	SQLite version 3.37.0 2021-12-09 01:34:53
	Enter ".help" for usage hints.
	sqlite> select * from missing;
	7|fabric 7 - Hipp-E & Halo
	11|fabric 11 - Swayzak
	12|fabric 12 - The Amalgamation Of Sounds
	13|fabric 13 - Michael Mayer
	15|fabric 15 - Tyrant
	16|fabric 16 - Eddie Richards
	17|fabric 17 - Akufen
	18|fabric 18 - Baby Mammoth
	19|fabric 19 - Andrew Weatherall
	22|fabric 22 - Adam Beyer
	54|fabric 54 - Damian Lazarus
	59|fabric 59 - Jamie Jones
	83|fabric 83 - Joris Voorn
	84|fabric 84 - Mathew Jonson
	100|fabric 100 - Craig Richards, Terry Francis, Keith Reilly
	sqlite>
	sqlite> select count(*) from missing;
	15
	sqlite>

Now I actually know which Fabric releases I haven’t entered into my
Music.app library. Next up Fabric Live accounting.

[1]: https://github.com/crossjam/musicapp
