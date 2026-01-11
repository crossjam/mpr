---
title: Pydantic Gateway
date: 2026-01-10 22:45
author: C. Ross Jam
status: published
---

The folks at [Pydantic](https://pydantic.dev) are building up quite
the [AI stack][2]. Their new to me [AI Gateway][1] would rival
[LiteLLM][3] with a second-mover advantage.

> Pydantic AI Gateway is a unified interface for accessing multiple AI providers
> with a single key. Features include built-in OpenTelemetry observability,
> real-time cost monitoring, failover management, and native integration with
> the other tools in the Pydantic stack.

If you haven’t gotten a taste of Pydantic’s leader, Samuel Colvin, give this
[episode of the AI Engineering Podcast][4] a listen. Colvin’s a hoot; he often
calls out the engineering quality of other frameworks. Here’s a skoosh of what
he’s cooking from [the Pydantic AI Gateway announcement blog post][5]:

> ### Why another Gateway?
>
> - We could see it was a pain point for our customers.
> - We knew we could build something with higher engineering quality and better
>   chosen abstractions.
> - We are uniquely positioned to offer a better developer experience via
>   integrations with the existing Pydantic Stack (specifically Pydantic AI and
>   Logfire).
>
> Most "AI gateways" are the wrong kind of abstraction.
>
> They try to wrap every provider in a single "universal schema" that slows you
> down. Every time a model adds a feature: tool calling, image input, JSON mode
> \- you wait weeks for the gateway to catch up.
>
> PAIG takes a different approach: **one key, zero translation**.

I am a big fan of Pydantic’s validation approach and often find their
Python libraries to be well designed. Let’s see if it works for
infrastructure.

[1]: https://ai.pydantic.dev/gateway/
[2]: https://ai.pydantic.dev/
[3]: https://www.litellm.ai
[4]: https://www.aiengineeringpodcast.com/episodepage/building-production-ready-ai-agents-with-pydantic-ai
[5]: https://pydantic.dev/articles/gateway-open-beta
