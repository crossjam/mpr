Title: Emacs TRAMP
Date: 2022-06-02
Status: published
Author: C. Ross Jam

Some might call me an Emacs tramp (🤣), but I’m referring to the Emacs
mode that allows for editing remote files over ssh connections. 

> TRAMP (Transparent Remote Access, Multiple Protocols) is a package
> for editing remote files, similar to AngeFtp or efs. Whereas the
> others use FTP to connect to the remote host and to transfer the
> files, TRAMP uses a remote shell connection (rlogin, telnet,
> ssh). It can transfer the files using rcp or a similar program, or
> it can encode the file contents (using uuencode or base64) and
> transfer them right through the shell connection.

The overall experience is pretty much seamless, while not having to
deal with a bunch of warts related to distributed file systems such as
SMB, AFS, Dropbox, et. al. Works great even with version control tools
such as [magit][2].

The fact that TRAMP can operate over telnet (😱) of all protocols
should tell you it’s ancient though. An elegant weapon, for a more
civilized age.

[1]: https://www.emacswiki.org/emacs/TrampMode
[2]: https://magit.vc
