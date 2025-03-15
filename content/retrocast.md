Title: retrocast
Date: 2024-12-12
Status: published
Author: crossjam

Thought exercise in action here.

I’ve been peripherally aware of [`uv`][1] for a bit. Now I’m ready to
dive in deeper. But the buzz on `uv` has been building for a
bit. What’s the aggregate knowledge in RSS feeds and podcast
subscriptions on `uv`?

If only I had a personal tool that could retrospectively search my
personal content to answer the request "Build a [precis][13] on `uv` for me".

The ground is fertile for a tool I’m calling _retrocast_ that would
fit that bill. It would be a personal app hooking into all your
feeds and constantly indexing the content. Layer in some text search,
semantic search, knowledge graphs, and LLMs to craft products, not
just 10 blue links.

Some components for inclusion and inspiration

* The [Feedbin API][2] using Feedbin’s backend as a feed database
* [Airshow][4] and [Overcasat][3] as podcasat players that make their
  data accessible
* Local embedded dbs and search engines such as [SQLite][7],
  [Kuzu][8], and [meilisearch][6]
* Local LLMs via [ollama][9] and [llamafile][10]
* [NotebookLM][11] and [Kagi Assistant][12] for UX ideas
* Simon Willison’s [llm][14] to glue it all together

[1]: https://docs.astral.sh/uv/
[2]: https://github.com/feedbin/feedbin-api
[3]: https://overcast.fm/
[4]: https://airshow.fm/
[6]: https://github.com/meilisearch/meilisearch
[7]: https://sqlite.org/
[8]: https://kuzudb.com/
[9]: https://ollama.com/
[10]: https://github.com/Mozilla-Ocho/llamafile
[11]: https://notebooklm.google
[12]: https://help.kagi.com/kagi/ai/assistant.html
[13]: https://en.wiktionary.org/wiki/pr%C3%A9cis#English
[14]: https://llm.datasette.io/en/stable/
