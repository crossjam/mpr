---
title: "A humble-cli Tip"
date: 2025-12-31 22:15
author: "C. Ross Jam"
status: published
---

I decided to see if I could download all of my Humble Bundle content to a local
NAS. I’ve [mentioned][1] the [humble-cli tool][2] as working really well for
interacting with Humble Bundle purchases.

A recent version of humble-cli has a `bulk-download` subcommand, which isn’t
very well documented. It takes a CSV file with columns labeled `key` and `name`.
It’s easy to generate with the humble-cli itself. Assuming you’ve already
authed, here’s what the steps look like:

```bash
$ humble-cli list --field key --field name > bundles.csv
...
$ humble-cli bulk-download bundles.csv
...
```

That’s it and off go your humble downloads.

In the current directory, this will iterate over each bundle in the csv file.
For each bundle, it’ll create a folder named after each item in the bundle. Then
it’ll download the corresponding media into that folder. This results in a nice,
two-level archive of all the bundles in the csv.

Bonus: the download process attempts to be idempotent. If you run a
`bulk-download` again and the media files are already present, it won’t
re-download them.

I haven’t seen this anywhere on the web, so maybe it’ll get indexed and help
someone out in the future.

[1]: {filename}/humblebundle_cli.md
[2]: https://github.com/smbl64/humble-cli
