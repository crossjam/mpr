Title: Collaboration Invitations
Date: 2022-06-08
Status: published
Author: C. Ross Jam

So I’ve been struggling for the longest time with my personal [dotfiles][2]
repository trying to share it between personal and work
activities. Two separate branches seemed to eliminate some of the
difficulties, but SSH access was quite frustrating. It was
challenging dealing with multiple public keys, across multiple
machines, one of which typically was used infrequently. Suffice it to
say I banged my head against a lot of SSH and git config file walls.

Then I just gave up and decided to push the work branch to a work
GitHub account and deal with cross pollination via merges over
HTTP. Part of the problem was attempting to keep the personal repo
private for no good reason. I really thought at some point I’d be
adding public keys into the repository just to make life easier and
became totally paranoid. YAGNI.

The final piece of the puzzle was sending [collaboration
invitations][1] between the two accounts, thereby providing push
access to both repos with one SSH key for each persona. 🤦 C’mon man!

Now it’s fairly straightforward to share changes between the two
configurations. I’d dare say I could even go back to making the
personal repo private, but what’s the point.


[1]: https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository
[2]: https://github.com/crossjam/dotfiles
