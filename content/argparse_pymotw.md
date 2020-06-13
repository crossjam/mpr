Title: argparse PyMOTW
Date: 2010-08-21 19:08
Author: crossjam
Category: Uncategorized
Slug: argparse_pymotw
Status: published

When I used to teach Python, I would always get on students to use Python's built-in [optparse][1] module when writing scripts. For whatever NIH reason, people wanted to do a half-ass job of groveling over `sys.argv` instead of using a module specifically designed to alleviate the pain.

Things on the command line parsing front have been advancing lately. To wit, the new [argparse module][2]:

> *The argparse module was added to Python 2.7 as a replacement for optparse. The implementation of argparse supports features that would not have been easy to add to optparse, and that would have required backwards-incompatible API changes, so a new module was brought into the library instead. optparse is still supported, but is not likely to receive new features.*

This makes a must read out of Doug Hellmann's Python Module of the Week (PyMOTW) [entry][2] for argparse to get a good basic understanding of the module.

[1]: http://www.doughellmann.com/PyMOTW/optparse/

[2]: http://www.doughellmann.com/PyMOTW/argparse/

