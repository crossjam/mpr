Title: Working With Git and Pip
Date: 2022-06-19
Author: C. Ross Jam
Status: published

Previously I mentioned [libpytunes][1] and went to kick the tires. I
thought it was published on [PyPI][2] but turns out it wasn’t. So here
I am going `pip install libpytunes` and wondering why I can’t
subsequently do a `import libpytunes`.

I’ve always known you can do `pip install` from a git repository, but
a while back Adam Johnson wrote up [some of the details][3]. There are
plenty of other good overviews out there, (e.g. [Simon Willison’s][4]),
this one just caught my eye recently.

Now `pip install git+https://github.com/liamks/libpytunes` actually
installs the module and my `import` statement works as expected. Bonus, you
can put `git+https://github.com/liamks/libpytunes` into
`requirements.txt` and `setup.py` files as well, to achieve similar
results.

Unfortunately the `liamks` version got hit by a trivial API change in
`plistlib` in Python 3.9, so there was still breakage on my end, but
Anirudh Acharya has [a forked repo][5] with the necessary one
liner fix. Of course I used `pip install git...`, and now [my Music.app
experiments][6] are proceeding apace.

[1]: https://github.com/liamks/libpytunes
[2]: https://pypi.org/
[3]: https://adamj.eu/tech/2019/03/11/pip-install-from-a-git-repository/
[4]: https://simonwillison.net/2022/Apr/24/pip-install-github/
[5]: https://github.com/anirudhra/libpytunes
[6]: {filename}/musicapp_xml.md
