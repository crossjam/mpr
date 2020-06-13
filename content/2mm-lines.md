Title: 2MM Lines
Date: 2011-10-28 20:52
Author: crossjam
Category: Uncategorized
Slug: 2mm-lines
Status: published

On the [tweet collection][1] front, the file in which I'm stashing my real-time notifications from Twitter has reached over 2 million lines. The requested notification format is length delimited, a line with the tweet length followed by the tweet text. So by my best estimation, I probably have over 1 million tweets harvested.

I actually need to do some validation processing, but I think I'm pretty close to declaring victory on this front. Once again, I'm impressed at how little handholding was necessary. My only worry is that it looks like my script restarted its `curl` process a couple of more times *(yeah)*, but I know I didn't add any code to cleanly mark those restart points *(boo)*. So there may be some lurking data corruption.

I'll let it run overnight just to provide a little safety margin, then get to some data crunching. A 2.5 Gb file is a heaping plate. 100 10K tweet files sounds like a job for [Elastic Map Reduce][2]!

[1]: http://crossjam.net/wp/mpr/2011/10/250k-tweets/
[2]: http://aws.amazon.com/elasticmapreduce/