# Configuration file for the Sphinx documentation builder.
# Lao PDR Whole Energy System Model (WESM) - documentation
#
# Full list of options: https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = "OSeMOSYS Lao PDR WESM"
copyright = "2026, Climate Compatible Growth (CCG) programme"
author = "Sridharan et al."

# The short X.Y version and the full version, including tags
version = "2.0"
release = "2.0.0"

# -- General configuration ---------------------------------------------------

extensions = [
    "myst_parser",
    "sphinx.ext.autosectionlabel",
]

# Support both Markdown (MyST) and reStructuredText source files
source_suffix = {
    ".md": "markdown",
    ".rst": "restructuredtext",
}

# Prefix section labels with the document name to avoid duplicate-label warnings
autosectionlabel_prefix_document = True

# MyST extensions (tables, figures with captions, math, etc.)
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_image",
    "linkify",
    "substitution",
]
myst_heading_anchors = 3

templates_path = ["_templates"]
# "_deploy_readthedocs.md" is a maintainer note, not part of the published docs
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "_deploy_readthedocs.md"]

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_title = "OSeMOSYS Lao PDR WESM"
