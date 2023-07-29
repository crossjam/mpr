Title: 782 Discogs Data Files
Date: 2022-12-29
Author: C. Ross Jam
Status: published

I wanted to know how many distinct data files (checksums and
compressed XML data) were referenced from
[discogs.data.com](https://data.discogs.com/). This is prelude to
trying to do a, extremely polite, crawl of all the files for some
longitudinal analysis. So I threw together a little script and learned
a few things.

The answer turned out be 782.

------

<!-- PELICAN_END_SUMMARY -->

The script is below. Definitely lots of ways it could be better. The
key lesson was finding the [Requests-HTML][1] library to help deal
with the embedded JavaScript that the Discogs team uses to render the
list of files. N.b. `sleep=1` from line 13 is necessary to get the
HTML rendering properly.

	#!python
	import sys

	from requests_html import HTMLSession

	if __name__ == "__main__":
		session = HTMLSession()

    urls = []

    for year in range(8, 23):
        url = f"https://discogs-data-dumps.s3.us-west-2.amazonaws.com/index.html?prefix=data/20{year:02}"
        resp = session.get(url)
        resp.html.render(sleep=1)
        urls.extend(
            [
                (2000 + year, l)
                for l in resp.html.links
                if l.endswith(".xml.gz") or l.endswith("_CHECKSUM.txt")
            ]
        )

    urls.sort()
    print(f"{len(urls)} in total", file=sys.stderr)
    for i, url in enumerate(urls):
        print(f"{url[0]}, http:{url[1]}")


And here's a CLI run:

	#!bash
	(discogsdata) crossjam@gabrielhounds:~/repos/discogsdata$ ./discogs_data_urls.xsh | wc -l
	/Users/crossjam/.local/pipx/venvs/xonsh/lib/python3.10/site-packages/requests_html.py:727:	DeprecationWarning: There is no current event loop
	  self.loop = asyncio.get_event_loop()
	/Users/crossjam/.local/pipx/venvs/xonsh/lib/python3.10/site-packages/websockets/legacy/client.py:488: DeprecationWarning: remove loop argument
	  warnings.warn("remove loop argument", DeprecationWarning)
	/Users/crossjam/.local/pipx/venvs/xonsh/lib/python3.10/site-packages/websockets/legacy/protocol.py:206: DeprecationWarning: remove loop argument
	  warnings.warn("remove loop argument", DeprecationWarning)
	782 in total
	  782

[Small victories][2].

[1]: https://requests-html.kennethreitz.org/
[2]: https://jvns.ca/blog/2022/03/13/celebrate-tiny-learning-milestones/
