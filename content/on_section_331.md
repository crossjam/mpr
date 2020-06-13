Title: On Section 3.3.1
Date: 2010-07-05 14:08
Author: crossjam
Category: Uncategorized
Slug: on_section_331
Status: published

<img src="http://crossjam.net/mpr/media/iOS 4 Logo.png" alt="iOS 4 Logo.png" border="0" width="124" height="54" align="right" style="margin: 10px;" />Back in April, Apple announced [adjustments to its guidelines][1] for App Store application approval. Of course as an Apple customer, Apple observer, and programming language enthusiast I had to take notice. At the time, I read the condition that

<blockquote><em>

... Applications must be originally written in Objective-C, C, C++, or JavaScript as executed by the iPhone OS WebKit engine, and only code written in C, C++, and Objective-C may compile and directly link against the Documented APIs...

</em></blockquote>

as a bit extreme, although I didn't descend into the histrionics that quite a few other folks did.

I immediately thought of all the dynamic languages (Common Lisp, Scheme, Python, Lua, Ruby, etc.) that were now essentially verboten. Sure these languages would be a distinct micro-minority of the tools used to develop iPhone apps, but they allowed for a vibrant community of potentially radically innovative tinkerers. Besides, folks using these languages weren't so much looking to be cross platform as rapid experimenters or hyper-productive.

Thinking a little sideways, I wonder if Apple couldn't assuage quite a few folks by releasing an Apple sanctioned and maintained high level development environment. Pick a language you've got a lot of smart run-time engineers already on staff for *(JavaScript?)*, build out some nice Cocoa Touch libraries in the language, maybe provide a nice client engine, and call it the next generation of [HyperCard][2].

Alternatively, buy a small company (e.g. [Runtime Revolution](http://www.runrev.com/)) that has the existing intellectual resources to make this happen. Or even just contract out with one to provide the environment in perpetuity. I'm sure Apple's lawyers could write language or come up with an agreement such that Apple still maintained the necessary platform control.

Then again Apple might just argue that Safari, JavaScript, and the Web are already fulfilling that role of alternative application environment.

Continue on for a linkdump of articles, mostly just here for posterity and future referencey, that helped inform my thoughts.

[1]: http://arstechnica.com/apple/news/2010/04/apple-takes-aim-at-adobe-or-android.ars

[2]: http://en.wikipedia.org/wiki/Hypercard


<!--more-->
I've been collecting varied reactions and analyses over the past few months to shape my thinking. With a little distance here's some of the best:

* Jason Snell had a fairly [lucid and coherent analysis][2] of all of the iPhone OS 4 announcements, shortly after they surfaced.

* ArsTechnica's John Siracusa, Mac tech analyst extraordinaire, framed the strategy as [Apple's big bet][3] for dominance.

* Ian Bogost's [*Flash is not a Right*][4] was a useful tonic to those proclaiming the lack of Flash as somehow a crime.

* While anthropomorphizing a tad too much, Mark Bernstein may have captured some of [the emotion behind Apple's desire for *Platform Control*][7].

* Of course John Gruber got in a couple of good ones, including thinking of smartphones as [*app consoles*][5], [*This is how Apple rolls*][6] on how Apple works, Apple's case [against cross-platform middleware][8], and the [consequences][9] of some of [the casualties][11].

* Finally, it looks like [Apple might be shifting a bit][10] to reduce some of the collateral damage.

[1]: http://arstechnica.com/apple/news/2010/04/apple-takes-aim-at-adobe-or-android.ars

[2]: http://www.macworld.com/article/150539/2010/04/apple_world.html

[3]: http://arstechnica.com/staff/fatbits/2010/04/apples-wager.ars

[4]: http://www.bogost.com/blog/flash_is_not_a_right.shtml

[5]: http://daringfireball.net/linked/2010/05/03/fraser-back-in

[6]: http://www.macworld.com/article/151235/2010/05/apple_rolls.html

[7]: http://www.markbernstein.org/Apr10/PlatformControl.html

[8]: http://daringfireball.net/2010/04/middleware_and_section_311

[9]: http://daringfireball.net/linked/2010/05/18/runrev

[10]: http://arstechnica.com/apple/news/2010/06/devs-cautiously-optimistic-about-ios-4-nonnative-code-change.ars

[11]: http://daringfireball.net/linked/2010/04/16/scratch

