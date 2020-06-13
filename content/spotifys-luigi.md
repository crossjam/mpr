Title: Spotify’s Luigi
Date: 2013-03-23 19:38
Author: crossjam
Category: Uncategorized
Slug: spotifys-luigi
Status: published

Been looking around for a flexibly engineered batch scheduling tool that’s Hadoop friendly. [Spotify open sourced its Luigi framework][1] which looks like it might fit the bill:
> Luigi is a Python package that helps you build complex pipelines of batch jobs. It handles dependency resolution, workflow management, visualization, handling failures, command line integration, and much more.

> The purpose of Luigi is to address all the plumbing typically associated with long-running batch processes. You want to chain many tasks, automate them, and failures will happen. These tasks can be anything, but typically long running things like Hadoop jobs, dumping data to/from databases, running machine learning algorithms, or anything else.

There’s also an attendant post on [other uses of Python at Spotify][2].

[1]: http://github.com/spotify/luigi
[2]: http://labs.spotify.com/2013/03/20/how-we-use-python-at-spotify/