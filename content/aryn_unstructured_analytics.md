Title: Aryn Unstructured Analytics
Date: 2024-12-03
Author: crossjam
Status: published

[Aryn](https://www.aryn.ai/) popped across my radar due to an
[interview][4] with [Matt Welsh][3] (_Go Bears_) in the Data Exchange
Podcast.

> In this episode, we explore how AI is revolutionizing programming
> and software development. We discuss AI-assisted tools like GitHub
> Copilot and ChatGPT, the rise of natural language programming, and
> AI’s expanding role in code review and operating systems. We also
> address challenges in trust and verification of AI-generated code,
> advanced data extraction techniques, and innovative frameworks for
> unstructured analytics.

I’ve become somewhat interested in using domain specific coding
copilots and assistants to tackle various data challenges. [Welsh’s
perspective on the topic][2] is quite useful.

[sycamore][5] seems to be at the center of what they’re
building. Here’s a recent pre-print on their work.

[_The Design of an LLM-powered Unstructured Analytics System_][1]
 ([blog post][6])

> LLMs demonstrate an uncanny ability to process unstructured data,
> and as such, have the potential to go beyond search and run complex,
> semantic analyses at scale. We describe the design of an
> unstructured analytics system, Aryn, and the tenets and use cases
> that motivate its design. With Aryn, users can specify queries in
> natural language and the system automatically determines a semantic
> plan and executes it to compute an answer from a large collection of
> unstructured documents using LLMs. At the core of Aryn is Sycamore,
> a declarative document processing engine, built using Ray, that
> provides a reliable distributed abstraction called DocSets. Sycamore
> allows users to analyze, enrich, and transform complex documents at
> scale. Aryn also comprises Luna, a query planner that translates
> natural language queries to Sycamore scripts, and the Aryn
> Partitioner, which takes raw PDFs and document images, and converts
> them to DocSets for downstream processing. Using Aryn, we
> demonstrate a real world use case for analyzing accident reports
> from the National Transportation Safety Board (NTSB), and discuss
> some of the major challenges we encountered in deploying Aryn in the
> wild.

[1]: https://arxiv.org/abs/2409.00847
[2]: https://www.aryn.ai/post/building-trust-by-closing-the-verification-gap-in-ai-powered-unstructured-analytics
[3]: https://www.mdw.la/
[4]: https://thedataexchange.media/matt-welsh-2024-09/
[5]: https://github.com/aryn-ai/sycamore
[6]: https://www.aryn.ai/post/learn-more-about-unstructured-analytics-in-aryn-s-new-paper
