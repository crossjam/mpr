Title: AWS S3 versus Cloudflare R2
Date: 2024-12-05
Author: crossjam
Status: published

A [comparison of object storage systems][1] on AWS and Cloudflare, by
Sylvain Kerkour. Let’s go straight to the punchline.

> Honestly, I see only a few reasons to use S3 today: if ~40ms of
> latency really matters, if you already have a mature AWS-only
> architecture and inter-region traffic fees are not making a dent in
> your profits, or if it's really hard to bring another vendor into
> your infrastructure for organizational reasons. That's all.

> Maybe 90%+ of projects and organizations will be better served by
> Cloudflare R2.

Trust but verify on that one. However, it’s nice that there are
multiple object storage options. In addition to R2, Backblaze runs
[B2][2], Akamai/Linode has its [own object storage][3], ditto Digital
Ocean [Spaces][4], Vultr [object storage][5], etc. 

I suspect that the offerings of the smaller players are best thought
of as internal S3 substitutes for building within those environments,
rather than globally facing S3 endpoints. YMMV.

[1]: https://kerkour.com/aws-s3-vs-cloudflare-r2-price-performance-user-experience?utm_source=changelog-news
[2]: https://www.backblaze.com/cloud-storage
[3]: https://www.linode.com/products/object-storage/
[4]: https://www.digitalocean.com/products/spaces
[5]: https://docs.vultr.com/vultr-object-storage

