Title: The marimo moment
Date: 2025-08-28
Author: C. Ross Jam
Status: published

In my previous full time gig, I did a bit of work implementing a
set of APIs using [FastAPI][3] and deploying them into AWS. I needed
to get a picture of API usage from external partners and AWS didn’t
have anything to easily use straight out of the box. So I set about
doing some dashboard development and initially thought about using
Jupyter but decided to take a sidequest into [marimo][2] which had
been popping up quite a bit on my podcast radar. Worked like a charm.

Also as part of my job, I built a little NLP model training platform
on top of [Coiled][1] running in AWS. Highly recommend Coiled if you
need to scale compute on AWS but have [minimal in-house cloud and ops
expertise and staffing][5]. Especially [coiled batch][4], which let us
effectively use AWS GPU nodes. We were running super lean and didn’t
have time to really drill down on all that AWS had to offer.

And now Coiled has illustrated [running marimo notebooks on
coiled][6].

My spider sense tells me marimo is having a moment and building
towards escape velocity. It won’t dislodge [Jupyter][9] so much as provide
a complement in the notebook ecosystem, similar to how [polars][7]
complements [pandas][8] in the dataframe ecosystem.

Here’s some data points about marimo being on my radar. These are all
from podcasts I subscribe to and where I consume episodes regularly:

- PythonBytes [July 23, 2024][10]
- The Real Python Podcast, [November 29, 2024][12]
- PythonBytes [March 24, 2025][11]
- Talk Python Podcast [April 14, 2025][16]
- The Real Python Podcast, [Jun 13, 2025][13]
- The Data Engineering Podcast, [July 28, 2025][14]
- The Data Exchange Podcast, [August 7, 2025][15]

A [Listen Notes search][17] would seem to confirm my intuition that
marimo is making a push to increase visibility, possibly due to a
round of venture funding at the end of last year. Podcasts aren’t
the only place marimo has been popping up. The founder, Akshay
Agrawal, did a PyCon US 2025 [talk][18] which is [available on
YouTube][19], and the tech features prominently in the TalkPython
course, ["LLM Building Blocks in Python"][20]. 

I’ve found Agrawal to be pretty engaging and thoughtful in all of
these conversations. He seems to be coming from a pragmatic place of
hard won experience. It’s giving me confidence that this project might
have legs.

My limited experimentation with marimo has shown promising shoots
although it’s a fast moving target. I really like the reactive
execution design choice and the underlying usage of plain Python as
the notebook storage format. They’re integrating agentic AI features,
of course, but there’s interesting possibilities for agentic
co-development of an interactive computational artifact along with the
user. Probably worthy of doing some digging into the CS research
literature for comps.

Here’s to marimo finding traction and enduring.

[1]: https://coiled.io/
[2]: https://marimo.io
[3]: https://fastapi.tiangolo.com
[4]: https://docs.coiled.io/user_guide/batch.html
[5]: https://docs.coiled.io/blog/is-aws-batch-right-for-data-professionals.html
[6]: https://docs.coiled.io/blog/marimo-on-coiled.html
[7]: https://pola.rs
[8]: https://pandas.pydata.org
[9]: https://jupyter.org/
[10]: https://pythonbytes.fm/episodes/show/393/dare-enter-the-bash-dungeon
[11]: https://pythonbytes.fm/episodes/show/425/if-you-were-a-klingon-programmer
[12]: https://realpython.com/podcasts/rpp/230/
[13]: https://realpython.com/podcasts/rpp/253/
[14]: https://www.dataengineeringpodcast.com/episodepage/revolutionizing-python-notebooks-with-marimo
[15]: https://thedataexchange.media/marimo/
[16]: https://talkpython.fm/episodes/show/501/marimo-reactive-notebooks-for-python
[17]: https://lnns.co/doHKf4k9Fep
[18]: https://us.pycon.org/2025/schedule/presentation/18/
[19]: https://youtu.be/3-3zy5W2SOw?si=PN76n6ZObHoxs3ox
[20]: https://training.talkpython.fm/courses/details/llm-building-blocks-for-python
