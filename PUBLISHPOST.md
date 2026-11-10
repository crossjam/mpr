# Publishing Drafts: publishpost.py

## How Drafts Work

Each unpublished post lives on its own `draft/<slug>` branch, started by
`draftpost.py`. Draft branches are pushed only to the `drafts` remote,
the private `crossjam/mpr.drafts` repository. `origin` is public, so
`main` holds published posts only.

A draft file carries `status: draft` in its metadata. The dev server
renders it at `/drafts/<slug>.html` with a Draft badge. A production
build of `main` contains no drafts at all.

## One-Time Setup per Clone

```bash
git remote add drafts git@github.com:crossjam/mpr.drafts.git
git fetch drafts
./install-draft-hooks.sh
```

`install-draft-hooks.sh` adds two guards to the clone's git hooks:

- **pre-push**: refuses to push any `draft/*` branch to a remote other
  than the drafts repository
- **post-commit**: ends the hook before anything else in it runs for
  commits on `draft/*` branches, so the automatic review (or anything
  else hooked there) never sees unpublished prose

The guards are inserted as marked blocks after the shebang, so hooks
installed by other tools stay in place and run as before everywhere
except that post-commit case. `draftpost.py` re-runs the
installer every time, in case another tool has rewritten a hook since.

To work on an existing draft from another machine:

```bash
git switch draft/<slug>      # tracks drafts/draft/<slug>
```

## Publishing

From a clean `main`:

```bash
./publishpost.py <slug>              # or: ./publishpost.py draft/<slug>
./publishpost.py <slug> --push       # also push and delete the draft branch
./publishpost.py <slug> --redate     # date the post now, replacing its date
```

The script:

1. Checks that `main` is checked out and clean, and that the branch exists
2. Squash-merges `draft/<slug>` into `main`, so the draft's revision
   history never reaches the public repository
3. In each post the merge adds or changes with `status: draft`, sets
   `status: published`, and adds a date if the post has none (or always,
   with `--redate`)
4. Commits as `Publish <title>`

Without `--push` it stops there and prints the remaining steps:

```bash
git push origin main
git push drafts --delete draft/<slug>
git branch -D draft/<slug>
uv run poe rsync_upload
```

To undo before pushing: `git reset --hard HEAD~1`. The draft branch is
untouched until you delete it.

Both metadata styles are handled: YAML front matter (`status: draft`
between `---` fences) and Pelican's `Key: value` header lines.

## Configuration

Constants at the top of `publishpost.py`:

- **`BASE_BRANCH`**: branch posts are published onto (`main`)
- **`PUBLIC_REMOTE`**: remote `main` is pushed to (`origin`)
- **`DRAFTS_REMOTE`**: remote draft branches live on (`drafts`)

## See Also

- `DRAFTPOST.md` - Starting a draft branch
- `install-draft-hooks.sh` - The hook guards
