Title: Conda Envs
Date: 2015-11-25 15:10
Author: crossjam
Category: Uncategorized
Slug: conda-envs
Status: published

I don’t find Python’s `virtualenvs` to be as cumbersome as Tim Hopper, especially when combined with [`virtualenvwrapper`][2], but his [argument for using Anaconda environments][1] is compelling:

> In 2015, I have almost exclusively used Python installations provided through Continuum Analytics's Conda/Anaconda platform. I have also switched from using virtualenvs to using conda environments, and I am loving it.

The only contra is that `pip` and `virtualenv` are so widely distributed and easily deployed with distro packages that they’re somewhat safe to rely on. Conda, not so much, even though it’s a light lift and spreading. 

Interestingly, I probably overlapped with some of Tim’s [Qadium][3] colleagues on a DARPA program.

[1]: http://stiglerdiet.com/blog/2015/Nov/24/my-python-environment-workflow-with-conda/#fn:python-version
[2]: https://virtualenvwrapper.readthedocs.org/en/latest/
[3]: https://qadium.com