Title: ssh-agent and Leopard Bliss
Date: 2009-05-03 18:49
Author: crossjam
Category: Uncategorized
Slug: ssh_agent_and_leopard_bliss
Status: published

[<img src="http://crossjam.net/mpr/media/ssh dialog.png" alt="ssh dialog.png" border="0" width="200" height="117" align="left" style="margin: 10px;" />][1] [SSH][2] is the greatest tool for logging into remote machines. [ssh-agent][3] is a convenient way to use public cryptography with ssh so that you don't have to repeatedly type in your password. Dave Dribin has a great explanation of [the whys and hows of ssh-agent][1], including how it's nicely integrated into MacOS X Leopard. Especially how the MocOS keychain is used to securely hold ssh passphrases.

Only thing was, it wasn't working for me. MacOS X would properly ask me for my keyphrase, and I'd hit the checkbox for "Remember password in my keychain", but the passphrase would not be stored. After a few hours of fruitless Googling and looking at debug logs for ssh, I finally turned my eye towards the MacOS keychain. Turns out the permissions on one of my keychain files was borked. The Keychain Access utility has options to Verify and Repair your keychains, which revealed the problem and cleaned up the issue.

Now I'm a happy camper. Hopefully, if someone else is having a similar issue, Google will be able to surface this discussion for them.

[1]: http://www.dribin.org/dave/blog/archives/2007/11/28/ssh_agent_leopard/

[2]: http://en.wikipedia.org/wiki/Ssh

[3]: http://en.wikipedia.org/wiki/Ssh-agent

