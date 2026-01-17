---
title: TIL orjson
date: 2026-01-16 21:45
author: C. Ross Jam
status: published
---

TIL: [orjson]

> orjson is a fast, correct JSON library for Python. It benchmarks as the
> fastest Python library for JSON and is more correct than the standard json
> library or other third-party libraries. It serializes dataclass, datetime,
> numpy, and UUID instances natively.
>
> orjson.dumps() is something like 10x as fast as json, serializes common types
> and subtypes, has a default parameter for the caller to specify how to
> serialize arbitrary types, and has a number of flags controlling output.
>
> orjson.loads() is something like 2x as fast as json, and is strictly compliant
> with UTF-8 and RFC 8259 ("The JavaScript Object Notation (JSON) Data
> Interchange Format").

_Via a rambling [TalkPython Podcast episode][diskcache-podcast] about the
[diskcache] module._

[diskcache]: https://grantjenks.com/docs/diskcache/
[diskcache-podcast]: https://talkpython.fm/episodes/show/534/diskcache-your-secret-python-perf-weapon
[orjson]: https://github.com/ijl/orjson
