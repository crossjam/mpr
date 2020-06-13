Title: OSM & PGSQL
Date: 2012-10-09 22:37
Author: crossjam
Category: Uncategorized
Slug: osm-pgsql
Status: published

Michal Migurski [drops knowledge][1] on how to get OpenStreetMap data into PostgreSQL/PostGIS:

> At first glance, OSM data and Postgres (specifically PostGIS) seem like a natural, easy fit for one another: OSM is vector data, PostGIS stores vector data. OSM has usernames and dates-modified, PostGIS has columns for storing those things in tables. OSM is a worldwide dataset, PostGIS has fast spatial indexes to get to the part you want. When you get to OSM’s free-form tags, though, the row/column model of Postgres stops making sense and you start to reach for linking tables or advanced features like hstore.

[1]: http://mike.teczno.com/notes/osm-and-postgres.html