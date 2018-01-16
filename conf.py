""" Sphinx documentation generator configuration
"""


AUTHOR = 'sinoroc'
MASTER_DOCUMENT = 'contents'
SUBTITLE = "Bits of knowledge"
TITLE = "Sinoroc KB"


# 
# General
#

extensions = [
    'sphinx.ext.graphviz',
]

master_doc = MASTER_DOCUMENT

templates_path = [
    'src/_templates',
]


#
# Project
#

project = TITLE


#
# HTML
#

html_show_copyright = False
html_show_sphinx = False

html_sidebars = {
    # 'about.html' provided by 'alabaster' theme
    '**': [
        'about.html',
        'globaltoc.html',
        'searchbox.html',
    ],
}

html_theme_options = {
    'description': SUBTITLE,
}

html_title = TITLE

html_use_modindex = False
html_use_index = False


#
# Latex
#

latex_documents = [(
    MASTER_DOCUMENT,
    '{}.tex'.format(TITLE.lower().replace(' ', '')),
    TITLE,
    AUTHOR,
    'manual',
)]

latex_elements = {
    'papersize': 'a4paper',
}

latex_show_pagerefs = True
latex_show_urls = 'footnote'

latex_toplevel_sectioning = 'part'


# EOF
