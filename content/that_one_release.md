Title: That One Discogs Release
Date: 2023-08-12
Status: published

Any significantly large, human created, dataset is going to get some
weird entries. In the Discogs Data Dumps, there’s a [release][1]
(_careful, following that link might blow up your browser_) with
a title that’s a whole bunch of Unicode characters and the word
"Unicode". The title is a little under 628K (yes, six hundred twenty
eight thousand) octets.

Does it matter at all? Well, if you stuff that record into a
PostgreSQL database and then build an index on the `title` column,
you’ll get a [sad trombone][2].

I’m thinking of hacking my personal fork of [discogs-xml2db][3] to
have an option for limiting field size.

[1]: https://www.discogs.com/release/23116274-ちゅううううううううううううううううううううううううううううううう
[2]: https://youtu.be/yJxCdh1Ps48
[3]: https://github.com/crossjam/discogs-xml2db
