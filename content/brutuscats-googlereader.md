Title: brutuscat's googlereader
Date: 2011-11-21 20:20
Author: crossjam
Category: Uncategorized
Slug: brutuscats-googlereader
Status: published

A few years ago, I had an automated script that would backup my starred items in Google Reader. It got busted when Google Reader made some changes to its [unofficial API][2].

Luckily a few other folks have updated the old [`pyrfeed`][3] module, and put the results up on GitHub. [Mauro *(brutuscat)* Asprea's *googlereader* fork][1] seems to be the most recent. 

Gave it a quick test drive against my starred items feed and seemed to do what it says on the tin. Interestingly, you can get the results out in JSON, which means another potential application of MongoDB.

[1]: https://github.com/brutuscat/googlereader
[2]: http://code.google.com/p/pyrfeed/wiki/GoogleReaderAPI
[3]: http://code.google.com/p/pyrfeed/