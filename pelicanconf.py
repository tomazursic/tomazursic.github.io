#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PORT = 9000
AUTHOR = "Tomaz"
SITEURL = "tomazursic.github.io"
SITENAME = "Weblog - " + SITEURL

PLUGIN_PATHS = ["./pelican-plugins"]
PLUGINS = ["tipue_search.tipue_search", "sitemap", "pelican-ipynb.markup"]
PATH = "content"

MARKUP = ("md", "ipynb")

IGNORE_FILES = [".ipynb_checkpoints"]

DIRECT_TEMPLATES = ["index", "tags", "categories", "authors", "archives", "search"]

TIMEZONE = "Europe/Ljubljana"

THEME = "themes/l33t"
DEFAULT_LANG = "en"

# The path to images
STATIC_PATHS = ["images"]

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = 'feeds/all.atom.xml'
# TAG_FEED_ATOM = 'feeds/%s.tag.atom.xml'
# CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
    },
    "output_format": "html5",
}

# Blogroll

# LINKS = (('Nova Gorica - The Things Network Community', 'https://www.thethingsnetwork.org/community/nova-gorica/'),
#          ('IoT Nova Gorica', 'http://iot.novagorica.eu/'),
#          )

# Social widget
# SOCIAL = (('Twitter TTN_Nova_Gorica', 'https://twitter.com/TTN_Nova_Gorica'),
#           )
import math

JINJA_FILTERS = {
    "count_to_font_size": lambda c: "{p:.1f}%".format(p=100 + 25 * math.log(c, 2)),
}

GOOGLE_ANALYTICS = "UA-155970867-1"

SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 1, "indexes": 0.5, "pages": 0.5,},
    "changefreqs": {"articles": "always", "indexes": "hourly", "pages": "monthly"},
}
# MENUITEMS = [
#     ['RSS', "feeds/all.atom.xml"]
# ]
DEFAULT_TITLE = None
