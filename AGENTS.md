# AGENTS.md

> A concise brief for AI coding agents working on this repository.  
> This project is a **Python project** managed with **uv** and tested
> with **pytest**.
>
> This repo is content for the blog [Mass Programming
> Resistanct](https://mpr.crossjam.net). It uses the Pythan package
> [Pelican](https://getplican.com) to render Markdown and Jinja2
> templates into HTML.

---

## 🧭 Quick Start

You should never need to activate a virtualenv for this project
directly. Let uv handle it. Almost everything package or Python
related should start with ‘uv run‘ . There may be named tasks provided
by the ‘poe‘ package that simplify some things like running linting or
type checking.

```bash
# set up environment from pyproject + uv.lock
uv sync

# run the test suite (quiet, stop on first failure)
uv run pytest -q -x

# run type checks & lint (if dev deps are present)
uv run ruff check src tests
uv run ruff format src tests

# poe is Poe the Poet, a Python task runner
# poe integrates well with pyproject.toml

# list tasks
poe
```

<!-- BEGIN KATA (managed by `kata init --with-agents`) -->
Kata is the system of record for intent.

- Never `kata delete` or `kata purge` without explicit user authorization.

~~~dot
digraph kata {
  rankdir=TB; node [shape=box];

  arrive   [shape=diamond label="Work arrives"];
  search   [label="Search first; reuse an open issue\nor create one"];
  route    [shape=diamond label="Work it, or delegate it?"];

  subgraph cluster_work {
    label="Working a kata-tracked issue";
    claim  [label="On claim or start, mark it actively tracked:\nkata meta set <ref> work.attention ok\nIn-flight work becomes visible to coordinators\nand dashboards from the moment it is grabbed."];
    branch [label="If the work happens on a dedicated branch, stamp it once:\nkata meta set <ref> work.branch <branch>\nor bind at creation:\nkata create ... --meta work.branch=<branch> --idempotency-key <key>"];
    live   [label="Keep your live state truthful on the issue:\nkata meta set <ref> work.attention stuck|needs-human|ok\nwith a one-line kata meta set <ref> work.attention_msg \"<why>\"\nRaise stuck when you cannot proceed, needs-human when you want\ninput or review (you may keep working), and clear back to ok\nwhen unblocked."];
    claim -> branch -> live;
  }

  subgraph cluster_delegate {
    label="Delegating work as separate issues (fan-out/join)";
    fanout [label="Create each delegated child with\n--parent <epic-or-coordinating-issue>,\n--meta work.branch=..., and an idempotency key;\ncapture refs from --json (.issue.short_id).\nAdd dependency links only for actual prerequisites."];
    join   [label="Join with kata wait <refs> --until attention --any\nMatches needs-human or stuck; a close also completes the wait,\nand the reported reason distinguishes which. Use --timeout so a\nwrapper can tell timeout from satisfaction."];
    coord  [label="As coordinator you read work.* —\nyou never write it on issues you delegated."];
    fanout -> join -> coord;
  }

  done     [shape=diamond label="Verified complete?"];
  close    [label="kata close <ref> --done\nwith a message and evidence"];
  review   [label="kata label add <ref> needs-review\nplus a comment on what remains"];
  park     [shape=diamond label="Park it?"];
  schedule [label="kata schedule <ref> <date-or-time>\nsets scheduled_on; clear with -"];
  someday  [label="kata meta set <ref> someday true --json-value\nclear with kata meta unset <ref> someday"];

  arrive -> search -> route;
  route -> claim   [label="work it"];
  route -> fanout  [label="delegate it"];
  route -> park    [label="record only"];
  live  -> done;
  coord -> done;
  done -> close    [label="yes"];
  done -> park     [label="no, stopping"];
  park -> schedule [label="start date known"];
  park -> someday  [label="no date"];
  park -> review   [label="no"];

  always [shape=note label="Always: one writer per key. work.* on closed issues is meaningless —\nnever write it there, ignore it when reading. Never end a session with\nthe signal stale: before stopping, either close the issue or set the\nattention pair to reflect the hand-off."];

  relationships [shape=note label="Relationships: Parent links express containment and roll-up only;\nthey do not gate readiness, and a parent cannot close with open children.\nUse --blocks <dependent> / --blocked-by <prerequisite>\nonly for real prerequisites; those links gate kata ready.\nUse --related <ref> for context only.\nkata wait observes state; it does not require a dependency edge."];

  gate [shape=note label="A future scheduled_on or someday=true keeps an issue\nout of ready and next. kata deadline <ref> <date-or-time>\nsets deadline_on, which never gates either."];
}
~~~
<!-- END KATA -->
