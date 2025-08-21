Title: ffmpeg, homebrew, and aac
Date: 2025-08-17
Author: C. Ross Jam
Status: published

Link parkin’ this Stack Overflow [solution][1] for personal reference:

> Homebrew v2.0 dropped all of the extra options that are not
> explicitly enabled in each formulae. So the --with options no longer
> work if you use the core Homebrew formulae. 

> Instead you can use a third-party repository (or "tap") such as
> ​homebrew-ffmpeg. This tap was created in response to the removal of
> the options from the core formulae. 

```bash
$ brew tap homebrew-ffmpeg/ffmpeg
$ brew install homebrew-ffmpeg/ffmpeg/ffmpeg --with-fdk-aac
# or
$ brew install homebrew-ffmpeg/ffmpeg/ffmpeg --with-fdk-aac --HEAD
```

I have a script that uses `ffmpeg` to convert `WAV` files to `m4a`
files for Apple Music. It needs [the non-free Fraunhofer FDK AAC][2]
to properly encode the data and write out in the correct file
format. It’s not often I use the script though and a skoosh of bitrot had
settled in to my installation with `homebrew`. This solution fixed
things up in a pinch.

[1]: https://stackoverflow.com/questions/55092608/enabling-libfdk-aac-in-ffmpeg-installed-with-homebrew
[2]: https://trac.ffmpeg.org/wiki/Encode/AAC
