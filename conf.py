#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# kittenbot docs documentation build configuration file, created by
# sphinx-quickstart on Fri Feb 23 20:48:29 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.


import os
import sys
sys.path.insert(0, os.path.abspath('./'))
sys.path.append(os.path.abspath("./_ext"))

copyright = '2020, Kittenbot HK'
author = 'Kittenbot HK'

import recommonmark
from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify

source_parsers = {
    '.md': recommonmark.parser.CommonMarkParser,
}
source_suffix = {
    '.rst': 'restructuredtext', 
    '.md': 'markdown',
}

# def get_version():
#     """Return package version from setup.cfg."""
#     config = RawConfigParser()
#     config.read(os.path.join('..', 'setup.cfg'))
#     return config.get('metadata', 'version')


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#

# needs_sphinx = '2.4.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.coverage',
    'sphinx.ext.autodoc',
    # 'sphinx_tabs.tabs',
    # 'sphinx_js',
    'sphinx.ext.todo',
    'sphinx.ext.autosectionlabel',  # 异页跳转
    # [My Subtitle][]
    # [My Subtitle]: <path/to/md:title>

    # 'sphinxcontrib.httpdomain',
    # "sphinx_rtd_theme"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
# source_suffix = '.rst'

# js_source_path = 'sphinx_search/static/js/'



# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Kittenbot HK hub'
copyright = '2020, Kittenbot HK'
author = 'Kittenbot HK team'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = release = ''
# The full version, including alpha/beta/rc tags.
# release = ''
# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'
# gettext_compact = False
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
# exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
# autosectionlabel_prefix_document = True
# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#


html_theme = 'sphinx_rtd_theme'


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".


# These folders are copied to the documentation's HTML output
html_static_path = ['_static']
# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
# html_css_files = [
#     'css/custom.css',
# ]

html_style = 'css/new.css'
# html_theme = 'insegel'

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars

# html_sidebars = {
#     '**': [
#         'relations.html',  # needs 'show_related': True theme option to display
        
#     ]
# }


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'kittenbot HK-doc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize':
    'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize':
    '11pt',

    # Additional stuff for the LaTeX preamble.
    'preamble':
    r'''
        \usepackage{charter}
        \usepackage[defaultsans]{lato}
        \usepackage{inconsolata}
    ''',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'kittenbotdocs.tex', u'kittenbot docs Documentation', u'kittenbot team', 'manual'),
]


# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = True

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = False


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    # (master_doc, 'kittenbotdocs', 'kittenbot docs Documentation',
    #  [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)

texinfo_documents = [
    # (master_doc, 'kittenbotdocs', 'kittenbot docs Documentation',
    #  author, 'kittenbotdocs', 'One line description of project.',
    #  'Miscellaneous'),
]

# html_theme_options = {
#     'sticky_navigation': True,  # Set to False to disable the sticky nav while scrolling.
#     'style_external_links': True,
#     'logo_only': True,  # if we have a html_logo below, this shows /only/ the logo with no title text
#     'collapse_navigation': False,  # Collapse navigation (False makes it tree-like)
# }

html_logo = 'images/sharinghub_logo.png'

html_theme_options = {
    'canonical_url': '',
    # 'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
    'logo_only': True,
    'display_version': False,
    'prev_next_buttons_location': 'bottom',
    # 'style_external_links': False,
    'style_external_links': True,
    # 'style_nav_header_background': '',
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': False,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': True,
    'style_external_links': False

}


# AutoStructify
def setup(app):
    app.add_config_value('recommonmark_config', {
            'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)
