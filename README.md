# Mass Programming Resistance

Source content, configuration, and code for creating [Mass Programming
Resistance](https://mpr.crossjam.net/)

```
uv sync
uv run post setup
uv run poe html
```

Drafts live on per-post `draft/*` branches in the private `drafts`
remote; see `docs/POST.md`.

Writing a post:

- `uv run post draft new --edit` from a clean `main` starts `draft/<slug>`
- Write, preview with `uv run poe devserver`, save with `uv run post draft save`
- `uv run post draft switch <slug>` resumes a draft, bringing in `main`'s changes
- `uv run post publish draft <slug> --push` publishes it
- `uv run poe rsync_upload` deploys the site

## License

Blog content is licensed under [CC BY-NC-SA
4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/), and the code
under the Apache License 2.0 (`LICENSE`); `LICENSE.md` says which is
which. Vendored third-party code keeps its own license; see
`THIRD_PARTY_NOTICES.md`.

TODO

- [x] Investigate removing submodules
- [x] figure out regex syntax warnings with Python 3.13
- [ ] Generation performance or caching improvements
- [x] Integrate Poe the Poet task running to replace make


