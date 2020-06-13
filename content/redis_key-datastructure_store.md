Title: redis key-datastructure store
Date: 2009-11-13 22:57
Author: crossjam
Category: Uncategorized
Slug: redis_key-datastructure_store
Status: published

[<img src="http://crossjam.net/mpr/media/redis logo.png" alt="redis logo.png" border="0" width="74" height="55" align="right" style="margin: 10px;" />][1] Haven't been too heavy on the tech talk here, but a recent discovery bears notice. I've been doing some development with [redis][1], "a persistent key-value database...". If you're a programmer redis is like a persistent dictionary, similar to [Berkeley DB][2]. redis has a network server baked in. Since redis maintains all of its data completely in main memory it's blazingly fast but is limited by the amount of RAM on a machine.

The key feature of note though is that the values stored in the DB are not restricted to simple strings. Lists, sets, and ordered sets are also provided. A number of atomic operations are also available on instances of these objects. This makes redis very convenient for a number of multiprocessing tasks where the processes coordinate through redis values.

As far as I can tell, the concept of having a handful of higher level datatypes as values in a key-value store is relatively new, although I'm sure there's some obscure CS paper or tech report somewhere that covers the topic.

[1]: http://code.google.com/p/redis/

[2]: http://en.wikipedia.org/wiki/Berkeley_db

