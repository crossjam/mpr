---
title: "Switching to Marimo"
date: 2025-11-26
author: "C. Ross Jam"
status: published
---

[Parul Pandey][2] has a lot of experience with Jupyter Lab and
Notebooks. He switched to Marimo and documented the whys and wins.

> TL;DR: After years of using Jupyter Lab, I have moved most of my
> work to marimo notebooks, a new kind of Python notebook that
> addresses many long-standing issues with traditional ones. This
> article covers the reasons behind my transition and how marimo fits
> naturally into my current workflow, with full gratitude to Project
> Jupyter for building the notebook ecosystem that shaped data
> science, research and education. 

There’s a lot of content, but it captures much of the Marimo upside
that has come across my transom. None of the observations were
particularly new to me, but it’s good to have them in one place.

Pandey’s point on AI integration covered an item I [discussed
previously, JupyterAI][5]

> Marimo also has some really useful AI-assisted coding features built
> in, which have been very helpful for me. To be honest, Jupyter also
> has a JupyterLab extension for AI features called JupyterAI (and
> yes, [I have written about that too][3]), but having AI support built
> into marimo removes a lot of the friction for me. 

[JupyterAI][4] is the Jupyter project’s effort to bring in AI
capabilities. I just generated some top level thoughts, but Pandey
wrote up his experience, [_Build Your Own AI Coding Assistant in
JupyterLab with Ollama and Hugging Face_][3], in depth. It’s good:


> As you can gauge from this article, Jupyter AI makes it easy to set
> up a coding assistant, provided you have the right installations and
> setup in place. I used a relatively small model, but you can choose
> from a variety of models supported by Ollama or Hugging Face. The
> key advantage here is that using a local model offers significant
> benefits: it enhances privacy, reduces latency, and decreases
> dependence on proprietary model providers. However, running large
> models locally with Ollama can be resource-intensive so ensure that
> you have sufficient RAM. With the rapid pace at which open-source
> models are improving, you can achieve comparable performance even
> with these alternatives.

[1]: https://towardsdatascience.com/why-im-making-the-switch-to-marimo-notebooks/
[2]: https://towardsdatascience.com/author/pandeyparul/
[3]: https://towardsdatascience.com/build-your-own-ai-coding-assistant-in-jupyterlab-with-ollama-and-hugging-face/
[4]: https://jupyter-ai.readthedocs.io/en/latest/index.html
[5]: {filename}/jupyter_ai.md
