Title: TIL pip requirements
Date: 2011-08-14 19:11
Author: crossjam
Category: Uncategorized
Slug: til-pip-requirements
Status: published
Attachments: wp/mpr/wp-content/uploads/2011/08/python-logo.gif

<img src="http://crossjam.net/wp/mpr/wp-content/uploads/2011/08/python-logo.gif" alt="Python logo" border="0" width="211" height="71" align="right" style="margin: 10px;" /> *Today I Learned* about [pip requirement files][2]. [pip][1] is a package installation tool for Python. It's great when you combine it with [virtualenv][3], so that you can easily build up complex Python installations with clean isolation from your base installation.

The kicker is `pip freeze > req_file.txt` and `pip -r req_file.txt` which will stash your installed packages and load them into a new environment. Makes it easy to kit out a new virtual environment with your favorite 3rd party modules. You only have to figure out the complete list of stuff you want once and then install it with one command line. And of course you can keep around variations of `req_file.txt` for different install types.

*Bonus: You can use [virtualenvwrapper][4] post install hooks to automatically run pip on a newly created virtual environment. You are using virtualenvwrapper aren't you?*

[1]: http://www.pip-installer.org/
[2]: http://www.pip-installer.org/en/latest/requirement-format.html
[3]: http://www.virtualenv.org/en/latest/index.html
[4]: http://www.doughellmann.com/docs/virtualenvwrapper/