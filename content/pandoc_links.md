Title: Pandoc Stuff
Author: crossjam
Date: 2021-08-13
Category: Uncategorized
Status: published

Link parkin’: [panflute][2]

All of this blog’s content is written in Markdown. As a side project,
I’m interested in working on a homegrown solution for search. Enter
[Pandoc][1] for doing some of the heavy lifting on document
parsing and generating an Abstract Syntax Tree. Thence to panflute for
spitting out into a format that could be indexed using [sqlite FTS][3]
to get started and then [Manticore][4] just for giggles.

[1]: https://pandoc.org/index.html
[2]: http://scorreia.com/software/panflute/
[3]: https://simonwillison.net/2019/Jan/7/exploring-search-relevance-algorithms-sqlite/
[4]: https://manticoresearch.com/


