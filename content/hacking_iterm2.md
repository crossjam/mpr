Title: Hacking iTerm2
Date: 2022-06-14
Author: C. Ross Jam
Status: published

Even though I’ve expounded on [the coolness of xonsh][2], I haven’t put it
to use in full anger yet. I’m thinking it might best be leveraged as
an interactive shell workspace, sort of like Jupyter Notebooks but
without the Web browser bits and much more of a CLI.

But I’ve been thinking about how to make launching a new space as
cheap and mindless as possible. Enter scripting the [iTerm2][3] terminal
emulator using its [Python API][4]. From [an example of scripting iTerm2][5]
straight from another command line:

> This script demonstrates two concepts:

>   1. Launching iTerm2 using PyObjC and running the script only after it
>   is launched. 

>   2. Creating a window that runs a command.

So if the command is "kickoff xonsh with some args," either in an
existing or newly created virtualenv, it becomes almost trivial to
fire off new interactive spaces.


[1]: https://iterm2.com/python-api/examples/launch_and_run.html
[2]: https://mpr.crossjam.net/wp/mpr/2022/05/streaking-2/
[3]: https://iterm2.com/
[4]: https://iterm2.com/python-api/
[5]: https://iterm2.com/python-api/examples/launch_and_run.html
