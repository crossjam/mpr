Title: Information Trapping, Google Desktop, and Apple Mail
Date: 2009-06-18 23:15
Author: crossjam
Category: Uncategorized
Slug: _so_previously_i_documented
Status: published

<img src="http://crossjam.net/mpr/media/Apple Mail Logo.jpg" alt="Apple Mail Logo.jpg" border="0" width="112" height="120" align="left" style="margin: 10px;" /> So previously I documented how my [information trapping process][1] had reduced to e-mailing links + text to myself. I'm pretty happy with the setup, but there was one little niggling glitch.

Google Desktop could search my notes, through GMail, but if I was offline I couldn't actually read the notes. I needed a seamless way to synch my notes folder out of IMAP onto my laptop. You can turn on an option in Thunderbird, my longstanding e-mail client, to synch folders. However, Thunderbird e-mail is not indexable by Google Desktop. At least, not without some [hairy kludges][2].

I had a thought to pulling out the Python swiss army knife and hacking something together.

Enter Apple Mail. Mail can be configured to do the exact same IMAP synching, but it's mail storage format is compatible with Spotlight, which is what Google Desktop uses under the covers for indexing. Mission accomplished, although I've turned a finely polished e-mail program into a simpleton file synch program.

Now all I need to do is get my starred items out of Google Reader and into my notes folder. Yeah, I could just mail the items from GReader instead of starring them (*I actually do this fairly often, but what about the old items*), but I'm trying to eliminate friction. Starring is as low friction as it gets.

Two challenges here: 1) getting the items out in an automated fashion (*sounds like a good job for a <code>cron</code> script*), 2) getting them up into GMail, in the right folder, with the right date (*not quite sure which of Python's [SMTP][3] or [IMAP][4] modules is the right call*)

[1]: http://crossjam.net/wp/mpr/2009/02/e_mail_subaddressing_and_infor/

[2]: http://www.dennis.ca/weblog/2007/04/17/howto-make-spotlight-and-google-desktop-index-thunderbird-messages/

[3]: http://docs.python.org/library/smtplib.html#module-smtplib

[4]: http://docs.python.org/library/imaplib.html

