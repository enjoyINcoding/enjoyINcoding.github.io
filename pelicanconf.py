#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jianzhi Zhang'
SITENAME = u'EnjoyINcoding'
SITEURL = ''

THEME = 'Casper2Pelican'

PATH = 'content'
OUTPUT_PATH = '/'

ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
PAGE_PATHS = ['pages']

RELATIVE_URLS = True
DEFAULT_PAGINATION = 5
TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

#日期格式设置，可按自己喜好设定

# Feed generation is usually not desired when developing
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

REVERSE_CATEGORY_ORDER = True
# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)


DISQUS_SITENAME = 'zjzblog'
GOOGLE_ANALYTICS = u"UA-66850247-1"
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}