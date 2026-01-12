---
title: trackio
date: 2026-01-12 16:00
author: C. Ross Jam
status: published
---

A lighter-weight experiment tracking framework with an [SQLite
mentality][sqlite-mentality] could be quite useful as an alternative
to [MLflow][mlflow].

Enter [trackio][trackio] from Hugging Face.

> trackio is a lightweight, free experiment tracking Python library built by
> Hugging Face 🤗.
>
> ...
>
> Trackio is designed to be lightweight (the core codebase is <5,000 lines of
> Python code), not fully-featured. It is designed in an extensible way and
> written entirely in Python so that developers can easily fork the repository
> and add functionality that they care about.

And from the Hugging Face team’s [blog post][trackio-blog-post]:

> TL;DR: Trackio is a new, open-source, and free experiment tracking Python
> library that provides a local dashboard and seamless integration with Hugging
> Face Spaces for easy sharing and collaboration. Since trackio is a drop-in
> replacement for wandb, you can get started with the syntax you already know!
>
> **Background**
>
> If you have trained your own machine learning model, you know how important it
> is to be able to track metrics, parameters, and hyperparameters during
> training and visualize them afterwards to better understand your training run.
>
> Most machine learning researchers use specific experiment tracking libraries
> to do this. However, these libraries can be paid, require complex setup, or
> lack the flexibility needed for rapid experimentation and sharing.

They note some further reasons they switched to trackio internally, including:

- Easy sharing and embedding
- Standardization and transparency
- Data accessibility
- Flexibility for experimentation

I think MLflow is a nice piece of kit, although it has been succumbing to scope
creep and API sprawl in recent versions. That said, its wide integration with
the popular ML toolkits is definitely convenient. Haven’t really had a chance
to use [Weights and Biases][wandb], since it doesn’t seem particularly friendly
to self-hosting. I’ll be giving trackio a test drive to see how it compares to
both and whether it lives up to its claims.

[mlflow]: https://mlflow.org/
[trackio]: https://github.com/gradio-app/trackio
[trackio-blog-post]: https://huggingface.co/blog/trackio
[wandb]: https://github.com/wandb/wandb
[sqlite-mentality]: https://sqlite.org/whentouse.html
