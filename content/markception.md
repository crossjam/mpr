Title: Markception
Date: 2019-05-27 13:44
Author: crossjam
Category: Uncategorized
Slug: markception
Status: published

Go figure. Based upon [these instructions][1] from Codeholics, I started to convert MPR using the Python powered [Pelican][2]. Pelican did a good job of cleanly processing my WordPress export, and extracting my posts and other content. It looked like I was on my way.

Except my posts are written in [Markdown][3] and stored that way in the WordPress database. Which Pelican’s `import` function conveniently escapes when it generates Markdown. Sigh.

It may not be the most elegant way, but I think I can work around this with a custom fork of [the Pelican][4] source code. At worst, I’ll be flexing some atrophying Git muscles.

[1]: https://codeholics.com/moving_a_website_from_wordpress_to_pelican.html
[2]: https://getpelican.com/
[3]: http://daringfireball.net/projects/markdown/
[4]: https://github.com/getpelican/pelican