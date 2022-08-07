Title: HealthKit Data Hacking
Date: 2022-07-02
Author: C. Ross Jam
Status: published

Don’t know why, but I was reminded that Simon Willison had a neat
utility to process data exported from Apple HealthKit data,
specifically from an Apple Watch, [`healthkit-to-sqlite`][1]

> Convert an Apple Healthkit export zip to a SQLite database

Includes export instructions from your watch. Worked surprisingly
well.

The neat part is that you can then use [Datasette][3] and the Datasette
[cluster map plugin][2] to visualize outdoor workouts on a map. And of
course there’s always good old, exploratory data analysis using sqlite
and Pandas.

[1]: https://datasette.io/tools/healthkit-to-sqlite
[2]: https://datasette.io/plugins/datasette-cluster-map
[3]: https://datasette.io/
