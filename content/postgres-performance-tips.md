Title: Postgres Performance Tips
Date: 2012-10-03 20:00
Author: crossjam
Category: Uncategorized
Slug: postgres-performance-tips
Status: published

<img src="http://crossjam.net/wp/mpr/wp-content/uploads/2011/09/PostgreSQL-Logo.png" alt="PostgreSQL Logo" border="0" width="120" height="120" align="right" style="margin: 10px;" /> 
> For many application developers their database is a black box. Data goes in, comes back out and in between there developers hope its a pretty short time span. Without becoming a DBA there’s a few pieces of data that most application developers can easily grok which will help them understand if their database is performing adequately. This post will provide some quick tips that allow you to determine whether your database performance is slowing down your app, and if so what you can do about it.

[Craig Kerstiens provides some handy Postgres SQL][1] that reveals how well the RDBMS is handling your queries. Optimization is left as an exercise for the reader.

[1]: http://www.craigkerstiens.com/2012/10/01/understanding-postgres-performance/