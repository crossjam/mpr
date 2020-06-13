Title: Up To Code
Date: 2017-07-15 15:45
Author: crossjam
Category: Uncategorized
Slug: up-to-code
Status: published
Attachments: wp/mpr/wp-content/uploads/2017/07/certbot-log.png

[<img src="https://crossjam.net/wp/mpr/wp-content/uploads/2017/07/certbot-log.png" alt="Certbot log" title="certbot-log.png" border="0" width="140" height="48" style="float:left; padding:10px;" />][2] Well, [that process][5] actually wasn’t too bad. Now I’m fully encrypted thanks to the [Electronic Frontier Foundation][1] and [certbot][2]. 

Also [Why No Padlock?][3] helped me figure out why Chrome wasn’t giving me the prized lock. Which then led to installing the [SSL Insecure Content Fixer][4] plugin for WordPress. Now my image URLs are cleaned up automagically. 

No thanks to **systemd** under Ubuntu Linux 16.04, which got itself twisted up and held me back from upgrading to Ubuntu 17.04. Boiled down to moving some arcane config file out of the way to allow a couple hundred odd packages to upgrade. That’s actually where the majority of my time was spent in this exercise.

Now I just have to figure what all the certificate mumbo jumbo actually means.

*certbot logo converted to png format from [the EFF’s SVG original][7], which should be legal under [the applicable Creative Commons license][6].*


[1]: https://eff.org/
[2]: https://certbot.eff.org/
[3]: https://www.whynopadlock.com/index.html
[4]: https://ssl.webaware.net.au/
[5]: https://crossjam.net/wp/mpr/2017/07/does-this-site-need-https/
[6]: https://creativecommons.org/licenses/by/3.0/us/
[7]: https://certbot.eff.org/images/certbot-logo-1A.svg