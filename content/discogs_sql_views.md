Title: Discogs Data SQL Views
Category: discogs

Well that was a mildly annoying adventure discovering how to get code
syntax highlighting. Pelican’s markdown support includes [CodeHilite][2] by
default but I couldn’t figure out how to actually trigger. Turns out
once I installed the [Pygments][3] module, things kicked in.

Anyway, who knew the language of the first code segment to appear on this blog would
be SQL? Using some handy regular expression features of Postgres, I
layered some views on top of data imported from
[discogs-xml2db][1]. The target was getting an extraction of releases from
the Fabric and FabricLive series. Still a fair amount of data normalization
to be done, but at least I’ve got 100% recall with not too much extra
stuff and that only because the titles aren’t quite consistent.

Code and example output below the fold

<!-- PELICAN_END_SUMMARY -->

	:::sql
	create materialized view if not exists fabric_releases as
       (select release.id as release_id, master.id as master_id, release.title,
               (regexp_matches(release.title, 'Fabric\.? ?(\d+)', 'gi'))[1]::int as num
           from release, master where release.title ~* 'fabric\.? ?\d+' and
	   release.master_id is not null and
           master.id = release.master_id and release.id = master.main_release)
        union
       (select release.id as release_id, release.master_id as master_id, release.title,
               (regexp_matches(release.title, 'Fabric\.? ?(\d+)', 'gi'))[1]::int as num
        from release where release.title ~* 'fabric\.? ?\d+' and
        release.master_id is null);
		
	create materialized view if not exists fabriclive_releases as
       (select release.id as release_id, master.id as master_id, release.title,
               (regexp_matches(release.title, 'FabricLive\.? ?(\d+)', 'gi'))[1]::int as num
        from release, master where release.title ~* 'fabriclive\.? ?\d+' and
        master.id = release.master_id and release.id = master.main_release)
       union
       (select release.id as release_id, release.master_id as master_id, release.title,
               (regexp_matches(release.title, 'FabricLive\.? ?(\d+)', 'gi'))[1]::int as num
        from release where release.title ~* 'fabriclive\.? ?\d+' and
        release.master_id is null);

_need to put an example of querying against the views here_

[1]: https://github.com/philipmat/discogs-xml2db
[2]: https://python-markdown.github.io/extensions/code_hilite/
[3]: https://pygments.org/languages/
