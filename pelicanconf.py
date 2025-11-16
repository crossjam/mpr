#!/usr/bin/env python
# -*- coding: utf-8 -*- #


PLUGIN_PATHS = ["plugins/pelican-plugins", "plugins", "plugins/pelican_json_feed"]
PLUGINS = ["summary", "period"]

PLUGINS = ["summary", "pelican_json_feed", "yaml_metadata"]

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {
            "css_class": "highlight",
            "use_pygments": True,
        },
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "pyembed.markdown": {},
        # "markdown.extensions.pyembed": {},
    }
}

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
CHECK_MODIFIED_METHOD = "mtime"

ARTICLE_URL = "{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{slug}/index.html"
MONTH_ARCHIVE_SAVE_AS = "{date:%Y}/{date:%m}/index.html"
MONTH_ARCHIVE_URL = "{date:%Y}/{date:%m}/"
YEAR_ARCHIVE_SAVE_AS = "{date:%Y}/index.html"
YEAR_ARCHIVE_URL = "{date:%Y}/"

# YEAR_ARCHIVE_SAVE_AS = "posts/{date:%Y}/index.html"
# MONTH_ARCHIVE_SAVE_AS = "posts/{date:%Y}/{date:%m}/index.html"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_JSON = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_METADATA = {
    "status": "published",
}

DEFAULT_CATEGORY = "Uncategorized"
DEFAULT_DATE = "fs"
TYPOGRIFY = True
TYPOGRIFY_IGNORE_TAGS = ["pre", "code", "head"]

DISPLAY_CATEGORIES_ON_MENU = False
TAGS_SAVE_AS = ""
TAG_SAVE_AS = ""
SUMMARY_MAX_LENGTH = None

SHOW_DRAFTS = True

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
    "mpr",
]

EXTRA_PATH_METADATA = {
    "static/robots.txt": {"path": "robots.txt"},
    "static/favicon.ico": {"path": "favicon.ico"},
    "static/favicon-16x16.png": {"path": "favicon-16x16.png"},
    "static/favicon-32x32.png": {"path": "favicon-32x32.png"},
    "static/apple-touch-icon.png": {"path": "apple-touch-icon.png"},
    "static/site.webmanifest": {"path": "site.webmanifest"},
}


# Social widget
SOCIAL = (
    ("twitter (dormant)", "https://twitter.com/crossjam"),
    ("github", "https://github.com/crossjam"),
)

GITHUB_URL = "https://github.com/crossjam"

DEFAULT_PAGINATION = 40
# THEME = "crowsfoot"
# THEME = "crossjam-svbhack"
THEME = "themes/crossjam-svbhack"

# SITEURL = "http://gabrielhounds:8000"
# SITEURL = "http://localhost:8000"
# SITEURL = "http://burningchrome:8000"
USER_LOGO_URL = SITEURL + "/theme/images/logo.png"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

IGNORE_FILES = [".#*", "*~", "#*", "*.bak", "#*"]
