"""Sphinx documentation generator configuration."""

AUTHOR = 'sinoroc'
MASTER_DOCUMENT = 'contents'
SUBTITLE = 'Bits of knowledge'
TITLE = 'Sinoroc KB'

# General
# =======

extensions = [
    'sphinx.ext.graphviz',
]

master_doc = MASTER_DOCUMENT  # pylint: disable=invalid-name

suppress_warnings = [
    'download.not_readable',
]

templates_path = [
    'src/_templates',
]

# Project
# =======

project = TITLE  # pylint: disable=invalid-name

# HTML
# ====

html_show_copyright = False  # pylint: disable=invalid-name
html_show_sphinx = False  # pylint: disable=invalid-name

html_sidebars = {
    '**': [
        'about.html',  # Provided by 'alabaster' theme
        'globaltoc.html',
        'searchbox.html',
    ],
}

html_theme_options = {
    'description': SUBTITLE,
}

html_title = TITLE  # pylint: disable=invalid-name

html_use_modindex = False  # pylint: disable=invalid-name
html_use_index = False  # pylint: disable=invalid-name

# Latex
# =====

latex_documents = [
    (
        MASTER_DOCUMENT,
        f'{TITLE.lower().replace(" ", "")}.tex',
        TITLE,
        AUTHOR,
        'manual',
    )
]

latex_elements = {
    'papersize': 'a4paper',
}

latex_show_pagerefs = True  # pylint: disable=invalid-name
latex_show_urls = 'footnote'  # pylint: disable=invalid-name

latex_toplevel_sectioning = 'part'  # pylint: disable=invalid-name
