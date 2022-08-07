Title: TIL ffprobe
Date: 2022-07-03
Author: C. Ross Jam
Status: published

I’ve been working on automating metadata additions to my [Fabric
collection][4] using information from Discogs. I was poking around for cli
ways, especially via [`ffmpeg`](https://ffmpeg.org), to add the info to
a music file and chanced across [a really useful gist][1].

> A quick guide on how to read/write/modify ID3 metadata tags for
> audio / media files using ffmpeg.

At the bottom of the gist is a mention of [`ffprobe`][2]. Much more
appropriate for the task at hand, especially since it can generate
output in JSON

> ffprobe gathers information from multimedia streams and prints it in
> human- and machine-readable fashion. 

> ... ffprobe output is designed to be easily parsable by a textual
> filter, and consists of one or more sections of a form defined by
> the selected writer, which is specified by the print_format option.

Although to be fair, `ffprobe` doesn’t seem to be able to write metadata
to a file.

_Bonus! [ffprobe tips][3]_
 

[1]: https://gist.github.com/eyecatchup/0757b3d8b989fe433979db2ea7d95a01 
[2]: https://ffmpeg.org/ffprobe.html
[3]: https://trac.ffmpeg.org/wiki/FFprobeTips
[4]: {filename}/finishing_fabric.md

