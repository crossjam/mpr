Title: Towards Production
Date: 2013-04-01 19:48
Author: crossjam
Category: Uncategorized
Slug: towards-production
Status: published

Another insightful gem from Rafe Colburn on taking a quick “hack” and [getting the result into a production system][1]:
> Why write this up? It’s to point out that for most projects, getting something to work is just a small, small part of building a production service. Exporting a CSV file from a database query and uploading it to an FTP server takes just a few minutes. Converting that into a service that runs within the standard infrastructure, and handles failure conditions smoothly takes hours.

Echoes of [the challenge of building capabilities][2].

Also, I’ve learned through hard won experience, don’t trust the environment cron provides your script at all. Make everything as explicit as possible. Even then it’s a difficult debugging process. Good luck!

[1]: http://rc3.org/2013/03/31/the-long-journey-toward-production/
[2]: http://crossjam.net/wp/mpr/2012/10/capability-challenge/