Title: Gmail, IMAP, and Spam
Date: 2008-09-10 23:00
Author: crossjam
Category: Uncategorized
Slug: gmail_imap_and_spam
Status: published

<img src="http://crossjam.net/mpr/media/GMail Logo.jpeg" border="0" height="53" width="129" alt="GMail Logo.jpeg" align="right" style="margin: 10px;"/>Even though I should know better, I don't outsource my e-mail services. I pay for a cheap <a href="http://en.wikipedia.org/wiki/Virtual_private_server">virtual private server</a> from <a href="http://rimuhosting.com/">RimuHosting</a>, and run <a href="http://www.postfix.org/">Postfix</a> with <a href="http://www.courier-mta.org/imap/">Courier IMAP</a>. This is a lose if you have any e-mail addresses which receive spam, which by definition means a flood of spam. And I've got a couple of such addresses. Meanwhile, I've also got a CS PhD but was stymied in my attempts to stem the tide using stock open source tools.

GMail to the rescue. In addition to receiving messages on my VPS I just forward all of them to an account on Google's mail servers. Then I just use <a href="http://mail.google.com/support/bin/answer.py?hl=en&amp;answer=75725">IMAP to access GMail</a>. This wins because:

<ol><li>GMail's spam filtering is really good

<li>I can use the Web frontend or Thunderbird

<li>If GMail goes down, I still have my old, spam overrun way of getting to my mail.

</ol>

