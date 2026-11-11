# Writing and Publishing Posts: the `post` CLI

Each unpublished post lives on its own `draft/<slug>` branch. Draft
branches are pushed only to the `drafts` remote, the private
`crossjam/mpr.drafts` repository. `origin` is public, so `main` holds
published posts only.

`post` is installed into the project environment by `uv sync`; run it
with `uv run post`. Every command has `--help`. It works on the
repository through [dulwich](https://github.com/jelmer/dulwich), so it
does not shell out to `git`.

## The Common Path

```bash
uv run post draft new --edit              # start draft/<slug> from main
uv run post draft save -m "First pass"    # commit and push to drafts
uv run post publish draft <slug> --push   # squash onto main, push, clean up
uv run poe rsync_upload                   # deploy
```

## One-Time Setup per Clone

```bash
uv sync
uv run post setup
```

`post setup` adds the `drafts` remote if it is missing, fetches it, and
runs `install-draft-hooks.sh`, which adds two guards to the clone's git
hooks:

- **pre-push**: refuses to push any `draft/*` branch to a remote other
  than the drafts repository
- **post-commit**: ends the hook before anything else in it runs for
  commits on `draft/*` branches, so the automatic review (or anything
  else hooked there) never sees unpublished prose

The guards are inserted as marked blocks after the shebang, so hooks
installed by other tools keep running everywhere except that
post-commit case. `post draft new` re-runs the installer every time, in
case another tool has rewritten a hook since.

dulwich runs the commit hooks but not pre-push, so `post` enforces the
same rule itself: it never pushes a `draft/*` branch to a URL other than
the drafts repository's.

## Drafts: `post draft`

### `post draft new`

From a clean working tree:

```bash
uv run post draft new --edit                     # prompts for the title
uv run post draft new -t "My Post" --clipboard   # body from the macOS clipboard
uv run post draft new -t "My Post" -f notes.md   # body from a file
pbpaste | uv run post draft new -t "My Post" -f - --quote --yes
```

It refuses to start if the working tree has uncommitted changes, the
branch already exists locally or on `drafts`, or the slug matches a post
already published on `main`. Then it:

1. Creates and switches to `draft/<slug>`, starting from `main`
2. Writes `content/<slug>.md` with YAML front matter marked `status: draft`
3. Opens it in `$EDITOR`, with `--edit`
4. Commits it as `Start draft: <title>`
5. Pushes the branch to `drafts` and sets it as the upstream

If the push fails (offline, say), the commit stays local; `post draft
save` pushes it later.

Options:

- `-t, --title`: the post title; prompted for when omitted
- `-a, --author`: defaults to C. Ross Jam
- `-s, --slug`: defaults to the slugified title
- `-f, --file FILE`: read the body from a file, or `-` for stdin
- `-c, --clipboard`: take the body from the macOS clipboard; RTF is
  converted to Markdown with pandoc (`brew install pandoc`) when available
- `-q, --quote`: format the body as a Markdown blockquote
- `-e, --edit`: open the post in `$EDITOR` before the first commit
- `-y, --yes`: skip the confirmation

With no `--file` or `--clipboard`, the body is Lorem Ipsum placeholder
text. When the body comes from stdin, pass `--title` and `--yes`, so no
prompt tries to read from it.

### `post draft save`

On a draft branch, commits changes to tracked files plus any new files
under `content/` (default message `Update draft`, or `-m`), then pushes
the branch to `drafts`. It pushes even when there is nothing new to
commit, so it also retries a push that failed earlier.

### `post draft list` and `post draft switch`

`post draft list` fetches `drafts` (skip with `--no-fetch`) and lists
every draft, marking whether it is here, on `drafts`, or both, with `*`
on the current one.

`post draft switch <slug>` checks a draft out. A draft started on
another machine is fetched from `drafts` and set to track it.

Preview while writing with `uv run poe devserver`; drafts render at
`/drafts/<slug>.html` with a Draft badge, and do not appear on the front
page.

## Publishing: `post publish`

### `post publish draft`

From a clean working tree, on the draft branch or anywhere else (it
switches to `main` first):

```bash
uv run post publish draft <slug>            # or: draft/<slug>
uv run post publish draft <slug> --push     # then finish, as below
uv run post publish draft <slug> --redate   # date the post now, replacing its date
```

It squash-merges `draft/<slug>` into `main`, so the draft's revision
history never reaches the public repository. The merge is worked out in
memory first, so a conflict with `main` changes nothing. In each post
the merge adds or changes with `status: draft`, it sets
`status: published` and adds a date if the post has none (or always,
with `--redate`). Then it commits as `Publish <title>`.

Without `--push` it stops after the commit, so you can look before
anything leaves the machine.

### `post publish finish`

```bash
uv run post publish finish <slug>
```

Pushes `main` to `origin`, then deletes `draft/<slug>` on `drafts` and
locally. It refuses unless `main` already carries every post the draft
touches as `status: published`, so an unpublished draft is never
deleted.

Both metadata styles are handled throughout: YAML front matter
(`status: draft` between `---` fences) and Pelican's `Key: value` header
lines.

## Shell Completion

click generates completion scripts, and the commands that take a slug
complete draft names. Completion only applies when you type `post`
itself, not `uv run post`, so it needs `.venv/bin` on your `PATH`. For
bash:

```bash
eval "$(_POST_COMPLETE=bash_source .venv/bin/post)"
```

## Configuration

The branch and remote names are constants in `src/mpr/repo.py`:
`BASE_BRANCH` (`main`), `PUBLIC_REMOTE` (`origin`), `DRAFTS_REMOTE`
(`drafts`), and the drafts repository's URL.

## Code Checks

`uv run poe qa` runs every check on `src/` and `tests/`: ruff format
and lint, ty, bandit, and pytest. Each also has its own task: `format`,
`lint`, `typecheck`, `bandit`, and `test`.
