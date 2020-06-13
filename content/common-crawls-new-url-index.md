Title: Common Crawl’s New URL Index
Date: 2013-01-09 16:00
Author: crossjam
Category: Uncategorized
Slug: common-crawls-new-url-index
Status: published

[Scott Robertson][1] put together [an index of the URLS in the Common Crawl dataset][2], so everyone  doesn’t have to trawl the whole contents looking for where the links are:

> I’m happy to announce the first public release of the Common Crawl URL Index, designed to solve the problem of finding the locations of pages of interest within the  archive based on their URL, domain, subdomain or even TLD (top level domain).

> Keeping with Common Crawl tradition we’re making the entire index available as a giant download. Fear not, there’s no need to rack up bandwidth bills  downloading the entire thing. We’ve implemented it as a prefixed b-tree so  you can access parts of it randomly  from S3  using byte range requests. At the same time, you’re free to download the entire beast and work with it directly if you desire.  

> Information about the format, and samples of accessing it using python are available on github. Feel free to post questions in the issue tracker and wikis there.

Combine with [a previous hare-brained scheme][3] to good effect.

[1]: https://angel.co/srobertson
[2]: http://commoncrawl.org/common-crawl-url-index/
[3]: http://crossjam.net/wp/mpr/2012/12/boinging-the-common-crawl/