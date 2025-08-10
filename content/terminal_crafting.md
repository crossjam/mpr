Title: Terminal Craft Time Sink
Date: 2025-08-09
Author: C. Ross Jam
Status: published

Hola peeps! It’s been a minute. Time for an update.

Nothing major on the life front. In fact, a bit of summer relief from
the tyranny of kid activity. I’ve actually been able to sleep in a few
days. And work slogs on per usual.

On the personal tech front though, I’ve been spending some quality
time seriously reworking my terminal lifestyle. The last couple of
posts hint at what’s been going on. Those were just initial steps and
much more buffing, waxing, polishing, and refinement were
needed. Let’s dive in ...

<!-- PELICAN_END_SUMMARY -->

A quick recap. Thanks to [this post from Frank Wiles][1], I started
reworking my command line tooling. Here’s his money quote:

> Ok, to be clear, yes I still ssh into the occasional server but now
> 99% of my time in a shell is local on MY laptop. 

> So I can customize the hell out of it!

I’ve also caught the [uv][3] bug and a Trey Hunner article
["_Switching from virtualenvwrapper to direnv, Starship, and uv_"][2]
intriguingly brought that into the mix for command line tooling
supporting Python project work. To top it off Hynek Schlawack started
[a bananas video series][4] diving deep on his approach.

This has resulted in me going all in with [starship][8], [atuin][5],
[direnv][6], and [zoxide][7]. There’s a side order of [fzf][9],
[ripgrep][10], and [fd][11].

The result has been a pleasant change. I’m quite surprised at how much
I enjoy the bling that starship brings to the prompt. It’s actually
useful to get that quick orientation about where in "project space"
I’m currently working. Atuin has transformed my relationship with bash
history. So much better. Direnv takes the grunge out of making sure
you have the right API keys and other environment variables set for a
specific project. Zoxide is getting there. I have to break my habit of using
pushd/popd and get used to it’s approach of space-tab completion with
fzf and the feeling of directory teleportation. Gettin’ there.

A fundamental underlying change is that I now longer think in bespoke
Python virtual environments unmoored from code efforts. This is where
[pyenv][21] really shined for me. The potential for customized Python
builds was tempting but I never really put it to use. Turns out uv
handles the multiple Python version issue well enough without really
needing to wade into custom builds. Meanwhile, my heavily bespoke
venvs were effectively tied to specific projects anyway. Soooo, just
bundle them into the same working directory and use uv to kit them out
fast and easy.

### The Knock On Effects

That shouldn’t have been so absorbing as to keep me from posting for
over a week though. What happened?

The shell configuration cascaded into me doing significant work on 1)
shell integration with [GNU Emacs][21] (_shout out [emacs-plus][23]_)
and 2) [my homespun dotfiles management system][12]. The former
because in addition to having a million terminal tabs open at any
given moment, I also have an Emacs instance running with multiple
shells inside of that, _(don’t judge)_. The latter because I needed to
propagate all of this shell goodness to the multiplicity of machines I
use on a daily basis, _(again, don’t judge)_.

**On Emacs**. The comint shell in Emacs is the workhorse that I’ve
been using for decades now. But it’s not quite a real shell. Still
with a bit of bash dotfile (.bash_profile and .bashrc) fixing up, my
new improved shell life worked well. The fiddliest bit was directory
syncing where Emacs relied on watching for `cd` commands to line
itself up with where the shell was. That led to an adventure
generating elisp with ChatGPT and Claude to effectively reimplement
directory tracking by having the directory always in the shell
prompt. This turns out to work well for the one thing I really need it
for, opening files from the shell’s working directory using C-x C-f. 

Really it’s the little things in life.

Unfortunately, while the comint interface is pretty shell like, it’s
not an honest to goodness fully compliant terminal. This means fancy
dancy tools that depend on such compliance, like atuin, don’t fit
well. After picking up a bit of muscle memory on those tools, this
begins to grate. Is there a way out?

C’mon. It’s emacs so you know the answer.

> [Emacs-libvterm (vterm)][13] is fully-fledged terminal emulator inside GNU
> Emacs based on libvterm, a C library. As a result of using compiled
> code (instead of elisp), emacs-libvterm is fully capable, fast, and
> it can seamlessly handle large outputs.

I can confirm it really is a full blown, fully compliant, fast
terminal emulator inside of The Deities’ Chosen Editor. All my new
terminal kit works well in vterm. I’m sorting through a few impedance
mismatches. Directory tracking had a similar problem as comint, but
the explicit directory in the prompt trick wasn’t enough for
vterm. Some serious bash shell fu and prompt configuration (way down
in [the advanced configuration of starship][20]) can get vterm to ship
a message into Emacs, so I think I have this sorted. But it took quite
a bit of time down in this rabbit hole. Lastly to top it off many of
the key essential Emacs bindings get passed on to the terminal, which
means my beloved C-x C-f has been hijacked. Haven’t quite solved this
puzzle yet. Still work to do.

**On Homely**. [Homely][19] has been my means for [automating my
dotfiles][14] management and distribution for well nigh 6 years. It’s
been stable and productive. There’s something comforting about `git
cloning` a repo, running a single shell script, and enjoying an
exquisite terminal and Emacs experience. However, incorporating all
this new shell configuration and CLI tooling induced a serious revisit
of my Homely specification. I also dug in and worked on cleaning up a
lot of janky failures and edge cases to make it repeatably deployable
across platforms. Even on freshly minted Raspberry Pi 4’s with "only"
1GB of RAM.

Some observations from this part of the effort:

- Switching away from using python, [pip `--user` package install][15]
  (which Debian and Linux discourage), and pipx to bootstrap a number
  of tools was a significant win.  Instead I now just rely on uv’s
  shell install to get that bootstrapped and then `uv tool install`
  makes pulling in follow on Python tools (including pipx if needed)
  easy to install without conflicting with any system Python

- Raspberry Pi OS packages lag quite a bit from the latest Debian and
  Ubuntu. Some things that Homebrew has are missing (no fzf? really?)
  including a few of the ones I was moving to from the Rust
  ecosystem. No problem, Rust has a great package ecosystem with
  [rustup][16] and [cargo][17]. This worked well on machines reasonably resourced
  with CPU and RAM. Even [an ancient white plastic MacBook][18].
  
- An RPi with 1GB of RAM? Not so much. Rust compilation can be really
  RAM hungry. Locked up the device once or twice trying to build
  zoxide from crates. Lesson learned, just script out retrieval of
  build artifacts from GitHub. Easy peasy with a coding assist from
  the AIs.
  
Okay, that’s way more than anyone wanted to hear about my personal
shell setup, but it felt good to get this narration out into the
world. At least ya’ll got a boatload of links. I’ll probably carve out
a few bits as posts on their own since they involve relatively obscure
corners of shell and Emacs configuration. Maybe some public posts can
help other folks sort their specific situations out. I tell you, there
was a lot of digging in GitHub issues, honest to gosh tool
documentation reading, and false pathing with AIs. It was a blast
heads down cranking away on this for a few days straight.

And there’s still so much more to do 🚀!!

[1]: https://frankwiles.com/posts/my-cli-world/
[2]: https://treyhunner.com/2024/10/switching-from-virtualenvwrapper-to-direnv-starship-and-uv/
[3]: https://docs.astral.sh/uv/
[4]: https://youtu.be/mFyE9xgeKcA?si=Ljea6VIxb64I-O95

[5]: https://atuin.sh
[6]: https://direnv.net
[7]: https://github.com/ajeetdsouza/zoxide
[8]: https://starship.rs
[9]: https://junegunn.github.io/fzf/
[10]: https://github.com/BurntSushi/ripgrep
[11]: https://github.com/sharkdp/fd
[13]: https://github.com/akermu/emacs-libvterm
[15]: https://pip.pypa.io/en/stable/user_guide/#user-installs
[16]: https://rustup.rs
[17]: https://doc.rust-lang.org/stable/cargo/
[19]: https://homely.readthedocs.io/
[20]: https://starship.rs/advanced-config/#custom-pre-prompt-and-pre-execution-commands-in-bash
[21]: https://github.com/pyenv/pyenv
[22]: https://www.gnu.org/software/emacs/
[23]: https://github.com/d12frosted/homebrew-emacs-plus
[12]: https://github.com/crossjam/dotfiles
[14]: {filename}/homely-dotfile-management.md
[18]: {filename}/happiness_is_a.md
