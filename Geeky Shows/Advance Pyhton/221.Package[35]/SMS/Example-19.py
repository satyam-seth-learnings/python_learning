# Example-19 Module
from Admin import *
# Before Adding __all__ in __init__.py
# service.admin_service()  NameError: name 'service' is not defined
# product.admin_product()
# After Adding __all__=['service'] in __init__.py
# service.admin_service() 
# -> 
# Admin Package --> service Module
# admin_service Function
# 
# product.admin_product()   NameError: name 'product' is not defined
# After Adding __all__=['service','product'] in __init__.py
service.admin_service()
product.admin_product()