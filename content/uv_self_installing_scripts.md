Title: uv scripts
Date: 2024-12-25
Status: published

[Trey Hunner](https://treyhunner.com), a seasoned Python trainer and
developer, has been experimenting with `uv` for a number of tasks
including [short script development][1] while also replacing `pipx`
and `pyenv`, two tools I routinely use. He hasn’t completely embraced
a substitution but `uv` does provide an intriguing upside:

> The biggest win that I’ve experienced from uv so far is the ability
> to run an executable script and have any necessary dependencies
> install automagically. 

> This doesn’t mean that I never make Python package out of my Python
> scripts anymore… but I do so much more rarely. I used to create a
> Python package out of a script as soon as it required third-party
> dependencies. Now my “do I really need to turn this into a proper
> package” bar is set much higher. 

This relies on a Python packaging standard [extension mechanism][2]
for embedding metadata in a script.

Pushing this to the limit, would it be possible to declare
[`xonsh`][4] as a dependency and then write the rest of the script in
that [shell language][5]?

[_Via PythonBytes episode 415_][3]

[1]: https://treyhunner.com/2024/12/lazy-self-installing-python-scripts-with-uv/
[2]: https://packaging.python.org/en/latest/specifications/inline-script-metadata/
[3]: https://pythonbytes.fm/episodes/show/415/just-put-the-fries-in-the-bag-bro
[4]: https://xon.sh/
[5]: {filename}/why_xonsh.md
