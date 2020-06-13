Title: Diggin’ On Supervisord
Date: 2012-11-30 21:06
Author: crossjam
Category: Uncategorized
Slug: diggin-on-supervisord
Status: published

Finally got a chance to put [supervisord][1] into action at work. It’s very handy for organizing, launching, and managing a bunch of server processes. I’m especially liking the interactive command shell provided by [supervisorctl][2]. Plus I think it’s easily launchable from a cron `@reboot` action which is great for this non-root user.

[1]: http://supervisord.org/
[2]: http://supervisord.org/running.html#running-supervisorctl