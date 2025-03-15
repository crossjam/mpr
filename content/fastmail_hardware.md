Title: Fastmail Hardware
Author: crossjam
Date: 2024-12-23
Status: published

Rob Mueller CTO, [blogged a piece][1] that caught my eye about how
[Fastmail](https://www.fastmail.com), a long standing hosted email
service, builds on their own hardware as opposed to public cloud
infrastucture. Part of the reason is that Fastmail predates the
availability of the major public cloud providers. Even at that they’ve
never seen a reason to move despite the persistent cloud evangelism
that has swept the tech industry.

A big part is the storage pricing of the blob services, S3 and its
competitive spinoffs. This interests me because I have a pile of
Discogs data that I’ve been hoarding. Pushing it all into the cloud
feels appealing but I don’t want to break the bank.

Mueller breaks down the surprising costs of storage at Fastmail
scale. Here’s the money graf on the choice:

> It’s interesting seeing the spread of prices here. Some also have a
> bunch of weird edge cases as well. e.g. “The S3 Glacier Flexible
> Retrieval and S3 Glacier Deep Archive storage classes require an
> additional 32 KB of data per object”. Given the large retrieval time
> and extra overhead per-object, you’d probably want to store small
> incremental backups in regular S3, then when you’ve gathered enough,
> build a biggish object to push down to Glacier. This adds
> implementation complexity.

Ultimately though, if you know your use case intimately, have a decent
handle on the cost envelope, and can employ enough operational expertise,
doing it yourself is an advantage.

Bonus, TIL about [Wasabi][2].

[1]: https://www.fastmail.com/blog/why-we-use-our-own-hardware/
[2]: https://wasabi.com/
