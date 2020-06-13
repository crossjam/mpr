Title: Python, argparse, append
Date: 2011-11-23 12:10
Author: crossjam
Category: Uncategorized
Slug: python-argparse-append
Status: published

<img src="http://crossjam.net/wp/mpr/wp-content/uploads/2011/08/python-logo.gif" alt="Python logo" border="0" width="211" height="71" align="right" style="margin: 10px;" /> This is a little Python conundrum that I had to solve at work. Hopefully it'll save someone else some time.

Python's [`argparse`][1] is the fabulous, back ported, standard, built-in Python 2.7 module for parsing command line arguments. Very helpful for building scripts that are a little too complex for `bash`. One thing you can do with `argparse` is specify that an argument is supposed to be an output (or input) file like so:

[sourcecode language="python"]
parser.add_argument('--log', type=argparse.FileType('w'), default='-')
[/sourcecode]

`argparse` has built-in knowledge of the UNIX convention that `-` represents standard input or output as appropriate. The above basically defaults to assigning `stdout` as the logging target unless a filename is supplied on the command line. Unfortunately, this always overwrites the target file, which is not quite what you want for log files. You really want to just append any new output, not wipe out the old stuff. 

But! The following, natural correction, doesn't quite work, with `argparse` throwing an error:

[sourcecode language="python"]
parser.add_argument('--log', type=argparse.FileType('a'), default='-')
[/sourcecode]

Turns out the `argparse.FileType` is hardwired to throw an exception for appending to the `-` pseudo-file.

However, there is a solution. You can supply a Python file object for the default, like so:

[sourcecode language="python"]
parser.add_argument('--log', type=argparse.FileType('a'), default=sys.stdout)
[/sourcecode]

Works great. Defaults correctly, but appends to existing files if specified. Happy hacking!

*Also, my first trial with WordPress' [programming language shortcodes][2]. So far so good.*
 
[1]: http://docs.python.org/dev/library/argparse.html
[2]: http://en.support.wordpress.com/code/posting-source-code/