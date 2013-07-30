# -*- coding: utf-8 -*-

from fanstatic import Library, Resource, Group
from js.bootstrap import bootstrap_css, bootstrap_js

library = Library('bootstrapdatepicker', 'resources')

bootstrapdatepicker_css = Resource(
    library, 'bootstrap-datepicker.css',
    depends=[bootstrap_css],
)

bootstrapdatepicker_js = Resource(
    library, 'bootstrap-datepicker.js',
    depends=[bootstrap_js],
    minified='bootstrap-datepicker.min.js',
    minifier='jsmin',
)

bootstrapdatepicker = Group([
    bootstrapdatepicker_css,
    bootstrapdatepicker_js,
])
