#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

PLUGINS = ["summary", "pelican_json_feed", "yaml_metadata", "archive_data"]

DEFAULT_METADATA = {
    "status": "draft",
}

DISPLAY_CATEGORIES_ON_MENU = False
SHOW_DRAFTS = False

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://mpr.crossjam.net"
USER_LOGO_URL = SITEURL + "/theme/images/logo.png"

RELATIVE_URLS = False

FEED_DOMAIN = "https://mpr.crossjam.net/wp/mpr"
FEED_ATOM = "feed/atom.xml"
FEED_ALL_ATOM = "feed/atom/atom.xml"
FEED_ALL_RSS = "feed/rss.xml"
FEED_ALL_JSON = "feed/feed.json"
FEED_MAX_ITEMS = 30

DELETE_OUTPUT_DIRECTORY = True

SHOW_DRAFTS = False
# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
