Date: 2025-06-01
Author: C. Ross Jam
Title: humble-cli, My Savior!
Status: published

I have an unfortunate addiction to [Humble Bundle][1] book
bundles. It’s a convenient way to get a lot of tech ebook content at a
reasonable price. Also, I can get graphic novels and an occasional
speculative fiction package of interest, usually in DRM free formats
and not through a global monopolist. 

That said, for all the time I’ve been buying from Humble Bundle, I’ve
only had the web interface to download my purchases. For bulk
downloads the UX wasn’t great so I turned to the [Humble Bundle
Downloader][2] extension for Firefox. Did the trick for quite a bit,
but age and rot seem to be setting in. Plus the extension was the only
reason to launch Firefox. But the downloader did have the nice feature
that it would rename files to match titles listed on the download
page, making the results much more human friendly.

Difficulties downloading a recent bundle put me on tilt and I cast
about for a better approach.

Enter [`humble-cli`][3], "The missing CLI for downloading your Humble
Bundle purchases". `humble-cli` is, you guessed it, a command line
interface tool for interacting with your Humble Bundle purchases. It
is sweet. Here’s a quick sample of how it lists purchases

```
crossjam@burningchrome:~$  ~/.cargo/bin/humble-cli list
...
a7nAf3UH3Vru8d3n | Humble Tech Book Bundle: Computer Science the Fun Way by No Starch                                   |    1.42 GiB | -
Ay3VN5rcSKrmt3d4 | Humble Tech Book Bundle: Data Engineering and Management by Pragmatic                                |  462.04 MiB | -
sRs4EtvxGf4hhDhb | Humble Tech Book Bundle: DevOps 2025 by O'Reilly                                                     |  348.66 MiB | -
bXPKrycBCSqbkhE7 | Humble Comics Bundle: Warren Ellis by Image Comics                                                   |    8.44 GiB | -
tDH8P68hkVWFnvNU | Humble Tech Book Bundle: Machine Learning, AI, and Bots by O'Reilly 2025                             |    1.07 GiB | -
nT68upU5Kuhwxp2Y | Brian Michael Bendis' Jinxworld Bundle                                                               |   16.96 GiB | -
crossjam@burningchrome:~$
```

The tool is a Rust binary that can be easily installed via `cargo
install`. There’s a minor bit of finagling around in browser cookie
storage to go through an auth sequence which could be smoothed out,
but I’m not really complaining. Quite performant for downloading too
while having a similar file naming approach as the Firefox
extension. 

So far, so good. I’m looking forward to putting `humble-cli` through
further paces and reorganizing my collection.

[1]: https://www.humblebundle.com/
[2]: https://addons.mozilla.org/en-US/firefox/addon/humble-bundle-downloader/
[3]: https://github.com/smbl64/humble-cli
