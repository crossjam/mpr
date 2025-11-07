---
title: "Not Standing Still: Jupyter AI"
author: "C. Ross Jam"
date: 2025-11-06
status: published
---

[Previously][2] I’ve noted my appreciation for
[marimo](https://marimo.io) notebooks, especially how their reactive
cell model was different from [Jupyter](https://www.jupyter.org)
notebook. Marimo has also been developing [an interesting narrative][3]
around [integration with agentic coding][3].

> In this blog we explain why agentic coding tools like Claude work
> exceptionally well with marimo, especially when compared to other
> notebooks such as Jupyter. We also share tips on how to best use
> Claude when working with marimo. While this blog focuses on Claude
> Code, you don’t have to use your terminal if you don’t want to: in a
> future blog post we’ll describe how marimo provides a
> batteries-included AI-native editor, with a best-in-class experience
> for working with LLMs and your data in a single development
> environment 

However, Jupyter is an established, robust, and large ecosystem. With
a lot of smart people at the forefront of data science and machine
learning. So I should have known the Jupyter team would not stand
still in the face of AI advances.

Enter [Jupyter AI][1]

<!-- PELICAN_END_SUMMARY -->

> Welcome to Jupyter AI, which brings generative AI to
> Jupyter. Jupyter AI provides a user-friendly and powerful way to
> explore generative AI models in notebooks and improve your
> productivity in JupyterLab and the Jupyter Notebook. More
> specifically, Jupyter AI offers: 
>
> - An %%ai magic that turns the Jupyter notebook into a reproducible
>   generative AI playground. This works anywhere the IPython kernel
>   runs (JupyterLab, Jupyter Notebook, Google Colab, VSCode, etc.). 
>
> - A native chat UI in JupyterLab that enables you to work with
>   generative AI as a conversational assistant. 
>
> - Support for a wide range of generative model providers and models
>   (AI21, Anthropic, Cohere, Gemini, Hugging Face, MistralAI, OpenAI,
>   SageMaker, NVIDIA, etc.). 

That’s a solid marketing pitch. A few years ago I had started poking
at the precursor to Jupyter AI for some work activities. One of me or
the framework, maybe both, wasn’t mature enough to intimate all the
downstream implications. Also, agentic coding wasn’t really a thing at
that stage.

However, I became really smitten when I started working through a
course at Deeplearning.AI: [_Jupyter AI: AI Coding in
Notebooks_][5]. The course features [Brian Granger][6], one of the
originators of the Jupyter project, in addition to Andrew Ng.

> About this course
>
> Learn to use Jupyter AI as your notebook coding partner in this
> short course, taught by Andrew Ng and Brian Granger, co-founder of
> Project Jupyter. 
>
> Coding practices are shifting from manual coding to AI-assisted
> development,  and Jupyter AI allows you to integrate AI coding into
> all your notebook development workflows. Many AI coding assistants
> struggle to function well within the notebook environment, the
> Project Jupyter team has introduced Jupyter AI, which is an
> open-source framework that deeply integrates AI coding and
> collaboration into Jupyter notebooks and JupyterLab. 
>
> Jupyter AI provides a chat interface that you can use to generate
> new cells in your notebook. You can also drag existing cells into
> the chat for debugging, attach files for context, and save chat
> histories to reuse later as additional context for your work.

Even about two thirds of the way through the course I’ve found
Jupyter’s conversational assistant approach to AI integration
intriguing. In essence, a user leans on an open AI chat window in
parallel with an open notebook. A little bit of UI chrome makes it
easy to transfer AI content to cells and cells into AI prompts. It’s
not as silky smooth as I would like, but the notion of working on a
notebook in "immediate mode" as a computational artifact feels
promising as a conceptual model. I’ll have to cross check, but this seems
like a distinctly different style from the marimo way of pointing the
AI at the code underlying the notebook implementation. For marimo that
makes total sense since their notebooks are just Python code. Thankfully,
this doesn’t have to be a competition. Let a thousand flowers bloom.

Personally, I’d like to see Jupyter AI ease the path of having the AI
manipulate the notebook from natural language prompts. Currently you
have to click buttons to do many of the content exchanges between the
two sides. Since a notation for referring to cells already exists,
courtesy of IPython, maybe a handful of tools could be added to make
this easier. I wonder how far you could get with `read_cell` and
`write_cell` tools, baked in?

So much room for experimentation. Part of the reason I’m skeptically
optimistic about AI and coding are examples like this of the
exploration space. There’s lots of possible ways to invent the future
and lots of folks exploring as they please. Exciting times!

[1]: https://jupyter-ai.readthedocs.io/en/v2/
[2]: {filename}/the_marimo_moment.md
[3]: https://marimo.io/blog/claude-code
[4]: https://marimo.io/blog/beyond-chatbots
[5]: https://www.deeplearning.ai/short-courses/jupyter-ai-coding-in-notebooks/
[6]: https://aws.amazon.com/blogs/machine-learning/announcing-new-jupyter-contributions-by-aws-to-democratize-generative-ai-and-scale-ml-workloads/
