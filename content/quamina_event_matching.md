Title: Quamina Event Matching
Date: 2022-05-21
Status: published

[Tim Bray][2] is an Internet Person of [Some Renown][3] (TM) that I’ve long
admired from many angles: as a software developer, as a blogger, and
as a public thinker with considered political and cultural views. As a
hacker, the urge to code never seems to wane, so he’s open sourced a
library, [Quamina][4], for doing event matching at Amazon scale.

Many moons ago, a gentleman named [Bob Wyman][6] was the publicly web
facing technical brains behind [PubSub.com][5]. Wyman advertised the
provided service as "prospective search" against blogs, represented
mainly by RSS feed content, among other "real-time" things on the ’Net
during that period. You could upload matching patterns and then follow
streams of content items that matched the patterns. As a business, it
didn’t quite work out, but I remember Wyman occasionally dug into the
underlying algorithms that made massive numbers of patterns
effectively match with low latency. I’ve fruitlessly tried to
rediscover his musings to no good effect.

So Quamina looks like a modern take on the core algorithmic challenge
within PubSub: taking extremely large numbers of patterns and matching
content in extremely low amounts of time. Patterns are expressed as
JSON and match against JSON objects. Given that many popular formats
have known, or well understood, mappings into JSON it shouldn’t be
hard to test Quamina against a wide range and scale of
datasets. Sounds like a benchmarking challenge waiting to happen.

I’m glad Bray released Quamina and I’ll definitely be digging in
trying to understand how it works. If I was a halfway decent Go
programmmer, I would take a quick stab at wrapping some kind of
RESTful API around it and seeing how close I could make it look like
my memories of PubSub. So many ideas, so little time.

_Although, if Quamina is fast enough, a cheap proof of concept could
be done by wrapping something like Python’s [FastAPI][7] around subprocess
invocation of the Go executable. Hmmmmm._

[1]: https://www.tbray.org/ongoing/When/202x/2022/05/12/Quamina
[2]: https://www.tbray.org/
[3]: https://www.tbray.org/ongoing/misc/Tim
[4]: https://github.com/timbray/quamina
[5]: https://en.wikipedia.org/wiki/PubSub_(website)
[6]: https://www.linkedin.com/in/bobwyman
[7]: https://fastapi.tiangolo.com/
