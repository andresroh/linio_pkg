from linio import products, orders, linio
from config import user, key
import json

# login

session = linio(user,key)

# Inquire about a product
 
items = products(session)

product_list = ["TP-19100"]

print(items.get(SkuSellerList=json.dumps(product_list)))

# Inquire about an order

purchase = orders(session)

print(purchase.get(11073979))