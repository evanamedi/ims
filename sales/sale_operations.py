from sales.sales import Sale

def create_sale(product, customer, date, quantity):
    new_sale = Sale(product, customer, date, quantity)
    new_sale.save_to_db()

def update_product(id, new_product):
    sale = Sale(None, None, None, None, id)
    sale.update_product(new_product)

def update_customer(id, new_customer):
    sale = Sale(None, None, None, None, id)
    sale.update_customer(new_customer)

def update_date(id, new_date):
    sale = Sale(None, None, None, None, id)
    sale.update_date(new_date)

def update_quantity(id, new_quantity):
    sale = Sale(None, None, None, None, id)
    sale.update_quantity(new_quantity)

def get_all_sales():
    return Sale.get_all_sales()

def get_product_sales(product):
    return Sale.get_product_sales(product)

def get_customer_sales(customer):
    return Sale.get_customer_sales(customer)

def get_date_sales(date):
    return Sale.get_date_sales(date)

def action_one():
    product = input("Enter Product #: ")
    customer = input("Enter Customer #: ")
    date = input("Enter Date: ")
    quantity = input("Enter Quantity: ")
    create_sale(product, customer, date, quantity)

def action_two():
    id_ = input("Enter Sales #: ")
    product = input("Enter New Product #: ")
    update_product(id_, product)

def action_three():
    id_ = input("Enter Sales #: ")
    customer = input("Enter New Customer #: ")
    update_customer(id_, customer)

def action_four():
    id_ = input("Enter Sales #: ")
    date = input("Enter New Date")
    update_date(id_, date)

def action_five():
    id_ = input("Enter Sales #: ")
    quantity = input("Enter New Quantity")
    update_quantity(id_, quantity)
