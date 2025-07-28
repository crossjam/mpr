Title: Adapting Atuin
Date: 2025-07-27
Author: C. Ross Jam
Status: published

As [previously][6] mentioned, [atuin][1] has been something of a
godsend. Interacting with the bash command history is a complete
joy. There’s a minor configuration tweak, illustrated below, that I
want to mention in case it helps someone else out. I prioritized
`session` and `directory` history ahead of `global` for lookup. Tab
sprawl is the name of the game for me, each one like an individual
context. So `session` makes the right place to start even if it’s
initially empty. `global` is just a few `C-r` hits away if needed.

```toml
[search]
## The list of enabled filter modes, in order of priority.
## The "workspace" mode is skipped when not in a workspace or workspaces = false.
## Default filter mode can be overridden with the filter_mode setting.
# filters = [ "global", "host", "session", "workspace", "directory" ]
filters = [ "session", "directory", "global", "host", "workspace" ]
```

The above TOML goes in `~/.config/atuin/config.toml`

Meanwhile, I spent some quality time working on [direnv][2]
configuration. Direnv is less of an immediate win because there’s some
effort needed to add it to existing projects and use it for initiating
new ones. Also, it works more as implicit magic than explicit
navigation. Trey Hunner provided [a good starting point][4] but I’m
molding his approach for my workflow. I’m working on a bash function
to properly setup `.direnv` for my pre-existing `uv` based Python
projects. `pyenv` is going the way of the dodo. Viva la [Frank
Wiles][5].

[zoxide][3] however, is going to take some getting used to. The
directory teleportation mental model needs some burn in.

[1]: https://atuin.sh
[2]: https://direnv.net
[3]: https://github.com/ajeetdsouza/zoxide
[4]: https://treyhunner.com/2024/10/switching-from-virtualenvwrapper-to-direnv-starship-and-uv/
[5]: https://frankwiles.com/posts/my-cli-world/
[6]: {filename}/adopting_atuin.md

