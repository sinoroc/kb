""" Sphinx documentation generator configuration
"""


NAME = "Sinoroc KB"


# 
# Global
#

project = NAME


#
# HTML
#

html_show_copyright = False
html_show_sphinx = False

html_sidebars = {
    '**': [
        'searchbox.html',
        'globaltoc.html',
    ],
    'contents': [
        'searchbox.html',
    ],
    'index': [
    ],
}

html_title = NAME

html_use_modindex = False
html_use_index = False


# EOF
