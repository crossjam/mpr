Title: 812 Discogs Data Files
Date: 2023-07-02
Status: published

[Previously][1] back in December, I noted a script that I had written
to count the number of data files pointed to at
[data.discogs.com](https://data.discogs.com). Back then it was 712.

I dusted off the old script just to see if still runs. Sure enough it
works. The latest total is 812 files, which feels right. 6 months
later at 5 files per month means a total of 30 additional.

Impressed that the script still works. Also, I should note that the
todos from the [total size calculation][2] have been completed, so
it’s a one liner to create an `sqlite` db of file info. Now I need to
turn it all into a Python package so I can use `pipx` to install it.

Or maybe I should keep it simple and just copy it into my personal
`~/.local/bin` directory 🤔.

[1]: {filename}/782_discogs_data_files.md
[2]: {filename}/discogs_data_total_size.md


