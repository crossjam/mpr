Title: Revenge of the Lisp Machine
Date: 2011-02-21 21:58
Author: crossjam
Category: Uncategorized
Slug: revenge_of_the_lisp_machine
Status: published

<div style="text-align:center;"><img src="http://crossjam.net/mpr/media/SBCL Circles.png" alt="SBCL Circles" border="0" width="320" height="262" style="margin: 10px;"/></div>

Well over two years ago, I blogged about [kicking the tires][1] on various Lisp implementations. At the time, I observed how modern machine performance had blown past the "inefficiencies" we saw back in the 80s to mid 90s.

Fast forward to last week, mid-February 2011. I'm stuck in a not-particularly captivating conference, with a relatively new Macbook Pro, dual core Intel i7 and 8 MB of memory. What's a Lisp nerd to do, but check out how the new ride rolls. So I grab and install every Lisp and Scheme implementation under the sun, since I've got so much idle time, and quickly whip out a recursive `fact` function in all of them.

Wow! All I can say is that I was blown away by the performance observed running a few micro-benchmarks. When a Common Lisp compiles to native code and can do `(fact 1000)` in about a millisecond, you're cooking with gas.

That prompted me to revisit the Lisps on my measly old, circa 2008, bottom of the line, white Macbook. Even if it's an order of magnitude slower, we're still looking at hundredth of a second performance. In doing so, I discovered the fabulous [Quicklisp project][2], which makes installing Common Lisp packages butt easy across a number of implementations. Turns out there's the nice [LISPBUILDER-SDL][3] package, which makes the cross-platform multimedia [SDL][4] library available within Common Lisp.

The above screen capture is an example from LISPBUILDER running in [SBCL][5]. If you squint close enough at the lower right, you can see the frames per second, FPS, reading. That's a 30.29.

A compiled Common Lisp on a pokey old Macbook can easily do 30 FPS of graphics rendering. And here I am [struggling to get Python][6] up to the pace of [processing](http://processing.org).

I'll have to get [substrate][7] implemented in SBCL just for comparison and we'll go from there.

[1]: http://crossjam.net/mpr/2008/09/lisp-on-modern-machines.html

[2]: http://www.quicklisp.org/

[3]: http://code.google.com/p/lispbuilder/wiki/UsingLispbuilderSDL

[4]: http://www.libsdl.org/

[5]: http://www.sbcl.org/

[6]: http://crossjam.net/mpr/2010/05/that-100-hours-project.html

[7]: http://www.complexification.net/gallery/machines/substrate/index.php

