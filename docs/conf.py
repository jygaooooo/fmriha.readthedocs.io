from datetime import datetime
from pathlib import Path
import shutil

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
myst_heading_anchors = 3

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
    "github_repo": "fmriha.readthedocs.io",
    "github_version": "main",
    "conf_py_path": "/docs/",
}


def _copy_understand_ha_assets(app, exception):
    if exception is not None:
        return

    docs_dir = Path(__file__).parent
    source_notebooks = docs_dir / "notebooks"
    output_notebooks = Path(app.outdir) / "notebooks"
    output_notebooks.mkdir(parents=True, exist_ok=True)

    for name in [
        "single_cat_feature_alignment.html",
        "three_cat_geometry_alignment.html",
    ]:
        shutil.copy2(source_notebooks / name, output_notebooks / name)

    source_pic_dir = source_notebooks / "pic" / "understandHA" / "html"
    output_pic_dir = output_notebooks / "pic" / "understandHA" / "html"
    output_pic_dir.mkdir(parents=True, exist_ok=True)

    for name in ["cat1.png", "cat2.png", "cat3.png"]:
        shutil.copy2(source_pic_dir / name, output_pic_dir / name)


def setup(app):
    app.connect("build-finished", _copy_understand_ha_assets)
