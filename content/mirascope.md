---
title: "Mirascope and Lilypad"
date: 2025-12-19 20:00
author: "C. Ross Jam"
status: published
---

Link parkin’: [Mirascope][1] for programming with LLMs

> Mirascope is a powerful, flexible, and user-friendly library that
> simplifies the process of working with LLMs through a unified
> interface that works across various supported providers, including
> OpenAI, Anthropic, Mistral, Google (Gemini/Vertex), Groq, Cohere,
> LiteLLM, Azure AI, and Bedrock. 
>
> Whether you're generating text, extracting structured information,
> or developing complex AI-driven agent systems, Mirascope provides
> the tools you need to streamline your development process and create
> powerful, robust applications. 

And [Lilypad][2] for [observability and context engineering][3]

> Context engineering refers to structuring everything an LLM sees so
> it provides the right response. This involves curating and
> sequencing the information that’s sent to the model, a task that
> goes beyond just writing prompt instructions. 
>
> ...
>
> That's why we built Lilypad, a context engineering framework that
> versions, traces, and evaluates everything influencing an LLM’s
> output, not just the prompt, allowing you to reproduce, compare, and
> improve every input, parameter, and piece of context systematically,
> rather than through trial and error. 

I’m eyeing Lilypad as a light(ish)weight option for getting started
with AI evals on a small scale. The [Docker Compose deployment][6] to
launch the necessary services doesn’t look too bad, only kicking off
Zookeeper, Kafka, Postgres, and Lilypad containers. And with [a
modernized version of Kafka][7] you could probably kill the Zookeeper
process to lighten the load a bit.

The TalkPython course on [LLM Building Blocks for Python][4] has some
coverage on Mirascope:

> Dive into LLM Building Blocks for Python, a concise 1.2-hour video
> course that equips you with everything you need to integrate large
> language models into your Python applications. You’ll learn to move
> beyond “text in → text out” by turning your prompts into structured
> data, orchestrating chat-style workflows, and building interactive
> prototypes. From rapid-fire notebook experiments to production-ready
> async pipelines and caching, this course gives you practical,
> code-first techniques for real-world LLM development. 

I actually went through the course when it first came out in the
middle of the summer (shout out again [Vincent Warmerdam][8]), but it
didn’t really sink in. Now, with the benefit of more experience with AI
API client frameworks, it makes more sense. The decorator and "prompt
function" styles feel attractive. Also, Vincent didn’t cover Lilypad,
which I’m hoping can provide a starter kit deployment for prototyping
processes around [LLM product evals][5].

[1]: https://mirascope.com/docs/mirascope
[2]: https://mirascope.com/docs/lilypad
[3]: https://mirascope.com/blog/context-engineering-platform
[4]: https://training.talkpython.fm/courses/llm-building-blocks-for-python
[5]: https://hamel.dev/blog/posts/evals-faq/
[6]: https://github.com/Mirascope/lilypad/blob/main/app/docker-compose.yml
[7]: https://www.redpanda.com/guides/kafka-tutorial-kafka-without-zookeeper
[8]: https://koaning.io


