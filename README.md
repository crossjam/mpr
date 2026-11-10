# Mass Programming Resistance

Source content, configuration, and code for creating [Mass Programming
Resistance](https://mpr.crossjam.net/)

```
uv sync
git remote add drafts git@github.com:crossjam/mpr.drafts.git
./install-draft-hooks.sh
uv run poe html
```

Drafts live on per-post `draft/*` branches in the private `drafts`
remote; see `DRAFTPOST.md` and `PUBLISHPOST.md`.

TODO

- [x] Investigate removing submodules
- [ ] figure out regex syntax warnings with Python 3.13
- [ ] Generation performance or caching improvements
- [ ] Integrate Poe the Poet task running to replace make


