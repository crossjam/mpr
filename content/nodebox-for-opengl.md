Title: NodeBox for OpenGL
Date: 2015-12-01 22:05
Author: crossjam
Category: Uncategorized
Slug: nodebox-for-opengl
Status: published

A while ago, I started a project called [AdoptedArt][1], where I attempted to transliterate Matt Pearson’s work at [AbandonedArt.org][2] into Python. Back then there were two impediments. One, there really weren’t any graphical toolkits that were a solid equivalent of [processing][3]. I cobbled something out of [pyprocessing][4] but it wasn’t very satisfying. Not to mention the project wasn’t particularly active. Two, my lil’ ole White MacBook really didn't have enough horsepower to compensate for the Python performance penalty.

AdoptedArt fell by the wayside, but just for giggles, over Thanksgiving I took a lark to see if it could be resurrected. Now I have two things on my side. One, the new MacBook Pro is easily an order of magnitude faster thanks to processing speedups, multiple cores, GPU acceleration, and a big old SSD. Second, [NodeBox for OpenGL][5] emerged, adding image manipulation capabilities and hardware acceleration to the [NodeBox][6] vector drawing API. Moore’s Law FTW! Plus, the install was painless using [Continuum’s Anaconda][8], even though there was some C based extensions to be built from source.

Bottom line, it only took me a little bit of work to adapt my adoption of [AbandonedArt’s first processing sketch, Spirograph][7] into NodeBoxGL. And it ran smooth as silk, with the MacBook barely breaking a sweat.

I’ve got high hopes to revive this project as a creative endeavor and a complete diversion from work stuff. We’ll see how it goes!

[1]: http://crossjam.net/wp/mpr/2012/03/pyprocessing-and-abandoned-art/
[2]: http://abandonedart.org
[3]: http://processing.org/
[4]: https://code.google.com/p/pyprocessing/
[5]: http://www.cityinabottle.org/nodebox/
[6]: https://www.nodebox.net
[7]: http://abandonedart.org/?p=14
[8]: https://www.continuum.io/downloads