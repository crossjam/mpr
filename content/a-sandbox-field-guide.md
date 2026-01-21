---
title: A Sandbox Field Guide
date: 2026-01-20 21:30
author: C. Ross Jam
status: published
---

An excellent [deep dive][field-guide] into sandboxes for AI agents by Luis
Cardoso.

> In the rest of this post, I’ll give you a simple mental model for evaluating
> sandboxes, then walk through the boundaries that show up in real AI execution
> systems: containers, gVisor, microVMs, and runtime sandboxes.

Cardoso goes into detail on multiple approaches (with figures!) and then clearly
lays out the tradeoffs. The focus is on containers or container-alikes (e.g.,
microVMs). Also, it's server and cloud oriented, rather than about code your
coding agent is running locally on your laptop. There is good additional
material on that topic, though.

I also enjoyed his "three-question model" of 1) boundary, 2) policy, and 3)
lifecycle for evaluating sandboxes.

This includes a well-organized and clearly presented discussion of the
underlying Linux kernel mechanisms that enable isolation. And their
fundamental limitations.

> A lot of “agent sandbox” failures aren’t kernel escapes. They’re policy
> failures.
>
> If your sandbox can read the repo and has outbound network access, the agent
> can leak the repo. If it can read ~/.aws or mount host volumes, it can leak
> credentials. If it can reach internal services, it can become a
> lateral-movement tool.
>
> This is why sandbox design for agents is often more about explicit capability
> design than about “strongest boundary available.” Boundary matters, but policy
> is how you control the blast radius when the model does something dumb or
> malicious prompts steer it.

Again, good times in Systems Land.

[field-guide]: https://www.luiscardoso.dev/blog/sandboxes-for-ai
