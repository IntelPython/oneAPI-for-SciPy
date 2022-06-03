# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys

from sphinx.application import Sphinx

# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'SciPy 2022: oneAPI for Scientific Python Community'
copyright = '2022, Intel Corporation'
author = 'Diptorup Deb and Oleksandr Pavlyk, Intel Corp.'

master_doc = "index"
language = "en"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx_design",
    "sphinxext.rediraffe",
    "sphinxcontrib.mermaid",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"
html_logo = "_static/oneAPI-rgb-3000@2x.png"
html_favicon = "_static/oneAPI-rgb-3000@2x.png"
html_title = ""
html_theme_options = {
    "home_page_in_toc": True,
    "github_url": "https://github.com/oleksandr-pavlyk/oneAPI-for-SciPy",
    "repository_url": "https://github.com/oleksandr-pavlyk/oneAPI-for-SciPy",
    "repository_branch": "master",
    "use_repository_button": True,
    "use_edit_page_button": True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    "fieldlist",
    "html_admonition",
    "html_image",
    "colon_fence",
    "smartquotes",
    "linkify",
    "replacements",
    "strikethrough",
    "substitution",
    "tasklist",
]
myst_number_code_blocks = ["typescript"]
myst_heading_anchors = 2
myst_footnote_transition = True
myst_dmath_double_inline = True

rediraffe_redirects = {
}

suppress_warnings = ["myst.strikethrough"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3.10", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
    "markdown_it": ("https://markdown-it-py.readthedocs.io/en/latest", None),
    "dpctl": ("https://intelpython.github.io/dpctl", None),
    "dpnp": ("https://intelpython.github.io/dpnp", None),
    "numba_dpex": ("https://intelpython.github.io/numba-dpex", None),
    "numba": ("http://numba.pydata.org/numba-doc/latest/", None),
}

autodoc_member_order = "bysource"
nitpicky = True
nitpick_ignore = [
]

def setup(app: Sphinx):
    """Add functions to the Sphinx setup."""
    app.add_css_file("custom.css")
