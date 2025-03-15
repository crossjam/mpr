Title: LaunchBar Actions Editor
Date: 2024-12-24
Author: crossjam
Status: published

Did a little more thinking about LaunchBar Actions and drifted into
considering how they could combine with [Simon Willison’s `llm`][2]
framework. Simon mostly demonstrates `llm` as a powerful CLI tool for
interacting with modern AI models. The CLI is porcelain around
extremely sophisticated Python module plumbing. LaunchBar could make a
nice alternative porcelain.

So how does one go about creating LaunchBar Actions? The code examples
I’ve seen are pretty straightforward. I could likely reverse engineer
the directory structure and code interface even if documentation
didn’t exist. However, the fine folks at Objective Development added a
[LaunchBar Action Editor][1] in version 6.4 of the tool. Well what do
you know!? 😲

And of course there is [documentation for authoring actions][3].

[1]: https://www.obdev.at/products/launchbar/actions.html
[2]: https://llm.datasette.io/
[3]: https://developer.obdev.at/launchbar-developer-documentation/#/actions-overview
