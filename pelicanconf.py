#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'tomazursic'
SITENAME = 'Weblog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Ljubljana'

THEME = 'themes/l33t'
DEFAULT_LANG = 'en'

# The path to images
STATIC_PATHS = ['images']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

# Blogroll

# LINKS = (('Nova Gorica - The Things Network Community', 'https://www.thethingsnetwork.org/community/nova-gorica/'),
#          ('IoT Nova Gorica', 'http://iot.novagorica.eu/'),
#          )

# Social widget
# SOCIAL = (('Twitter TTN_Nova_Gorica', 'https://twitter.com/TTN_Nova_Gorica'),
#           )

