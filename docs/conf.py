from datetime import datetime

project = "fMRI-HA"
author = "GongLab"
if datetime.now().year == 2026:
    copyright = "2026"
else:
    copyright = f"2026-{datetime.now().year}"

release = "1.0"
version = "1.0"

extensions = [
    "myst_nb",
    "sphinx_copybutton",
    "sphinx.ext.mathjax",
]

myst_enable_extensions = [
    "dollarmath",
    "amsmath",
]

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**.ipynb_checkpoints",
]

language = "en"

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "myst-nb",
    ".ipynb": "myst-nb",
}

root_doc = "index"

nb_execution_mode = "off"

html_theme = 'sphinx_rtd_theme'
html_title = "fMRI-HA"
html_short_title = "fMRI-HA"
html_theme_options = {
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": 3,
    "titles_only": False,
}

html_context = {
    "display_github": True,
    "github_user": "jygaooooo",
    "github_repo": "fmrihatestweb",
    "github_version": "main",
    "conf_py_path": "/docs/",
}
