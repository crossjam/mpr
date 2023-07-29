Title: Pelican: Draft View vs Published View
Author: C. Ross Jam
Date: 2023-01-03
Status: published

One thing that’s been annoying me recently with the static site
publishing tool that I use, [pelican](https://getpelican.com), is how
it treats draft posts and publishing. Out of the box, I haven’t been
able to easily generate one development site that includes all draft
(and unlabeled status) posts and another "officially" published site
that omits draft posts. The development site being handled by
pelican’s built-in HTTP server will provide a drafts folder, but I
find it’s usage clunky.

However, there may be a workaround using pelican’s default `Makefile`
and some smart configuration:

* Have the `devserver` and `devserver-global` targets in the
  `Makefile` generate output into a distinct dev output dir, where
  dev content winds up getting served from
* Modify the `pelicanconf.py` config files `DEFAULT_METADATA` to set
  `status` to `publish`
* Leave the `publishconf.py` as is, or make sure the default status is
  `draft`
* Maybe put all draft posts in a `draftposts` subdir so they get
  tagged in the dev server and are easier to find. 

That should cleanly isolate the dev content from the published
content, yet put all the draft material in one place during dev. It
should at the same time prevent accidental publishing of draft material to the
production site. I’m going to try an experiment using this approach
for a few days and report back.

P. S. Combined with TailScale, mobile life and authoring on the go
should become quite palatable. Hmmm 🤔, how well does self-hosted
filesharing tech like NFS and SMB work over TailScale? Given my
personal toolkit, worst comes to worst, I could also employ [Emacs
TRAMP][1] over SSH.

Oh wait. Is it even possible to get Emacs on an iPad? There's gotta be
a way right! [Apparently][3] [not.][2]

[1]: https://www.gnu.org/software/tramp/
[2]: https://news.ycombinator.com/item?id=33716799
[3]: https://andschwa.com/posts/emacs-on-an-ipad/
