Title: Rolling Up The Sleeves
Date: 2025-03-15
Author: crossjam
Status: published

Sometimes, you just gotta roll up your sleeves to try and get back in
the groove.

Sprinkled throughout this blog was usage within [pelican][3] of a
[Python-Markdown][2] extension [pyembed-markdown][1] for plugging in
[pyembed][5]. Pyembed queries OEmbed endpoints and generates
appropriate HTML to, surprise, embed the content from the endpoint.

Unfortunately, the combo had been busted for a bit. The plugin hadn’t
kept up with how Python-Markdown registered plugins. The way tagging
was done had changed. When there were errors probing the endpoint,
pelican wouldn’t generate anyting.

So I spent a leisurely mid-afternoon uncovering the key issues,
locating the point for a fix, and [committing a small fix][4] within a
small personal fork pyembed-markdown. After applying little elisp
magic with [ripgrep][6], [rg.el][7], and [wgrep-ag][8], everything
updated properly even leaving nice messages about bitrot as
appropriate.

[1]: https://github.com/crossjam/pyembed-markdown
[2]: https://github.com/Python-Markdown/markdown
[3]: https://getpelican.com/
[4]: https://github.com/crossjam/pyembed-markdown/commit/65d09094bfb47a4fe1d39decb99bf300ad509dee
[5]: https://pyembed.github.io
[6]: https://github.com/BurntSushi/ripgrep
[7]: https://rgel.readthedocs.io/en/latest/
[8]: https://github.com/mhayashi1120/Emacs-wgrep
