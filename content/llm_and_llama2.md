Title: llm and Llama 2
Status: published
Date: 2023-08-04

The prolific Simon Willison has put together [`llm`][1], a Python library and CLI
for messing around with AI:

> A CLI utility and Python library for interacting with Large Language
> Models, including OpenAI, PaLM and local models installed on your
> own machine.

Eminently convenient is a plugin mechanism that supports [usage of
local open source models][2]. 

I followed the directions on the tin and was able to run the latest
[Llama 2 model][3] on my M2 MacBook within about 15 minutes. Most of that
time was spent waiting for downloads. 

However, the model does run as slowly as advertised, taking about 20
seconds to respond to a prompt. Still, it’s nice to not be beholden to
our Big Tech overlords for ungoverned experimentation. OpenAPI access
is definitely **not** cheap!

[1]: https://llm.datasette.io/en/stable/
[2]: https://simonwillison.net/2023/Jul/12/llm/
[3]: https://ai.meta.com/llama/
