Title: Xonsh, history, sqlite
Date: 2022-07-25
Author: C. Ross Jam
Status: published

[xonsh][1] has been growing on me as an interactive shell. One area I
haven’t delved into much is the [history capabilities][3]. I guess I
shouldn’t be too surprised that [sqlite makes an appearance][2]:

> Xonsh has a second built-in history backend powered by sqlite (other
> than the JSON version mentioned all above in this tutorial). It
> shares the same functionality as the JSON version in most ways,
> except it currently doesn’t support the history diff action and does
> not store the output of commands, as the json-backend
> does. E.g. __xonsh__.history[-1].out will always be None. 

> The Sqlite history backend can provide a speed advantage in loading
> history into a just-started xonsh session. The JSON history backend
> may need to read potentially thousands of json files and the sqlite
> backend only reads one. Note that this does not affect startup time,
> but the amount of time before all history is available for
> searching. 

Combine with the sqlite’s full text search capabilities for even more
entertainment.

[1]: https://xon.sh/
[2]: https://xon.sh/tutorial_hist.html#sqlite-history-backend
[3]: https://xon.sh/tutorial_hist.html
