Title: Emacs and Emojis
Author: crossjam
Status: published
Date: 2022-05-17

So that’s all there was to it?

For the longest time, I had no memorable and easy way to enter and
display Unicode text within my Emacs buffers. When jumping back into
blogging this is somewhat problematic since the world sort of expects
at a minimum the frivolous usage of a few emojis to demonstrate you’re
keeping up with the cool kids 💥! After installing Nerd Fonts on my
Macbook, I was more determined than ever to solve this conundrum.

Mickey Petersen of _Mastering Emacs_ (buy his [book][4]), solved [the
display challenge][1]. Install a package, do some customization, and
voilà! Unicode characters, cut and paste from the Internet, display.

Petersen (buy his [book][4], really) also had a nifty approach to entering
emojis. Emacs has ["input methods"][5] which you can rig to [expand text
sequences][2] into Unicode characters. You have to make a modal switch
into the input method, but it’s better than nothing.

So then I started digging arouund to remind myself on how to insert
characters with diacriticals. Of course Petersen (you did buy his [book][4]
right?) [had the answer][3], but within that answer was this nugget:

> To insert a code point type C-x 8 RET and enter the Unicode name
> (type TAB twice to get a complete list).

Well, whaddya know 🤔

[1]: https://www.masteringemacs.org/article/unicode-ligatures-color-emoji
[2]: https://www.masteringemacs.org/article/inserting-emoji-input-methods
[3]: https://masteringemacs.org/article/diacritics-in-emacs
[4]: https://masteringemacs.org/book
[5]: https://www.gnu.org/software/emacs/manual/html_node/emacs/Input-Methods.html
