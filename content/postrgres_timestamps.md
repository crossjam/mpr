Title: PostgreSQL Timestamps
Date: 2022-06-29
Author: C. Ross Jam
Status: published

At the day job, I got sucked into trying to understand two PostgreSQL
data types, `timestamp` and `timestamptz`. Thought I knew what I was
doing, then read the [docs][2] and came away even more confused. Luckily,
the folks at Cybertec had a pretty recent blog post on just this topic
[_Time Zone Management in PostgreSQL_][1].

> Next to character encoding, time zones are among the least-loved
> topics in computing. In addition, PostgreSQL’s implementation of
> timestamp with time zone is somewhat surprising. So I thought it
> might be worth to write up an introduction to time zone management
> and recommendations for its practical use.

The punchline ...

> Even though it is easy to get confused with time zones, you can
> steer clear of most problems if you use timestamp with timezone
> everywhere, stick with IANA time zone names and make sure to set the
> TimeZone parameter to the time zone on the client side. Then
> PostgreSQL will do all the heavy lifting for you.

But really, read the whole thing. There’s a lot of nuance and the
proper handling of timezones in Postgres is definitely not obvious. I
may actually circle back and illustrate what dragged me into this
tarpit and how I currently understand things.


[1]: https://www.cybertec-postgresql.com/en/time-zone-management-in-postgresql/
[2]: https://www.postgresql.org/docs/current/datatype-datetime.html
