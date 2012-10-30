import fanstatic
import js.jquery

library = fanstatic.Library('strophe.js', 'resources')

strophe = fanstatic.Resource(
    library, 'strophe.js', minified='strophe.min.js',
    depends=[js.jquery.jquery])
