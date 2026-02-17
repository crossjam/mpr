---
title: Routing to Identity
date: 2026-02-16 19:56
author: C. Ross Jam
status: published
---

I still haven’t quite grokked the entire concept, but Sam Ruby recently posted
about ["routing to identity"][routing-to-identity-post]:

> ### A Different Architecture
>
> Kubernetes routes to capacity — any healthy pod can serve any request. Cell
> orchestration routes to identity — a request for this team's board or this
> event's scores must reach the specific instance that holds that data. These
> are fundamentally different problems, and everything downstream follows from
> which one you're solving.
>
> When you route to capacity, you separate compute from storage, make pods
> fungible, and scale by adding replicas. When you route to identity, compute
> and storage fuse together — a SQLite file lives with the code that serves it.
> You scale by creating more cells, not bigger ones. Cells sleep when idle, wake
> on demand, and can be disposed of when they've served their purpose.

He opened the conversation with a call out to [cells][aws-cells]:

> LLM conversations are cells. Each has a unique identity, carries its own
> state, needs to be routed specifically, is active in bursts, and is
> fundamentally disposable. The explosive demand for this pattern forced
> infrastructure providers — Cloudflare with Agents, Fly.io with Sprites,
> Akamai's Fermyon with Spin — to build first-class support for identity-routed,
> stateful, hibernatable compute. They built it for AI. It turns out it's the
> right infrastructure for any application where data partitions along
> human-scale collaboration boundaries.

And chasing the pointer into the AWS documentation, here’s what constitutes a
cell-based architecture:

> A cell-based architecture comes from the concept of a bulkhead in a ship,
> where vertical partition walls subdivide the ship's interior into
> self-contained, watertight compartments. Bulkheads reduce the extent of
> seawater flooding in case of damage and provide additional stiffness to the
> hull girder.
>
> ...
>
> The overall workload is partitioned by a partition key. This key needs to
> align with the grain of the service, or the natural way that a service's
> workload can be subdivided with minimal cross-cell interactions. Examples of
> partition keys are customer ID, resource ID, or any other parameter easily
> accessible in most API calls. A cell routing layer distributes requests to
> individual cells based on the partition key and presents a single endpoint to
> clients.
>
> A cell-based architecture uses multiple isolated instances of a workload,
> where each instance is known as a cell. Each cell is independent, does not
> share state with other cells, and handles a subset of the overall workload
> requests. This reduces the potential impact of a failure, such as a bad
> software update, to an individual cell and the requests that it's processing.
> If a workload uses 10 cells to service 100 requests, when a failure occurs in
> one cell, 90% of the overall requests would be unaffected by the failure.

Ruby (the person) argues that the new era of isolation for AI agents, especially
within cloud providers, is an ideal fit for route-to-identity, with wide
implications for building applications and services. The only bit I’m noodling
over is which identity mechanisms to use for designation and dispatch. I’ll have
to go back and take a closer look at his current work with Ruby (the language)
and Ruby on Rails (the platform) to gain more clarity.

It’ll probably help to work my way through his guide,
["Shared Nothing Architecture"][shared-nothing-architecture], part of
[fly.io’s](https://fly.io) collection of [Guides (Blueprints)][fly-io-guides]
for building apps on their platform.

Also, I haven’t dug deeply into how it’s built, but this suggests one possible
aspect of how [OpenClaw] gained such rapid adoption. Decentralized and largely
unintentional, those bots exemplify a route-to-identity system.

[aws-cells]: https://docs.aws.amazon.com/wellarchitected/latest/reducing-scope-of-impact-with-cell-based-architecture/what-is-a-cell-based-architecture.html
[fly-io-guides]: https://fly.io/docs/blueprints/
[openclaw]: https://openclaw.ai
[routing-to-identity-post]: https://intertwingly.net/blog/2026/02/05/Routing-to-Identity.html
[shared-nothing-architecture]: https://fly.io/docs/blueprints/shared-nothing/
