Title: Flyspell and abbrev
Date: 2022-05-25
Status: published

Back to improving my Emacs environment. Since [I conquered emojis
in Emacs][7], now it’s time to deal with spelling since typos in my blog
posts drive me up a wall.

I vaguely had a recollection about some *spell package for Emacs but
couldn’t remember the specifics. Turns out it was the built-in [`flyspell`][6],
conveniently covered by [Ryan Moore][1]. Especially useful is the
keybinding for the mouse click on Macbook trackpads that let’s you see
variant spellings.

That led me to thinking about text expansion to help cut down on some
of my more frequent lapses (looking at you _occasionally_). And what
would an MPR Emacs post be without a mention of Mickey Petersen (go
buy another copy of [Mastering Emacs][2]). Emacs has a venerable
[`abbrev`][5] package and Petersen ably [addresses its usage][3] for spell
correction. Job done, but there’s bonus material on using
`hippie-expand` which does [a whole lot of interesting dynamic abbreviation
expansion][4], a.k.a replacements based on text already existing in
buffers. If you don’t like hippies, he mentions at least three other
text expansion modules 😆.

One of the real reasons I need text expansion is one of my favorite
emojis is this one, 😆, which is named, I kid you not 
> `SMILING FACE WITH OPEN MOUTH AND TIGHTLY-CLOSED EYES`

Sort of a pain to enter after `C-x 8 RET` even with tab completion.

[1]: https://www.tenderisthebyte.com/blog/2019/06/09/spell-checking-emacs/
[2]: https://www.masteringemacs.org/book
[3]: https://www.masteringemacs.org/article/correcting-typos-misspellings-abbrev
[4]: https://www.masteringemacs.org/article/text-expansion-hippie-expand
[5]: https://www.emacswiki.org/emacs/AbbrevMode
[6]: https://www.emacswiki.org/emacs/FlySpell
[7]: {filename}/emacs_and_emojis.md
