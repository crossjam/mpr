Title: Fun With Discogs Data
Date: 2013-04-23 21:33
Author: crossjam
Category: Uncategorized
Slug: fun-with-discogs-data
Status: published

<img src="http://crossjam.net/wp/mpr/wp-content/uploads/2011/11/Discogs-Logo.gif" alt="Discogs Logo" border="0" width="135" height="49" align="left" style="margin: 10px;" /> I’ve decided to try and pick up a “datadidact” habit, by regularly working with a large dataset. Even if it’s doing lowly basic characterization, this should force me to hone various skills and brush up on some basic knowledge.

Having [spoken before of the Discogs.com dataset][1], their repository would appear to be a treasure trove and is completely unrelated to anything at work to boot. Thought siccing wget on <http://www.discogs.com/data/> would be a no-brainer and a quick start. Except it’s blocked to crawlers based upon their robots.txt. ’Twould be nice if the HTTP Response for the data URL actually was more informative than a 500 error, but I can understand where Discogs is coming from.

However, I WILL NOT BE DENIED! Just have to do it tediously by hand through my browser. So be it. The longitudinal analysis possibilities are too intriguing.

Already have some initial data in hand. Not looking forward to dealing with 11Gb XML files, though First item might be to convert the data into a record/line oriented format.

[1]: http://crossjam.net/wp/mpr/2012/10/discogs-doubleplus-good/