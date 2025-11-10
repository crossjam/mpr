---
title: "Bray On Pagefind"
date: 2025-11-09
author: "C. Ross Jam"
status: published
---

I [implemented search][1] here earlier this year, using
[Pagefind][2]. It’s been working out pretty well for me.

In a nice bit of independent confirmation, [Tim
Bray](https://www.tbray.org), a blogging hero of mine, just recently
discovered Pagefind himself, 😲, and used it to [replace Google for
search][3] on his own site.

> Pagefind · Tl;dr: I downloaded it and installed it and it Just
> Worked out of the box. I’d describe the look and feel but that’d be
> a waste of time since you just tried it out. It’s fast enough and
> doesn’t seem to miss anything and has a decent user interface.

> How it works · They advertise “fully static search library”, which I
> assumed meant it’s designed to work against sites like this one
> composed of static files. And it is, but there’s more to it than
> that; read on.

Of course Bray has plenty of thoughts on his approach and
results. Definitely read on. I picked a bit of intel [here][5]:

> The one thing that in the rear-view seems unnecessary is that I had
> to add a data-pagefind-meta attribute to the element at the very
> bottom of the page where the date is to include it in the result
> list. There should be a way to do this without custom markup. John
> Siracusa filed a [related bug][4]. 

I’ve been desiring to have dates integrated into search on MPR but not
the time to figure out. This seems like a hint on where to look.

[Bottom line?][6]

> Thanks! · To the folks who built this. Seems like a good thing.

Totally agree!

[1]: {filename}/searching_mpr.md
[2]: https://pagefind.app/
[3]: https://www.tbray.org/ongoing/When/202x/2025/11/01/Blog-Search-Pagefind
[4]: https://github.com/Pagefind/pagefind/issues/974
[5]: https://www.tbray.org/ongoing/When/202x/2025/11/01/Blog-Search-Pagefind#p-4
[6]: https://www.tbray.org/ongoing/When/202x/2025/11/01/Blog-Search-Pagefind#p-7
