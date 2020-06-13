Title: So Far, So Good
Date: 2011-04-16 22:49
Author: crossjam
Category: Uncategorized
Slug: so-far-so-good
Status: published

The [switch][1] seems not to have seriously busted anything. About the only 404's I'm seeing on the new site are for images. Images that shouldn't even be linked to from an external site. And occasionally there's an old permalink that didn't get translated correctly. Those are easy to fix though. 

The various search bots are visiting the new site, being bounced through old urls into the new site using HTTP redirects. I used the fairly brute force method of leaving the old static MovableType HTML files in place, but putting Php code in them to generate the HTTP redirect. Some Python fu was needed to automatically rewrite the statics pages and generate the right destination URL. That was fun hacking though. I'm gonna pat myself on the back for ingeniously avoiding linkrot.

Best of all I ran essentially the same process for [New Media Hack][2]. Now my old writings have a fresh coat of paint and are searchable.

**Update:** Spoke a little too soon, as I had some incorrect permalinks in the imported posts. Did a quick search and replace, bulk delete the old posts, and then reimported. Probably need to do a post by post examination.

[1]: http://crossjam.net/wp/mpr/2011/04/movin-daze/
[2]: http://crossjam.net/wp/nmh/