Title: Emacs Custom Shell Config
Date: 2013-04-21 10:01
Author: crossjam
Category: Uncategorized
Slug: emacs-custom-shell-config
Status: published

[Another great tip][1], that I wasn’t aware of, from Emacs Redux:
> Emacs sends the new shell the contents of the file ~/.emacs_shellname as input, if it exists, where shellname is the name of the name if your shell - bash, zsh, etc. For example, if you use bash, the file sent to it is ~/.emacs_bash. If this file is not found, Emacs tries with ~/.emacs.d/init_shellname.sh.

[1]: http://emacsredux.com/blog/2013/04/21/custom-config-for-shells/