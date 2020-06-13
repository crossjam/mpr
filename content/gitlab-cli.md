Title: GitLab CLI
Date: 2020-05-28 23:12
Author: crossjam
Category: Uncategorized
Slug: gitlab-cli
Status: published

At the day job, we rely heavily on [GitLab][1] which is a beast of a platform, even in if you only consider all the features in the [FOSS version][2]. Looks like I’m going to have to automate some processes on top of GitLab and thankfully, there’s a [rich RESTful API][4].

Even better for me there’s a nice looking [Python client package for the api][4] that also provides a command line interface. Looks like the client library is pretty well maintained although [the CLI needs some love][5]. 

[1]: https://en.wikipedia.org/wiki/GitLab
[2]: https://gitlab.com/gitlab-org/gitlab-foss
[3]: https://python-gitlab.readthedocs.io/en/stable/cli.html#cli
[4]: https://docs.gitlab.com/ee/api/
[5]: https://github.com/python-gitlab/python-gitlab/issues/708