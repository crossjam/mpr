Title: Bashing History
Date: 2010-03-04 21:08
Author: crossjam
Category: Uncategorized
Slug: bashing_history
Status: published

GNU's [Bash][1] is my command language interpreter of choice. I can't even remember when I started using it. But I probably only use about 1/10th of its capabilities.

Chanced across this discussion of [effective use of Bash's history mechanism][1] by Jason Bechtel and learned a couple of things. The `HISTIGNORE` environment variable is a new feature to me. This is the foundation of a neat trick, whereby if you put a space in front of a command then it **doesn't** get added to your command history. Handy for leaving out the trivial `ls`, `cd`, and, for me at least, `pushd` executions that litter my command usage.

Also, I was completely ignorant of the `shopt` command. Learn something new every day.

[1]: http://www.gnu.org/software/bash/

[2]: http://www.talug.org/events/20030709/cmdline_history.html

