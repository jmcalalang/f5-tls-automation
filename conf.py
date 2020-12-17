import os
import sys

sys.path.append(os.path.join(os.environ["SAMPLE_DOCS_LOCATION"], "demo"))
print("", sys.path[-1], "", sep="\n" + "-" * 80 + "\n")

# -- Project information -----------------------------------------------------

project = 'F5 TLS Automation'
copyright = '2020, Jon Calalang (jon@f5.com)'
author = 'Jon Calalang (jon@f5.com)'

# The full version, including alpha/beta/rc tags
release = '0.1'

# -- Extensions --------------------------------------------------------------
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
]

# -- Options for HTML output -------------------------------------------------

html_title = project

# NOTE: All the lines are after this are the theme-specific ones. These are
#       written as part of the site generation pipeline for this project.
# !! MARKER !!
html_theme = "f5_sphinx_theme"
