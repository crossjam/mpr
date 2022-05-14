Title: Discogs Data Hacking (DDH), End of the Beginning
Author: crossjam
category: discogs

Well, it might have only taken five and a half years, but I’m finally
making some headway on [actually hacking][2] the [pile of discogs data dumps][1]
I’ve been collecting.

I managed to ingest the data for one snapshot into a Postgres database
running on my M1 Macbook laptop. Working on creating some specialized
views for the Fabric London mix series (Fabric and Fabric Live) led to
mayhem ensuing. Real honest to gosh dirty data, SQL, and the
power of Postgres all combining for some interesting results. In the
end though, I have [the beginnings of a CLI][3] that can do the following:

	:::console
	(discogsdata) crossjam@GabrielHounds:~$ export PGDATABASE=discogs
	(discogsdata) crossjam@GabrielHounds:~$ discogsdata fabric tracks 1
	('fabric_num', 'release_id', 'release_title', 'release_artist', 'track_id', 'track_sequence', 'track_position', 'track_title', 'track_artists')
	(1, 21355, 'Fabric 01', '[]:[Craig Richards]', 114935, 1, '1', 'At That Café', '[]:[Gemini]')
	(1, 21355, 'Fabric 01', '[]:[Craig Richards]', 114936, 2, '2', "Pirate's Life", '[]:[CPEN]')
	(1, 21355, 'Fabric 01', '[]:[Craig Richards]', 114937, 3, '3', 'The Realist', '[]:[Antonelli Electr.]')
	(1, 21355, 'Fabric 01', '[]:[Craig Richards]', 114938, 4, '4', 'Sugar Rush', '[Dub Tech Soundsystem]:[Dub-Tech Soundsystem]')
	(1, 21355, 'Fabric 01', '[]:[Craig Richards]', 114939, 5, '5', 'Montage', '[]:[Jamie Anderson]')
	(1, 21355, 'Fabric 01', '[]:[Craig Richards]', 114940, 6, '6', 'Cozmoport', '[]:[SCSI-9]')
	(1, 21355, 'Fabric 01', '[]:[Craig Richards]', 114941, 7, '7', 'Cologne', '[]:[SCSI-9]')
	(1, 21355, 'Fabric 01', '[]:[Craig Richards]', 114942, 8, '8', 'Sinners', '[]:[Lo-Kee]')
	(1, 21355, 'Fabric 01', '[]:[Craig Richards]', 114943, 9, '9', 'Nightlife', '[]:[Ernst Viebeg]')
	(1, 21355, 'Fabric 01', '[]:[Craig Richards]', 114944, 10, '10', 'Bluntski', '[]:[Bushwacka!]')
	(1, 21355, 'Fabric 01', '[]:[Craig Richards]', 114945, 11, '11', 'Drum Hydraulics', '[]:[Swag]')
	(1, 21355, 'Fabric 01', '[]:[Craig Richards]', 114946, 12, '12', '(14x7x4)', '[]:[Roman IV]')
	(1, 21355, 'Fabric 01', '[]:[Craig Richards]', 114947, 13, '13', 'Silicon Jazz', '[]:[Wavescape]')
	(1, 21355, 'Fabric 01', '[]:[Craig Richards]', 114948, 14, '14', 'Took From Me', '[]:[Terry Francis]')
	(1, 21355, 'Fabric 01', '[]:[Craig Richards]', 114949, 15, '15', 'Early Riser', '[]:[Helmet]')
	(1, 21355, 'Fabric 01', '[]:[Craig Richards]', 114950, 16, '16', 'Mispent Years', '[]:[Schatrax]')
	(discogsdata) crossjam@GabrielHounds:~$ 

A handy bit to know for embedding code in (non-GitHub) Markdown is you
only need to [indent the code][4], not use triple quotes.


[1]: {filename}fwdd-0-fun-with-discogs-data.md
[2]: {filename}discogs_and_data.md
[3]: https://github.com/crossjam/discogsdata
[4]: https://daringfireball.net/projects/markdown/syntax#precode

