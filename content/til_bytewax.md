Title: TIL Bytewax
Date: 2022-07-11
Author: C. Ross Jam
Status: published

TIL about [Bytewax][1]

> Bytewax is an open source Python framework for building highly
> scalable dataflows in a streaming or batch context.

<!-- PELICAN_END_SUMMARY -->

Heard about the project [via a Python Podcast.\_\_Init\_\_
episode][2]. Being a Message Processing Nerd (TM), I was both excited
and skeptical. There have been a fair number of Python stream
processing libraries, none of which I’ve really cottoned to, primarily
because they often seem like second class citizens in a Java world. 

<iframe title="Podlove Web Player: The Python Podcast.__init__ -Stream Processing In Real Time And At Scale In Pure Python WithBytewa" width="400" height="200"
src="https://cdn.podlove.org/web-player/share.html?episode=https%3A%2F%2Fwww.pythonpodcast.com%2Fwp%2F%3Fpodlove_player4%3D755"
frameborder="0" scrolling="no" tabindex="0"></iframe>

Bytewax takes a different angle, tightly coupling with Rust. And when
Zander Matheson, CEO and co-founder of [bytewax](bytewax.io), started
riffing on [Frank McSherry’s "Scale at What COST?"][3] and [timely
dataflow][4] then I became really intrigued. I will definitely have to
give this framework a testdrive.

[1]: https://github.com/bytewax/bytewax
[2]: https://www.pythonpodcast.com/bytewax-python-stream-processing-episode-370/
[3]: {filename}/at-what-cost.md
[4]: https://timelydataflow.github.io/timely-dataflow/
