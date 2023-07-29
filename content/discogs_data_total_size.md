Title: Discogs Data Total Size
Date: 2022-12-30
Author: C. Ross Jam
Status: published

The next question I have about the Discogs Data is what’s the total
amount to download? An initial step is updating my [URL gathering
script][1] to grab the `Content-Length` header from an http probe of
each url and start generating csv compatible output.

-----

<!-- PELICAN_END_SUMMARY -->

Below is the tweakage. The script has moved from straight Python to a
[`xonsh`](https://xon.sh) script. The most interesting piece is line 6
where I shell out to use [`httpie`][2] to make a HEAD request against
the url. The `@` splices the value of the `furl` variable into the
command line from the outer Python context, while `!` captures the
output of the inner subcommand for processing in the outer Python
context.

	#!python
	urls.sort()
    print(f"{len(urls)} in total", file=sys.stderr)	
	for i, url in enumerate(urls):
        clength = -1
        furl = "http:" + url[1]
    	for line in !(http --headers HEAD @(furl)):
            if line.strip().startswith("Content-Length"):
                h, v = line.split()
                clength = int(v)
        print(f"{url[0]}, http:{url[1]}, {clength}")

Still need to pull in the `csv` module for proper output generation. I
also want to add the http headers as a column of json data, which will
definitely need correct `csv` escaping. Once that's all in place, it
should be possible to [pipe the output into][4] Simon Willison's
[`sqlite-utils`][3] to create an SQLite DB, then run a query to compute the
total storage.

This is why I love `xonsh`. I had to do a _little_ documentation
reading to get the right sigils (`!`, `@`) in the right places, but
once done I can still actually comprehend what the script is doing. If
I keep working at it, this should become mental muscle memory and make
writing such scripts completely natural. Might be better off learning
`bash` in depth, but this fits my brain way cleaner.

Using questions to be asked of data seems to be a good driver for me to
actually write code. Boy do I have plenty of questions for this data.

[1]: {filename}/782_discogs_data_files.md
[2]: https://httpie.io/
[3]: https://github.com/simonw/sqlite-utils
[4]: https://sqlite-utils.datasette.io/en/stable/cli.html#inserting-csv-or-tsv-data
