Title: Python Data Visualization
Date: 2013-03-29 15:57
Author: crossjam
Category: Uncategorized
Slug: python-data-visualization
Status: published

Interesting post-PyCon take on [the state of matplotlib and Python and visualization][1] from one Jake Vanderplas, a core [matplotlib][2] developer:
> And where does that leave matplotlib? I would not, by any means, discount it just yet. Still, as John Hunter noted last summer, it faces some significant challenges, particularly in the area of client-rendered, dynamic visualizations. Any core matplotlib developers reading this should go back and re-watch John’s SciPy keynote: it was his last public outline of his vision for the project he started and led over the course of a decade. An IPython notebook-compatible client-side matplotlib viewer along the lines of the ideas John mentioned at the end of his talk would be the killer app that would, in all likelihood, allow matlotlib to maintain its position as the de facto standard visualization package for the Scientific Python community.

> And all that being said, regardless of what the future brings, you can be assured that in the meantime I and many others will still be doing all our daily work and research using matplotlib. Despite its weaknesses and the challenges it faces, matplotlib is a powerful tool, and I don’t anticipate it withering away any time soon.

Of special interest to me was the callout to [NodeBox OpenGL][3], harkening back to my old [generative art in Python noodling][6] days. [NodeBox 1][7] wasn’t a bad analog to [processing][4], but it looks like NodeBox OpenGL might be a major advance beyond [pyprocessing][5], which seems to have stalled out as a project.

Still the stickler was the bit level manipulations that processing did well and I haven’t seen done quite right in any of the Python based parallels.


[1]: http://jakevdp.github.com/blog/2013/03/23/matplotlib-and-the-future-of-visualization-in-python
[2]: http://matplotlib.org/
[3]: http://www.cityinabottle.org/nodebox/
[4]: http://processing.org/
[5]: http://code.google.com/p/pyprocessing/
[6]: http://crossjam.net/wp/mpr/2010/05/that_100_hours_project/
[7]: http://nodebox.net/code/index.php/Home