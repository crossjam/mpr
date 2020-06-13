#!/usr/bin/env python
# -*- coding: utf-8 -*- #


PLUGIN_PATHS = ["/Users/crossjam/gitrepos/pelican-plugins"]
PLUGINS = ["summary"]

MARKDOWN = {"extension_configs": {"pyembed.markdown": {}}}

AUTHOR = "C. Ross Jam"
SITENAME = "Mass Programming Resistance"
SITEURL = ""
SITESUBTITLE = "information informs. analysis enlightens."
TAGLINE = "information informs. analysis enlightens."

PATH = "content"
TIMEZONE = "America/New_York"
DEFAULT_LANG = "en"

CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True

ARTICLE_URL = "{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{slug}/index.html"
MONTH_ARCHIVE_SAVE_AS = "{date:%Y}/{date:%m}/index.html"
MONTH_ARCHIVE_URL = "{date:%Y}/{date:%m}/"
YEAR_ARCHIVE_SAVE_AS = "{date:%Y}/index.html"
YEAR_ARCHIVE_URL = "{date:%Y}/"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_DATE = "fs"
TYPOGRIFY = True
DISPLAY_CATEGORIES_ON_MENU = False
TAGS_SAVE_AS = ""
TAG_SAVE_AS = ""
SUMMARY_MAX_LENGTH = None

# Blogroll
LINKS = (
    ("Built by a Pythonista ...", "https://www.python.org/"),
    ("... using Pelican", "https://getpelican.com/"),
)

STATIC_PATHS = [
    "static",
    "images",
    "wp-content",
    "media",
]

EXTRA_PATH_METADATA = {
    "static/robots.txt": {"path": "robots.txt"},
}


# Social widget
SOCIAL = (
    ("twitter (dormant)", "https://twitter.com/crossjam"),
    ("github", "https://github.com/crossjam"),
)

GITHUB_URL = "https://github.com/crossjam"

DEFAULT_PAGINATION = 40
# THEME = "crowsfoot"
THEME = "crossjam-svbhack"
SITEURL = "http://localhost:8080"
USER_LOGO_URL = SITEURL + "/theme/images/logo.png"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
