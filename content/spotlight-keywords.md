Title: Spotlight Keywords
Date: 2012-01-30 19:46
Author: crossjam
Category: Uncategorized
Slug: spotlight-keywords
Status: published

At work, I moved to a brand spanking new Macbook Pro. Yeehaw! But in the migration of my old data, Spotlight search over my Thunderbird e-mails no longer worked. This was a big hindrance as I archive e-mail by stashing it in Thunderbird local folders. Thunderbird search is getting better, but I've got LaunchBar muscle memory for shooting off Spotlight searches. In effect, I underwent partial institutional memory loss.

After an epic hunt across the Interwebs, I finally managed to [find a solution to enable Thunderbird Spotlight indexing][2] thanks to [GetSatisfaction](http://getsatisfaction.com). Suffice it to say it involves gnarly file permission tweaking.

Then I got to thinking, wouldn't it be great to limit Spotlight searches to just e-mail? Gotta be a way to do that right? Turns out Spotlight supports a number of [keywords to match various file types][1]. `kind:email` gets both Thunderbird and Outlook messages. Handy!

[1]: http://docs.info.apple.com/article.html?path=Mac/10.7/en/mh26784.html
[2]: http://getsatisfaction.com/mozilla_messaging/topics/osx_10_7_2_lion_thunderbird_mails_dont_show_up_in_spotlight_search