Title: Tab Colorization
Date: 2012-06-02 21:24
Author: crossjam
Category: Uncategorized
Slug: tab-colorization
Status: published

Many of my favorite tools support multiple tabs, including iTerm2. On Firefox, there’s a plug-in, Colorful Tabs, that automatically colorizes the tabs making for nice visual distinction. Not sure it’s that big a deal cognitively, but at least it’s pleasant.

[Mikko Ohtamaa](http://opensourcehacker.com) has put together some [Python code that implements tab colorization][1] on ANSI-escape compatible terminal applications such as iTerm2:
> OSX’s iTerm 2, and maybe some other terminal applications, support ANSI control sequence extensions which allow shell to set the color of the terminal tab.

> Below is a Python script which
>
> * Randomizes a color based on the server host name. The same hostname always results to the same color.
* The color is randomized in HSL color space, so that only the hue component varies and saturation and lightness are locked. This prevents the creation of ugly color combinations like black text on black tab background.

Very handy!

[1]: http://opensourcehacker.com/2012/05/22/automatically-colorize-terminal-tabs-based-on-the-server-you-are-logged-into/