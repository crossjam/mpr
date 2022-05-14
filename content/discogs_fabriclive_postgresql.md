Title: Discogs Data, FabricLive, PostgreSQL

Postgres for extracting FabricLive number from titles:

	select distinct(regexp_matches(title, '(\d+)'))[1]::int as num
	from release where title ~* 'fabriclive\.? ?\d+' order by num;
	
	
