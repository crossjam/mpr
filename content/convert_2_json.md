---
title: "convert2json"
date: 2025-11-13
author: "C. Ross Jam"
---

Link parkin’: [convert2json][1], [GitHub repo][2]

> Utilities for use on the command line to convert BSON, CBOR, CSV,
> INI, MessagePack, Plist, RSV, TOML, XML, & YAML to JSON. For each
> supported format, there is a tool for use in a pipe as well as a
> wrapper that passes the converted input or files in the arguments
> to jaq or jq for further querying and processing. 

This is one of the few tools I’ve seen that’s both fast and reasonably
error-resistant for converting XML to JSON. 

I have [a work in progress repository][3] for turning [Discogs Data
Dumps][4], which are big to ginormous, into a DB ingest-friendly
format. The dumps are in XML. The goal is XML --> [JSONL][6] --> [Parquet][7]
--> DBs. discogs-xml2db is written in Python, and to date, I have only
been able to get it so robust (old datasets are sketchy with
[mojibake][5] and ill-formed XML) and performant (newer datasets are
gigabytes of compressed XML). I’m going to give a coding agent a
chance, but I’m not all that hopeful.

In the event that route doesn’t pan out, I’ll fall back to wrapping
`convert2json`, crate, or binary CLI within a Python module. It could be
an interesting experiment just by itself.

[1]: https://crates.io/crates/convert2json
[2]: https://github.com/simonrupf/convert2json
[3]: https://github.com/crossjam/discogs-xml2db
[4]: https://data.discogs.com/
[5]: https://en.wikipedia.org/wiki/Mojibake
[6]: https://jsonlines.org
[7]: https://parquet.apache.org
