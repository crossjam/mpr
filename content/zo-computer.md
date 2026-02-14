---
title: zo.computer and exe.dev
date: 2026-02-13 21:15
author: C. Ross Jam
status: published
---

As a Systems Guy (TM), I see LLMs and agentic coding sparking yet
another renaissance in program isolation mechanisms. Two projects,
among many, that have caught my eye recently are zo.computer and
exe.dev.

### zo.computer

Link parkin’: [Zo]

> Zo is a new kind of computer. It's a personal server, where you can store your
> files, and connect your tools. And it's intelligent, so you can ask it to do
> research, create automations, and build apps on top of your personal context.
>
> - Explore – Craft your personal AI. It can browse the web, edit your files,
>   and connect to your apps. You can even text or email your Zo.
> - Automate – Write workflows in natural language for your AI to execute. Run
>   your workflows automatically.
> - Create – Use AI to make anything: documents, images, videos, websites... the
>   sky's the limit.
> - Host – Websites, APIs, even self-hosted services like n8n. You don't need to
>   be technical! Just ask Zo.

Ben Guo added [a bit more grandiose aspiration][personal-civilization]

> If you boil down what a tech company is, it's code, compute, collective
> intelligence, and agents that act. The future is about enabling individuals to
> work at the scale of a tech company.
>
> This is the original dream of personal computing, but on a much grander scale.
> It's the evolution from Personal Computing to Personal Civilization-Building.
>
> "AWS for your mom" is one of the ways we've described what we're building with
> Zo Computer. But this only scratches the surface of our vision
>
> ...
>
> Our mission is to build a general purpose computational mech suit for
> everyone. This requires designing enduring abstractions for compute and AI
> that are simple, last for decades, and enable the individual to harness powers
> that were previously only accessible to entire technical organizations.

Interestingly, Zo Computer comes across as a bit less hyped than [clawdbot],
having emerged in roughly the same time frame.

### exe.dev

In a Discord specifically for Simon Willison’s projects, one of the developers
for [exe.dev](https://exe.dev), Josh Bleecher Snyder, popped up a while ago
offering promotional credits. Should have taken Josh up on that.

What’s [exe]?

> exe.dev is a subscription service that gives you virtual machines, with
> persistent disks, quickly and without fuss. These machines are immediately
> accessible over HTTPS, with sensible and secure defaults. You can share your
> web server as easily as you can share a Google Doc. With built-in optional
> authentication, so you can focus on your thing.
>
> Your VMs share CPU/RAM—you pay for underlying resources, not per VM. Make a
> bunch!

### crawshaw.io

The [developers of exe.dev][exe-devs] include David Crawshaw, who’s gotten a bit
of attention posting about programming [with LLMs][programming-with-llms] and
[with-agents][programming-with-agents]. That includes some good thoughts in
[_"Eight more months of agents"_][eight-months-of-agents]

> ## Built-in agent sandboxes do not work
>
> The constant stream of "may I run cat foo.txt?" from Claude Code and "I tried
> but cannot go build in my very-sophisticated sandbox" from Codex is a
> nightmare. You have to turn off the sandbox, which means you have to provide
> your own sandbox. I have tried just about everything and I highly recommend:
> use a fresh VM.
>
> ## I have far more programs and services than I used to
>
> This is why I am building exe.dev. I need a VM, with an unconstrained agent,
> that I can trivially start up and type the one liner I would have otherwise
> put into an Apple Note named TODO and forgotten about. A good portion of the
> time Shelley turns a one-liner into a useful program.
>
> I am having more fun programming than I ever have, because so many more of the
> programs I wish I could find the time to write actually exist. I wish I could
> share this joy with the people who are fearful about the changes agents are
> bringing. The fear itself I understand, I have fear more broadly about what
> the end-game is for intelligence on tap in our society. But in the limited
> domain of writing computer programs these tools have brought so much
> exploration and joy to my work.

Now, where had I heard David Crawshaw's name before? Ah yes! Crawshaw
was intimately connected to Tailscale, and I [posted][tailscale-post]
my delight with his LAN manifesto.

[clawdbot]: https://en.wikipedia.org/wiki/OpenClaw
[eight-months-of-agents]: https://crawshaw.io/blog/eight-more-months-of-agents
[exe]: https://exe.dev/docs/what-is-exe
[exe-devs]: https://exe.dev/docs/who
[personal-civilization]: https://www.zo.computer/blog/from-personal-computer-to-personal-civilization
[programming-with-agents]: https://crawshaw.io/blog/programming-with-agents
[programming-with-llms]: https://crawshaw.io/blog/programming-with-llms
[tailscale-post]: {filename}/tailscale_manifesto.md
[zo]: https://www.zo.computer
