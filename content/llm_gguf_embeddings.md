Title: Embeddings with llm-gguf
Date: 2024-12-22
Author: crossjam
Status: published

I find the ability to create [multi-dimensional embedding vectors][3]
from deep learning models quite fascinating. There’s an obvious
application pattern in [Retrieval Augmented Generation (RAG)][4] with
current LLMs. However, useful embedding models come in a much wider
[range of scales and capabilities][6] then general language models. In
principle, it’s quite possible to train custom embedding models at a
reasonable cost in terms of compute hardware, data scale, and time.

Last month, [Simon Willison updated][2] his [llm-gguf plugin][1] to
support creating embeddings from GGUF models specifically for
embeddings.

> The [LLM docs][5] have extensive coverage of things you can then do with
> this model, like embedding every row in a CSV file / file in a
> directory / record in a SQLite database table and running similarity
> and semantic search against them.

This could come in handy since I have a few piles of content laying
around where using embeddings to supplement search and retrieval would
be an interesting experiment.

[1]: https://github.com/simonw/llm-gguf
[2]: https://simonwillison.net/2024/Nov/21/llm-gguf-embeddings/
[3]: https://vickiboykis.com/what_are_embeddings/
[4]: https://en.wikipedia.org/wiki/Retrieval-augmented_generation
[5]: https://llm.datasette.io/en/stable/embeddings/index.html
[6]: https://huggingface.co/models?other=text-embeddings-inference
