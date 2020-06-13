Title: MovableType 4.23 to 5.02
Date: 2010-09-07 20:06
Author: crossjam
Category: Uncategorized
Slug: movabletype_423_to_502
Status: published

<img src="http://crossjam.net/mpr/media/bug-pbmt-white.png" border="0" width="120" height="75" align="right" style="margin: 10px;" /> Harder than I think it should have been, but not as bad as my worst imaginings, I've managed to upgrade [Mass Programming Resistance](http://crossjam.net/mpr) to the latest version of Movable Type. Here's the high level steps to the migration:

* Export the 4.23 content to a basic MovableType xml file.

* Install MovableType 4.34 in a parallel setup. This installation should use MySQL as a database.

* Import the 4.23 content into the 4.34 installation. At this point you have a MySQL db with the 4.007 schema.

* Following [Jason Culverhouse's instructions][1] overwrite all of the MovableType 4.34 CGI files with 5.02 files.

* Use `perl ./tools/upgrade --name superuser` from the cgi directory to upgrade the db to the 5.0x schema.

At this point, seems like I'm in good shape. There are some configuration settings that need to be tweaked, and I need to port the handful of MT pages over, but otherwise all seems good. Even posting using MarsEdit seems to work. In fact, the new install seems make posting with MarsEdit speedier.

No thanks to the [Movable Type documentation][2], which I found to be pretty much useless on the topic of upgrading.

Still need to do the actual switch over, but should be about a 5 minute job. Apologies if screws up your feed reader.

[1]: http://www.mischievous.org/2010/01/upgrading-from-movabletype-4-t.html

[2]: http://www.movabletype.org/documentation/installation/upgrade-movable-type.html

