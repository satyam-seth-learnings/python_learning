# Example-21 Module
from Admin.Comman import *
# Before Adding __all__ in __init__.py
# header.admin_comman_header() NameError: name 'header' is not defined
# After Adding __all__=['header','footer'] in __init__.py
header.admin_comman_header()
footer.admin_comman_footer()