Title: Kids Don’t Do This
Date: 2012-09-06 17:10
Author: crossjam
Category: Uncategorized
Slug: kids-dont-do-this
Status: published

A lot of my data hacking involves mugging over multiples of biggish files stashed in a standard UNIX filesystem. On any UNIXen worth its salt, the `find` and `xargs` utilities are your friends here. Use ’em.

But don’t make the same mistake that’s been biting me in the rear recently, embedding invocations of these tools **within** my programs. So tempting, especially in languages like Python that make shell invocation so easy, even though Python has the nice `os.walk` module. Works great until you move to another system and one or the other of `find` or `xargs` doesn’t work the way you assumed. Now you have to extract the calls and use the language’s built in filesystem walking capabilities or provide a command line option to specify the specific tool binaries if you build local custom versions.

Instead devise your program to read filenames from its command line args. Bonus points if you have an option to read from  stdin. Then wrap `find` and `xargs` **around** your program. And if in a specific situation your args to either utility get too hairy, stuff the invocation into a shell script.

You’ll thank me in the long run.