Title: Fully Operational
Date: 2017-09-01 21:17
Author: crossjam
Category: Uncategorized
Slug: fully-operational
Status: published
Attachments: wp/mpr/wp-content/uploads/2017/09/Peyote-Substrate.png

<img style="display:block; margin-left:auto; margin-right:auto;" src="https://crossjam.net/wp/mpr/wp-content/uploads/2017/09/Peyote-Substrate.png" alt="Peyote Substrate" title="Peyote Substrate.png" border="0" width="300" height="148" />

Wasn’t all that difficult, but I got my [peyote substrate sketch][3] working again. The only interesting thing I discovered is that the Python [`cairocffi`][2] module doesn’t work particularly well with [`pygame`][1] surfarrays. `cairocffi` has this weird bit where it stashes data buffers in an internal cache to help finalize external data garbage collection. Unfortunately, this conflicts with `pygame`’s locking of Surfaces before blitting to the screen. Switching back to [`pycairo`][4] was the resolution.

Anyhoo, debugging the issue forced a reintroduction with peyote. The codebase is surprisingly although a bit hackish. It’ll be fun to clean it up, modernize it, and generate some new sketches.

[1]: http://www.pygame.org/
[2]: https://cairocffi.readthedocs.io/en/latest/
[3]: https://crossjam.net/wp/mpr/2010/01/mission_accomplished/
[4]: https://pycairo.readthedocs.io/en/latest/