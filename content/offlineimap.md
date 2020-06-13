Title: offlineimap
Date: 2011-11-20 19:34
Author: crossjam
Category: Uncategorized
Slug: offlineimap
Status: published

For the longest time, I've been keeping an eye out for a good GMail backup solution. I've stashed a lot of links, but never really cottoned to any of the potential applications. However, thanks to [Mike Johnson][1], I might finally have something that fits my tastes.

[Johnson describes][2] how to use [`offlineimap`][3] to download your GMail contents using of course the [IMAP protocol][4]. `offlineimap` is written in Python, so it should work on both Linux and MacOS.
> *Offlineimap is meant to take an IMAP folder offline for later reading by copying the contents of the IMAP server to a MailDir folder, which is an older Unix standard that organizes emails into local mail folders. Once copied locally, the mail folder can be read by any number of email programs. At it turns out, this is also awesome for making backups.*

There are a couple of great things that fall out if this actually works

* The backup procedure can be hosted on my own home Linux box or better yet my Linode VPS. No lockin to a particular vendor.
* `cron` can be used to run the backup process automatically. I won't forget to do it.
* `offlineimap` allows you to select specific folders. So I finally might have a convenient way to download my **@Notes** folder locally to my MacBook for indexing by Spotlight. Alternatively, I can use my own full text search engine.

[1]: http://www.publicstatic.net/
[2]: http://www.publicstatic.net/2011/11/06/backup_gmail/
[3]: https://github.com/nicolas33/offlineimap
[4]: http://en.wikipedia.org/wiki/Imap