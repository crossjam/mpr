Title: Petrel
Date: 2013-04-05 19:09
Author: crossjam
Category: Uncategorized
Slug: petrel
Status: published

At work, I’m being overtaken by the [Storm][2]. But I’ll be damned if I get sucked back into Java programming without some kicking and screaming. I’ll definitely be giving [Petrel][1] a whirl
> Tools for writing, submitting, debugging, and monitoring Storm topologies in pure Python.

> ...

> Petrel offers some important improvements over the storm.py module provided with Storm:

> * Topologies are implemented in 100% Python
> * Petrel's packaging support automatically sets up a Python virtual environment for your topology and makes it easy to install additional Python packages.
> * "petrel.mock" allows testing of single components or single chains of related components.
> * Petrel automatically sets up logging for every spout or bolt and logs a stack trace on unhandled errors.

And just in case you’re looking for an alternative to Storm, don’t forget [Yahoo!’s, now Apache’s, S4][3]. While not as fashionable, [S4 is definitely comparable][4].

[1]: https://github.com/AirSage/Petrel
[2]: http://storm-project.net/
[3]: http://incubator.apache.org/s4/
[4]: http://gdfm.me/2013/01/02/distributed-stream-processing-showdown-s4-vs-storm/