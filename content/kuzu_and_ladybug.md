---
title: "KuzuDB and LadybugDB"
date: 2025-11-17
author: "C. Ross Jam"
status: published
---

[KuzuDB][3] is a professional take on a graph database
engine. Also embeddable so sort of like SQLite for graph and vector
data.

Unfortunately, the company behind the open source project, [up and
pulled stakes][3] according to [The
Register](https://www.theregister.com). One of the more annoying
possible outcomes of a VC backed project ([c.f. Marimo][5]).

> The KuzuDB embedded graph database, open source under the MIT
> license, has been abandoned by its creator and sponsor Kùzu Inc,
> leaving its community pondering whether to fork or find an
> alternative. 

> A few days ago, the GitHub project was archived and a note appeared
> stating that "Kuzu is working on something new." In addition, the
> documentation and blog post archive were moved from the Kuzu website
> to GitHub. 

Since the project was developed with a generous open source license,
forking was quite an eminent possibility. Enter [LadybugDB][1]:

> LadybugDB is a modern graph database designed with a primary focus
> on object storage. Unlike traditional databases that treat storage
> as an afterthought, LadybugDB places object storage at the core of
> its architecture, enabling efficient management of complex,
> interconnected data structures while maintaining the flexibility and
> scalability that modern applications demand. 

> Built on top of KuzuDB, LadybugDB inherits a robust and modular
> implementation of cypher. KuzuDB was previously developed by Kùzu Inc.

Here’s the [repo][4]. The emphasis on object storage takes it in a bit
of a different direction though. Now moving into DuckDB territory.

[1]: https://ladybugdb.com
[2]: https://github.com/kuzudb/kuzu
[3]: https://www.theregister.com/2025/10/14/kuzudb_abandoned/
[4]: https://github.com/LadybugDB/ladybug
[5]: {filename}/marimo_acquired.md
