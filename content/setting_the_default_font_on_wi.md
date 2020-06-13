Title: Setting the Default Font on Windows Emacs
Date: 2010-07-23 20:42
Author: crossjam
Category: Uncategorized
Slug: setting_the_default_font_on_wi
Status: published

[<img src="http://crossjam.net/mpr/media/Emacs Small Icon.png" alt="Emacs Small Icon.png" border="0" width="48" height="48" align="left" style="margin: 10px;" />][1] At work I'm stuck with Windows XP, papered over to look like UNIX as much as possible. Luckily our sysadmins have installed a version of [GNU Emacs for Windows][1] that works pretty well.

I don't like the default font, whatever it is. I much rather prefer Lucida Console. So any time I reboot the machine or restart Emacs, I had to right click on the main frame and select Lucida Console. You'd think as a tried and true geek, I'd follow [the DRY principle][3] on this one. But noooooooo...

I've been doing this little font setting dance for over 3+ years. Pathetic.

Knowing from long experience how arcane configuring Emacs can be, I was dreading a multi-hour session reading Info files and writing Emacs Lisp. But last week I finally hunkered down and decided to nail this one. Only took me about 45 minutes or so combining Google searching and Emacs Lisp experimentation.

Turns out the key is understanding the Emacs frame *(window to the rest of the world)* [parameters][2] and ignoring the [face][4] stuff. Faces are Emacs way of specifying font stylings for regions of text. They play nice with Emacs options customization menu. You'd think they would be one stop shopping for text options. But even if you set the default font for the default face, your text won't show up right in every frame.

Here's what you want in your `.emacs.el`, `emacs.el`, `init.el` or whatever:

<code>

(add-to-list 'default-frame-alist

'(font . "-outline-Lucida Console-normal-r-normal-normal-11-82-96-96-c-70-iso8859-1"))

</code>

This says, for every frame opened, use my particular version of Lucida Console to initialize the frame's text font parameter. Then per frame settings and face stylings can kick in afterwards. Generating the font specification is left as an exercise to the reader. `default-frame-alist`, besides letting you set the default font, also initializes some obvious window geometry and color parameters, as well as some fun stuff like opacity and window bar title.

And with that, I save myself a whopping 10-15 seconds every time I start up Emacs, along with my sanity.

One last thing, I tried [using `set-default-font`][5] and it did not work.

Just as a point of reference, here's the result of `(emacs-version)` on my work machine:

<code>

"GNU Emacs 21.3.1 (i386-mingw-nt5.1.2600) of 2004-03-10 on NYAUMO"

</code>

So Your Mileage May Vary.

*Posted in the hopes that this may help someone else someday.*

[1]: http://ftp.gnu.org/pub/gnu/emacs/windows/README

[2]: http://www.gnu.org/s/emacs/manual/html_node/elisp/Frame-Parameters.html#Frame-Parameters

[3]: http://en.wikipedia.org/wiki/Don't_repeat_yourself

[4]: http://www.gnu.org/s/emacs/manual/html_node/elisp/Faces.html#Faces

[5]: http://habib.posterous.com/how-to-change-emacs-default-fo

