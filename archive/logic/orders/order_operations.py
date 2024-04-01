from orders.orders import Order



def action_one():
    product = input("Enter Product #: ")
    date = input("Enter Date: ")
    quantity = input("Enter Quantity: ")
    create_order(product, date, quantity)

def action_two():
    id_ = input("Enter Order #: ")
    product = input("Enter New Product #: ")
    update_product(id_, product)

def action_three():
    id_ = input("Enter Order #: ")
    date = input("Enter Updated Date: ")
    update_date(id_, date)

def action_four():
    id_ = input("Enter Order #: ")
    quantity = input("Enter Updated Quantity: ")
    update_quantity(id_, quantity)

def create_order(product, date, quantity):
    new_order = Order(product, date, quantity)
    new_order.save_to_db()

def update_order(id, product, date, quantity):
    update_order = Order(id, product, date, quantity)
    update_order.save_to_db

def update_product(id, new_product):
    order = Order(None, None, None, id)
    order.update_product(new_product)

def update_date(id, new_date):
    order = Order(None, None, None, id)
    order.update_date(new_date)

def update_quantity(id, new_quantity):
    order = Order(None, None, None, id)
    order.update_quantity(new_quantity)

def get_all_orders():
    return Order.get_all_orders()

def get_order_by_product(product):
    return Order.get_order_by_product(product)