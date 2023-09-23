Title: Some jq Stuff
Status: published
Date: 2023-09-17

[`jq`][1] is one of my favorite command line tools and there’s a bit of
news. There’s a [`jq` 1.7][2] finally:

> After a five year hiatus we're back with a GitHub organization, with
> new admins and new maintainers who have brought a great deal of
> energy to make a long-awaited and long-needed new release. We're
> very grateful for all the new owners, admins, and
> maintainers. Special thanks go to Owen Ou (@owenthereal) for pushing
> to set up a new GitHub organization for jq, Stephen Dolan
> (@stedolan) for transferring the jq repository to the new
> organization, @itchyny for doing a great deal of work to get the
> release done, Mattias Wadman (@wader) and Emanuele Torre
> (@emanuele6) for many PRs and code reviews. Many others also
> contributed PRs, issues, and code reviews as well, and you can find
> their contributions in the Git log and on the closed issues and PRs
> page.

Also, is there anything Postgres can’t do? Enter [pgJQ][3] as a supplement
to Postgres’ built-in `jsonb` support.

> The pgJQ extension embeds the standard jq compiler and brings the
> much loved jq lang to Postgres. 

> It adds a jqprog data type to express jq programs and a jq(jsonb,
> jqprog) function to execute them on jsonb objects. It works
> seamlessly with standard jsonb functions, operators, and jsonpath.

Very much feels like alpha software, but could still be a useful
addition to one’s toolbox.

[1]: https://jqlang.github.io/jq/
[2]: https://github.com/jqlang/jq/releases/tag/jq-1.7
[3]: https://github.com/Florents-Tselai/pgJQ

