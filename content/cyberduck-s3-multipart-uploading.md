Title: Cyberduck S3 Multipart Uploading
Date: 2011-09-13 20:24
Author: crossjam
Category: Uncategorized
Slug: cyberduck-s3-multipart-uploading
Status: published
Attachments: wp/mpr/wp-content/uploads/2011/09/Cyberduck-Icon.png

[<img src="http://crossjam.net/wp/mpr/wp-content/uploads/2011/09/Cyberduck-Icon.png" alt="Cyberduck Icon" border="0" width="100" height="100" align="right" style="margin: 10px;" />][2] Taking some "vacation" time this week, and what am I doing? Uploading multi-gigabyte files to [Amazon S3][3]. So I'm a nerd.

Turns out though that uploading files greater than 5GB requires multipart uploading, which breaks the file up into chunks for better throughput and reliability. Client support for this part of the S3 API is not obvious.

Hat tip to Joe Miller for [cataloging a few S3 clients][1] that **do support** multipart uploads, including [Cyberduck][2]. Open source, free as in beer, cross platform, and eminently usable, Cyberduck is the Swiss Army knife of file uploading. Just for this capability I will be making a donation shortly.

[1]: http://joemiller.me/2011/02/18/client-support-for-amazon-s3-multipart-uploads-files-5gb/
[2]: http://cyberduck.ch/
[3]: http://aws.amazon.com/s3