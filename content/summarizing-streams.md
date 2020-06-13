Title: Summarizing Streams
Date: 2012-10-18 18:31
Author: crossjam
Category: Uncategorized
Slug: summarizing-streams
Status: published

[embed]https://twitter.com/bigdata/statuses/258963194163380224[/embed]

From [*A Framework for Summarizing and Analyzing Twitter Feeds*][1] (PDF alert)
> *In this paper, we present a dynamic pattern driven approach to summarize data produced by Twitter feeds. We develop a novel approach to maintain an in-memory summary while retaining sufficient information to facilitate a range of user- specific and topic-specific temporal analytics. We empir- ically compare our approach with several state-of-the-art pattern summarization approaches along the axes of storage cost, query accuracy, query flexibility, and efficiency using real data from Twitter. We find that the proposed approach is not only scalable but also outperforms existing approaches by a large margin.*

My quick half-ass summary:

1. use frequent item set mining, to come up with a code book
2. recode your content with the code book
3. compress, which exploits the redundancy uncovered by the coding
4. profit!!

But I need to read the paper more closely. And the real-time summarization and topic tracking aspects seem really cool.

[1]: http://www.cse.ohio-state.edu/~yangxin/Xintian_Yangs_website/Welcome_to_Xintian_Yangs_Homepage_files/kdd12.pdf