# parent_directory/ 
#     main.py 
#     ecommerce/ 
#         __init__.py 
#         database.py 
#         products.py 
#         payments/ 
#             __init__.py 
#             square.py 
#             stripe.py 

import ecommerce.products
product = ecommerce.products.Product()

from ecommerce.products import Product
product = Product()

from ecommerce import products
product = products.Product()


# __init__.py contents:
#   from .database import db
# main.py contents could then be:
#   from ecommerce import db