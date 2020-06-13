Title: A Mystery Solved
Date: 2011-01-30 00:34
Author: crossjam
Category: Uncategorized
Slug: a_mystery_solved
Status: published

<img src="http://crossjam.net/mpr/media/Thunderbird Mailboxes.png" alt="Thunderbird Mailboxes.png" border="0" width="249" height="284" align="left" style="margin: 10px;" /> I finally, Finally, FINALLY, solved a long standing conundrum that had been vexing me. The nut of the issue involved mailing links from myself to my own GMail account, using a `+` address, e.g. `bmd+notes@example.com`. I have a GMail rule to automatically file such messages into a folder. This worked great until I would mail a link from my MacBook, through [MailHop](http://www.dyndns.com/services/sendlabs/outbound.html). Then the message wouldn't get autofiled, and would sort of disappear.

Initially I blamed MailHop for not forwarding a message with the same `to` and `from` addresses. Not true. Messages were getting through to GMail. In fact, once I poked around in the "All Mail" folder, there were my little self-notes.

So why wasn't GMail running my dang filter?

Turns out I had Thunderbird set up to add a copy of the message to the "Sent" folder. So when my message was delivered through SMTP, GMail was smart enough to reconcile the incoming as already existing in my message store. Ergo, this wasn't a new message.

And GMail only runs filters on new messages.

The quick solution was to simply turn off Thunderbird's filing of outgoing messages. Then my links messages got autofiled. GMail was even smart enough to recognize that I sent the mail and stash it in the "Sent Mail" folder. Only problem is that if I actually sent mail to someone else, e.g. `crossjam@example.com`, I wouldn't have a record of the sent mail. Through a combination of Thunderbird `Bcc`ing myself and another GMail filter I juryrigged a solution. I think.

Of course, if I just used Google's SMTP for all my outbound mail, this wouldn't be a problem at all. It's what I do on my iPhone. But it's the general principle of not having Google slurp up all of my communications, and besides I like the [MailHop](http://www.dyndns.com/services/sendlabs/outbound.html) guys.

*Whew!*

