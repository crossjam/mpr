Title: GNU Screen Locking Fix
Date: 2022-12-31
Author: C. Ross Jam
Status: published

Since I [started using][2] an iPad Pro cover, SSH, and screen, [this problem][1]
has been biting me in the rear:

> I have been using GNU Screen for a while now. I usually create
> multiple new windows (Ctrl-a c) every day. Then I flip back and
> forth between the multiple screens (Ctrl-a n) or just toggle between
> the last 2 windows used (Ctrl-a a). Sometimes my finger slips and I
> hit Ctrl-a x which provides you with a password prompt. This is GNU
> Screen's lockscreen function.

> Normally you just enter your user password and the screen will
> unlock. Screen is using /local/bin/lck or /usr/bin/lock by
> default. This is all fine and dandy if you have a user account
> password to enter. If you have servers that only use SSH keys and
> don't use passwords you will have no valid password to enter. In
> other words you are stuck at this lock screen. One way around it is
> to login to the same machine and re-attach to the same screen
> session (normally "screen -r" if you have only 1 session open). Then
> kill the session with the lock screen. This is annoying to have to
> do. 

It really is a pain, but it has an [extremely simple
solution][1]. Basically you disable the default binding for locking
and go on about your business.

[1]: https://www.pantz.org/software/screen/disabling_gnu_screen_lock_screen.html
[2]: {filename}/ipad_cover.md
