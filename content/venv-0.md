Title: venv-0
Date: 2013-04-20 16:09
Author: crossjam
Category: Uncategorized
Slug: venv-0
Status: published

Apparently, I’ve been [bootstrapping virtualenv][1] incorrectly. Eli Bendersky does it quite elegantly:
> I had to install some packages (Sphinx and related tools) on a new machine into a virtualenv. But the machine only had a basic Python installation, without setuptools or distribute, and without virtualenv. These aren’t hard to install, but I wondered if there’s an easy way to avoid installing anything. Turns out there is.

The idea is to create a "bootstrap" virtual environment that would have all the required tools to create additional virtual environments. It turns out to be quite easy with the following script (inspired by the answer in this SO discussion):

My shtick was to install setuptools, pip, then virtualenv. Bendersky gets them all in one clean shot.

[1]: http://eli.thegreenplace.net/2013/04/20/bootstrapping-virtualenv/