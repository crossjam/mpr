Title: Big Data Lessons
Date: 2012-02-27 23:14
Author: crossjam
Category: Uncategorized
Slug: big-data-lessons
Status: published

As a self-proclaimed Mad Data Scientist (Apprentice 3rd Class), I've learned at least two lessons, maybe more. First, **you will wait**. When you get upwards of 32 Gb of data, it's almost impossible to just read through the data in a reasonable amount of time on commodity hardware. You've left the land of interactivity son, live with it.

As a result of that first lesson, one gets in the habit of **timing everything**. If it takes a while for a task to run, you want to know how long, just in case you have to run it again. You want to know how that runtime is growing with data growth. Better be at least linear, preferably sub-linear. And if not, well you've got a problem.

Of course, [Nathan Marz captures the issues][1] much better than me, backed by much more real-world experience. At the end of the day, it all comes down to creating data views that go as fast as possible.

[1]: http://www.slideshare.net/nathanmarz/the-secrets-of-building-realtime-big-data-systems