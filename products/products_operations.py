from products.products import Product



def action_one():
    supplier_id = input("\nSupplier ID: ")
    name = input("\nProduct name: ")
    info = input("\nInfo: ")
    price = input("\nPrice: ")
    quantity = input("\nQuantity: ")
    create_new_product(supplier_id, name, info, price, quantity)

def action_two():
    id_ = input("\nWhat is the product ID?\n")
    name = input("\nNew product name: ")
    update_product_name(id_, name)

def action_three():
    id_ = input("\nWhat is the product ID?\n")
    info = input("\nNew info: ")
    update_product_info(id_, info)

def action_four():
    id_ = input("\nWhat is the product ID?\n")
    price = input("\nNew price: ")
    update_product_price(id_, price)

def action_five():
    id_ = input("\nWhat is the product ID?\n")
    quantity = input("\nNew quantity: ")
    update_product_quantity(id_, quantity)

def create_new_product(supplier_id, name, info, price, quantity):
    new_product = Product(supplier_id, name, info, price, quantity)
    new_product.save_to_db()

def update_product_name(id, new_name):
    existing_product = Product(None, None, None, None, None, id)
    existing_product.update_name(new_name)

def update_product_info(id, new_info):
    existing_product = Product(None, None, None, None, None, id)
    existing_product.update_info(new_info)

def update_product_price(id, new_price):
    existing_product = Product(None, None, None, None, None, id)
    existing_product.update_price(new_price)

def update_product_quantity(id, new_quantity):
    existing_product = Product(None, None, None, None, None, id)
    existing_product.update_quantity(new_quantity)

def get_all_products():
    return Product.get_all_products()

def get_product_by_name(name):
    return Product.get_product_by_name(name)