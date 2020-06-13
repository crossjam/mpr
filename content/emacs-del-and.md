Title: Emacs, DEL, and delete
Date: 2011-12-19 23:30
Author: crossjam
Category: Uncategorized
Slug: emacs-del-and
Status: published

I'm mildly chuffed that the following issue stumped me for a couple of hours this afternoon. I've been using Emacs forever and the solution should have been a no-brainer. Warning, major nerdage ahead.

So I've been amping up my Python hacking at work. The last time I was in such a mode, I was using Xemacs. In Python code, when I was at the first character of an indented line and hit delete, it would outdent one level. Very handy and natural for Python editing.

For my current run, I've switched back to Emacs 23. For a while, it wasn't really bugging me, but the outdent didn't work. A delete would just erase one character backwards. 

Finally I got fed up, and the issue turned out to be the following. On modern keyboards, you often get two keys marked with delete. The one in the standard QWERTY position should effectively be a backspace and erase. The other one should be a rightward erase. Emacs is smart enough to figure out the difference, so you can individually bind `DEL` and `delete`. It's all [documented][1] right in the Emacs manual. Unfortunately, I could never get the right combination of Google keywords to find a web page to explain this. I had to resort to **gasp**, Reading The **F*!** Manual.

The problem is that the latest and greatest Emacs python mode only binds `delete` to the really useful `py-electric-backspace` which Does The Right Thing (™). Meanwhile, `DEL` is left to its normal backwards character erase. Massive irritation for this particular user.

So here's the fix:
[sourcecode language="text"]
(add-hook 'python-mode-hook
	'(lambda ()
		(define-key py-mode-map &quot;\d&quot; 
			'py-electric-backspace)))
[/sourcecode]

May this post save another soul some time and effort.

[1]: http://crossjam.net/wp/nmh/wp-admin/index.php