Title: Discogs Data SQL Views
Date: 2022-06-05
Author: C. Ross Jam
Category: discogs
Status: published

_This sat in the drafts folder for a bit, but I finally decided to just
hit publish and stop seeking perfection._

Well that was a mildly annoying adventure discovering how to get code
syntax highlighting working. Pelican’s markdown support includes
[CodeHilite][2] by default but I couldn’t figure out how to actually
trigger. Turns out once I installed the [Pygments][3] module, things
kicked in.

Anyway, who knew the language of the first code segment to appear on
this blog would be SQL? Using some handy regular expression features
of Postgres, I layered some views on top of data imported from
[discogs-xml2db][1]. The target was getting an extraction of releases
from the [Fabric][4] and [FabricLive][5] series. Still a fair amount of data
normalization needed to be done, but at least I’ve got 100% recall
with not too much extra stuff and that’s only because the titles
aren’t quite consistent. Ultimately had to resort to explicitly black
listing some rows

Code and example output below the fold

<!-- PELICAN_END_SUMMARY -->

After a few iterations, here’s where I’m currently at. On one hand I’m
satisfied at the results. On the other, I’m sure a Postgres expert
would cringe at this, plus I feel there are better ways to do some of
what I’m doing. I’m pretty sure joining variadic results as in
`fabric_tracks_artists` has a more idiomatic Postgres expression. 

	:::sql
	create materialized view if not exists fabric_releases as
		   (select false as fabric_live, release.id as release_id, master.id as master_id, release.title,
				   (regexp_matches(release.title, 'Fabric\.? ?(\d+)', 'gi'))[1]::int as fabric_num
			   from release, master where release.title ~* 'fabric\.? ?\d+' and
		   not release.title ~* 'Radio Mix' and
		   release.master_id is not null and
		   release.status = 'Accepted' and
		   not release.title ~* 'Sampler' and
		   release.id not in (select * from fabric_release_blacklist) and
			   master.id = release.master_id and release.id = master.main_release)
			union
		   (select false as fabric_live, release.id as release_id, release.master_id as master_id, release.title,
				   (regexp_matches(release.title, 'Fabric\.? ?(\d+)', 'gi'))[1]::int as fabric_num
			from release where release.title ~* 'fabric\.? ?\d+' and
		   not release.title ~* 'Radio Mix' and
		   release.status = 'Accepted' and
		   not release.title ~* 'Sampler' and
		   release.id not in (select * from fabric_release_blacklist) and
			   release.master_id is null)
		union
		   (select true as fabric_live, release.id as release_id, master.id as master_id, release.title,
				   (regexp_matches(release.title, 'FabricLive\.? ?(\d+)', 'gi'))[1]::int as fabric_num
			from release, master where release.title ~* 'fabriclive\.? ?\d+' and
		not release.title ~* 'Radio Mix' and
		release.status = 'Accepted' and
		not release.title ~* 'Sampler' and
		release.id not in (select * from fabric_release_blacklist) and
			master.id = release.master_id and release.id = master.main_release)
		   union
		   (select true as fabric_live, release.id as release_id, release.master_id as master_id, release.title,
				   (regexp_matches(release.title, 'FabricLive\.? ?(\d+)', 'gi'))[1]::int as fabric_num
			from release where release.title ~* 'fabriclive\.? ?\d+' and
		not release.title ~* 'Radio Mix' and
		release.status = 'Accepted' and
		not release.title ~* 'Sampler' and
		release.id not in (select * from fabric_release_blacklist) and
			release.master_id is null);

	create materialized view if not exists fabric_tracks as
	select
		fabric_releases.fabric_num as fabric_num,
		fabric_releases.fabric_live as fabric_live,
		fabric_releases.release_id as release_id,
		release.title as release_title,
		release_track.id as track_id,
		release_track.title as track_title,
		release_track.sequence as track_sequence,
		release_track.position as track_position
	from fabric_releases, release, release_track
	where fabric_releases.release_id is not null
		and fabric_releases.release_id = release.id
		and release_track.release_id = release.id;

	create materialized view if not exists fabric_tracks_artists as
	select
	fabric_tracks.track_id as track_id,
	array_agg(concat_ws(' ', concat_ws(':', format('[%s]', anv), format('[%s]', artist_name)), join_string)  order by position) as track_artists
	from fabric_tracks left join release_track_artist on (fabric_tracks.track_id = release_track_artist.track_id)
	where not release_track_artist.extra
		and fabric_tracks.track_position is not null
	group by fabric_tracks.track_id, release_track_artist.track_sequence;

And here’s an example of querying against the views using
`pgcli`. These are the tracks from one of my favorite mixes,
[Fabriclive.25: High Contrast][6]

	:::bash
	crossjam@localhost:discogs> select * from fabric_tracks where fabric_num = 25 and fabric_live;
	+------------+-------------+------------+----------------+----------+-------------------------------+----------------+----------------+
	| fabric_num | fabric_live | release_id | release_title  | track_id | track_title                   | track_sequence | track_position |
	|------------+-------------+------------+----------------+----------+-------------------------------+----------------+----------------|
	| 25         | True        | 560721     | FabricLive. 25 | 3044071  | 8ball                         | 1              | 1              |
	| 25         | True        | 560721     | FabricLive. 25 | 3044072  | Power Ballad                  | 2              | 2              |
	| 25         | True        | 560721     | FabricLive. 25 | 3044073  | Restart                       | 3              | 3              |
	| 25         | True        | 560721     | FabricLive. 25 | 3044074  | Life Rhythm                   | 4              | 4              |
	| 25         | True        | 560721     | FabricLive. 25 | 3044075  | Flashback                     | 5              | 5              |
	| 25         | True        | 560721     | FabricLive. 25 | 3044076  | Desperate Housewives          | 6              | 6              |
	| 25         | True        | 560721     | FabricLive. 25 | 3044077  | Nxt 2 U                       | 7              | 7              |
	| 25         | True        | 560721     | FabricLive. 25 | 3044078  | Ghetto Blaster                | 8              | 8              |
	| 25         | True        | 560721     | FabricLive. 25 | 3044079  | Woe                           | 9              | 9              |
	| 25         | True        | 560721     | FabricLive. 25 | 3044080  | Strength 2 Strength           | 10             | 10             |
	| 25         | True        | 560721     | FabricLive. 25 | 3044081  | The Big Picture               | 11             | 11             |
	| 25         | True        | 560721     | FabricLive. 25 | 3044082  | Love Insane                   | 12             | 12             |
	| 25         | True        | 560721     | FabricLive. 25 | 3044083  | Soul Function                 | 13             | 13             |
	| 25         | True        | 560721     | FabricLive. 25 | 3044084  | Solar Burn                    | 14             | 14             |
	| 25         | True        | 560721     | FabricLive. 25 | 3044085  | Summer Sun                    | 15             | 15             |
	| 25         | True        | 560721     | FabricLive. 25 | 3044086  | What's Happening?             | 16             | 16             |
	| 25         | True        | 560721     | FabricLive. 25 | 3044087  | Real McCoy                    | 17             | 17             |
	| 25         | True        | 560721     | FabricLive. 25 | 3044088  | Bitch I'm Gone                | 18             | 18             |
	| 25         | True        | 560721     | FabricLive. 25 | 3044089  | Going In Circles (A.I. Remix) | 19             | 19             |
	| 25         | True        | 560721     | FabricLive. 25 | 3044090  | Hell Hath No Fury             | 20             | 20             |
	| 25         | True        | 560721     | FabricLive. 25 | 3044091  | Rapture                       | 21             | 21             |
	| 25         | True        | 560721     | FabricLive. 25 | 3044092  | Days Go By                    | 22             | 22             |
	+------------+-------------+------------+----------------+----------+-------------------------------+----------------+----------------+
	SELECT 22
	Time: 0.016s
	crossjam@localhost:discogs>	

I cooked up a little CLI app using Python and `click` for querying
releases and tracks. I need to plug in a flexible row output formatter
so CSV, json, etc. results can be delivered.
	
	:::bash
	(discogsdata) crossjam@GabrielHounds:~$ discogsdata fabric tracks --live 25
	('fabric_num', 'release_id', 'release_title', 'release_artist', 'track_id', 'track_sequence', 'track_position', 'track_title', 'track_artists')
	(25, 560721, 'FabricLive. 25', '[]:[High Contrast]', 3044071, 1, '1', '8ball', '[]:[Adam F]')
	(25, 560721, 'FabricLive. 25', '[]:[High Contrast]', 3044072, 2, '2', 'Power Ballad', '[]:[London Elektricity]')
	(25, 560721, 'FabricLive. 25', '[]:[High Contrast]', 3044073, 3, '3', 'Restart', '[]:[DJ Marky] , []:[Bungle] & []:[DJ Roots]')
	(25, 560721, 'FabricLive. 25', '[]:[High Contrast]', 3044074, 4, '4', 'Life Rhythm', '[]:[Logistics]')
	(25, 560721, 'FabricLive. 25', '[]:[High Contrast]', 3044075, 5, '5', 'Flashback', '[]:[Cyantific] Vs []:[Logistics]')
	(25, 560721, 'FabricLive. 25', '[]:[High Contrast]', 3044076, 6, '6', 'Desperate Housewives', '[]:[Funky Technicians]')
	(25, 560721, 'FabricLive. 25', '[]:[High Contrast]', 3044077, 7, '7', 'Nxt 2 U', '[]:[Martyn]')
	(25, 560721, 'FabricLive. 25', '[]:[High Contrast]', 3044078, 8, '8', 'Ghetto Blaster', '[]:[Cyantific]')
	(25, 560721, 'FabricLive. 25', '[]:[High Contrast]', 3044079, 9, '9', 'Woe', '[Jenna G]:[Jenna Gibbons]')
	(25, 560721, 'FabricLive. 25', '[]:[High Contrast]', 3044080, 10, '10', 'Strength 2 Strength', '[Matrix Vs Futurebound]:[Matrix & Futurebound]')
	(25, 560721, 'FabricLive. 25', '[]:[High Contrast]', 3044081, 11, '11', 'The Big Picture', '[]:[Artificial Intelligence]')
	(25, 560721, 'FabricLive. 25', '[]:[High Contrast]', 3044082, 12, '12', 'Love Insane', '[]:[Craggz & Parallel Forces]')
	(25, 560721, 'FabricLive. 25', '[]:[High Contrast]', 3044083, 13, '13', 'Soul Function', '[]:[Danny Byrd]')
	(25, 560721, 'FabricLive. 25', '[]:[High Contrast]', 3044084, 14, '14', 'Solar Burn', '[]:[Blame]')
	(25, 560721, 'FabricLive. 25', '[]:[High Contrast]', 3044085, 15, '15', 'Summer Sun', '[]:[Logistics]')
	(25, 560721, 'FabricLive. 25', '[]:[High Contrast]', 3044086, 16, '16', "What's Happening?", '[Chris S.U. & SKC]:[Chris.Su & SKC]')
	(25, 560721, 'FabricLive. 25', '[]:[High Contrast]', 3044087, 17, '17', 'Real McCoy', '[]:[State Of Mind (8)]')
	(25, 560721, 'FabricLive. 25', '[]:[High Contrast]', 3044088, 18, '18', "Bitch I'm Gone", '[]:[Nero (5)]')
	(25, 560721, 'FabricLive. 25', '[]:[High Contrast]', 3044089, 19, '19', 'Going In Circles (A.I. Remix)', '[]:[Total Science]')
	(25, 560721, 'FabricLive. 25', '[]:[High Contrast]', 3044090, 20, '20', 'Hell Hath No Fury', '[]:[Klute]')
	(25, 560721, 'FabricLive. 25', '[]:[High Contrast]', 3044091, 21, '21', 'Rapture', '[]:[Sparfunk] & []:[Joe Solo (2)]')
	(25, 560721, 'FabricLive. 25', '[]:[High Contrast]', 3044092, 22, '22', 'Days Go By', '[]:[High Contrast]')
	(discogsdata) crossjam@GabrielHounds:~$
	
Endless possibilities for improvement.

[1]: https://github.com/philipmat/discogs-xml2db
[2]: https://python-markdown.github.io/extensions/code_hilite/
[3]: https://pygments.org/languages/
[4]: https://www.discogs.com/label/1115423-Fabric-3?page=1&limit=250
[5]: https://www.discogs.com/label/348990-FabricLive?page=1&genre=All&limit=250
[6]: https://www.discogs.com/release/560721-High-Contrast-FabricLive-25
