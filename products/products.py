# products/products.py
products_catalog = []

def add_product(name, price):
    products_catalog.append({"name": name, "price": price})

def list_products():
    return products_catalog