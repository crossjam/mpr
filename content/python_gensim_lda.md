Title: Python, Gensim, LDA
Date: 2010-09-22 22:24
Author: crossjam
Category: Uncategorized
Slug: python_gensim_lda
Status: published

Link parkin': [Gensim][1] is a Python framework for vector space modeling. This means taking a corpus of text documents, where document means any bag of symbols from a fixed vocabulary, turning the documents into a vector representation and then discovering latent structure within the corpus. Good for unsupervised document analysis.

I've been wondering for a long time about the specific implementation of a vector space model algorithm known as [Latent Dirichlet Allocation][2] or LDA. The only LDA implementations I've seen previously are in C++ and Java and I can't seem to grok how they translate the LDA math into code. Maybe the Python version in Gensim will be a bit more illuminating.

[1]: http://nlp.fi.muni.cz/projekty/gensim/

[2]: http://en.wikipedia.org/wiki/Latent_Dirichlet_Allocation

