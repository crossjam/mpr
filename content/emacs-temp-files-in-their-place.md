Title: Emacs Temp Files in Their Place
Date: 2013-05-09 21:23
Author: crossjam
Category: Uncategorized
Slug: emacs-temp-files-in-their-place
Status: published

[Really handy tip][1] from Emacs Redux:
> Auto-backup is triggered when you save a file - it will keep the old version of the file around, adding a ~ to its name. So if you saved the file foo, you’d get foo~ as well.

> auto-save-mode auto-saves a file every few seconds or every few characters …

> Even though I’ve never actually had any use of those backups, I still think it’s a bad idea to disable them (most backups are eventually useful). I find it much more prudent to simply get them out of sight by storing them in the OS’s tmp directory instead.

I find the biggest pain with autosave files is getting git to ignore their existence. Yeah, I can fiddle around with .gitignore files, but that never quite seems to be universally applied correctly for me. Not even having emacs temp files in project directories makes the whole issue go away.

[1]: http://emacsredux.com/blog/2013/05/09/keep-backup-and-auto-save-files-out-of-the-way/