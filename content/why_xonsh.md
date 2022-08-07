Title: Why xonsh?
Date: 2022-07-01
Author: C. Ross Jam
Status: published

I was dorking around last night and came up with the following in
about 15 minutes of work in [`xonsh`][1] command line session.
	
	:::python
	from pathlib import Path
   	for fname in !(ls *.wav):
		p = Path(fname.strip())
		ffmpeg -i @(p) -c:a libfdk_aac -b:a 128k @(f"{p.stem}.m4a")

🎉 💥 💥 🎉

<!-- PELICAN_END_SUMMARY -->

That’s mostly Python, with an escape out to the `ffmpeg` Swiss army
knife media encoder command. The `!()` mechanism runs a UNIX command
and captures the subprocess output is an input stream, ready for
line-by-line processing. The `@` markers signal where I’m splicing in
computed arguments from the outer Python context. Four lines of code
and I’ve converted a collection of `wav` files to `m4a` content
that’s more compatible with Apple’s Music.app. "More" meaning I can
eventually add the appropriate music metadata from Discogs data.

One of the beauties of `xonsh` (and there are multiple beautiful
things) is that it makes those shell calls trivial. No importing
modules. No building up lists of command args. No function
invocations. This is a superpower of Perl and obviously of shells like
`bash` themselves. It’s just really nice to have it in Python, because
I don’t have to remember the syntax of loops, variables, string
manipulation, etc. And you can make an argument that it’s a better
designed language. This approach is really for dedicated Pythonistas,
so I’m not encouraging folks to switch over, but for me it’s pretty
close to transformative. Even though I’ve been writing code for 30+
years, I’m embarrased to say I’m actually scared of shell programmming
😔. Now I don’t have to fear shell scripting the UNIX way any more!

[1]: https://xon.sh/
