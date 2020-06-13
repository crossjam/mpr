Title: Speaking of Data Collection
Date: 2011-10-20 20:29
Author: crossjam
Category: Uncategorized
Slug: speaking-of-data-collection
Status: published
Attachments: wp/mpr/wp-content/uploads/2011/10/PubSubHubbub-Logo.png

[<img src="http://crossjam.net/wp/mpr/wp-content/uploads/2011/10/PubSubHubbub-Logo.png" alt="PubSubHubbub Logo" border="0" width="113" height="38" align="left" style="margin: 10px;" />][3] So [Gowalla][2] and [Instagram][1] have real-time streaming apis. Not quite as easy as Twitter since those services use [PubSubHubbub][3] to stream their updates. It also means running a notification receiver that accepts incoming HTTP requests on my Linode. So for my next trick, I'd like to see if I can't get a million updates out of each of those services.

[1]: http://instagram.com/developer/realtime/
[2]: http://gowalla.com/api/docs/pshb
[3]: http://code.google.com/p/pubsubhubbub/