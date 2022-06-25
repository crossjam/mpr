Title: Yikes! Yak Shaving
Date: 2022-05-30
Author: C. Ross Jam
Status: published

![Xonsh Terminal on Ubuntu Screen
Capture]({static}/images/xonsh_ubuntu_capture.png)

Yesterday I lost the plot by [yak shaving][6] my [shell setup][10]
installation process to work better under Ubuntu. The above capture
illustrates that lots of progress was made, but then I forgot to
actually post. Oh well!

<!-- PELICAN_END_SUMMARY -->

Part of the distraction involved dealing with [Linuxbrew][1], the
Linux version of [Homebrew][2]. If I have `brew` successfully
installed via my [`homely`][3] setup, it makes the package management
a bit more consistent. On the other hand, Linux distros in general and
Ubuntu in particular have their own package managers, which generally
work better and which `homely` is compatible with. Also, Linuxbrew is
a bit heavy handed in that you essentially need to have root
privileges for the easiest install. The kicker is that there are often
Linux distro packages that can be quite a few releases behind
upstream, which introduces another inconsistency. I was trying to
leverage [`pipx`][4] for a fixed base set of Python CLI apps, but
Ubuntu had a way old package version that failed on a repeat request
to install a Python package, breaking my overall `homely`
install. _It’s turtles all the way down_ 😆.

Grappling with the growing sprawl of my `homely` configuration and
landing on the shores of a new machine I think the approach will
become:

* Hand bootstrap the process via [installation of `pipx` as user
  local][5]
* Install a few pure Python CLIs using `pipx` including `homely`
* Clone my private `dotfiles` repo onto the new machine for `homely`
* Script the installation of Linuxbrew within `homely`
* Default to the Linux package manager unless there’s a significant
  reason to get a recent version via `brew`, but at least that option
  will be there

Becoming obvious to me is that [`pyenv`][7] is somewhat
superfluous. Generally speaking, I don’t need multiple Python
interpreter versions installed, just one good one. Previously,
Homebrew provided a nice means to get a Python 3.8.x or greater
version installed, even though it wasn’t [particularly good][8] for
preserving Python interpreters across package upgrades. Now the
platforms have caught up with their stable Python 3 versions and
`pyenv` is a bit janky from a shell perspective. The Xonsh ecosystem
even has its own [integration extension for `pyenv`][9]. I’ll keep `pyenv` in
the mix, deprioritize it’s installation, and monitor the usage.

[1]: https://docs.brew.sh/Homebrew-on-Linux
[2]: https://brew.sh/
[3]: https://homely.readthedocs.io/en/latest/
[4]: https://pypa.github.io/pipx/
[5]: https://pypa.github.io/pipx/installation/
[6]: https://en.wiktionary.org/wiki/yak_shaving
[7]: https://github.com/pyenv/pyenv
[8]: https://justinmayer.com/posts/homebrew-python-is-not-for-you/
[9]: https://github.com/dyuri/xontrib-langenv
[10]: {filename}/prompt_action.md
