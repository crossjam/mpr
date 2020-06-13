Title: Pattern Matching in Programs
Date: 2010-04-26 21:39
Author: crossjam
Category: Uncategorized
Slug: pattern_matching_in_programs
Status: published

Running across [Matchure][2] gave me good vibes regarding the utility of pattern matching in higher order programming languages. Pattern matching is still an undervalued mechanism in modern programming. A kissing cousin of [Lisp macros][3], [pattern matching][1] is a nice high-level way to express tree structure matching **and** binding of matched substructure to variables. It's simultaneously easy to decompose structures and immediately compute over the decomposition. Similar to regular expressions over strings, functional style patterns tend to look like the structures they're trying to match.

I have a soft spot for pattern matching because in my dissertation I suggested that they would be a powerful addition to multimedia scripting languages, especially languages embedded in Web browsers. The pattern matching would be handy for dealing with the tree structure of HTML pages.

I was both wrong and right. Functional style pattern matching never did wind up in the browser. **But** [XPath in JavaScript][4] bears witness that tree destructuring is actually pretty useful. Every language could seemingly use pattern matching, but it's exceedingly hard to embed in languages with Algol-style syntax.

[1]: http://docs.plt-scheme.org/reference/match.html

[2]: http://spin.atomicobject.com/2010/04/25/matchure-serious-clojure-pattern-matching

[3]: http://en.wikipedia.org/wiki/Common_Lisp#Macros

[4]: http://ejohn.org/blog/xpath-overnight/

