""" Sphinx documentation generator configuration
"""


MASTER_DOCUMENT = 'contents'
TITLE = "Sinoroc KB"
SUBTITLE = "Bits of knowledge"


# 
# General
#

master_doc = MASTER_DOCUMENT


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
    ],
}

html_theme = 'alabaster'
html_theme_options = {
    'description': SUBTITLE,
}

html_title = TITLE

html_use_modindex = False
html_use_index = False


# EOF
