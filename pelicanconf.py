#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Kangjie Lu'
SITENAME = 'EthiCS: Ethics in Computer Security'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

THEME = 'lib/pelican-bootstrap3'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['lib']
PLUGINS = ['i18n_subsites']
I18N_TEMPLATES_LANG = 'en'

STATIC_PATHS = ['img', 'static']
FAVICON = 'img/favicon.ico'
CUSTOM_CSS = 'static/custom.css'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

MENUITEMS = [
        ('Program', 'program.html'),
        ('Keynotes', 'keynote.html'),
        ('Registration/Venue', 'reg.html'),
        ]

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

HIDE_SIDEBAR = True
DISPLAY_CATEGORIES_ON_MENU = False
