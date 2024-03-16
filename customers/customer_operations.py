from customers.customers import Customer

def create_customer(name, address, contact):
    new_customer = Customer(name, address, contact)
    new_customer.save_to_db()

def update_name(id, name):
    customer = Customer(None, None, None, id)
    customer.update_name(name)

def update_address(id, address):
    customer = Customer(None, None, None, id)
    customer.update_address(address)

def update_contact(id, contact):
    customer = Customer(None, None, None, id)
    customer.update_contact(contact)

def get_all_customers():
    return Customer.get_all_customers()

def search_customer(name):
    return Customer.get_customer_by_name(name)

def action_one():
    name = input("\nWhat is the name?\n")
    address = input("What is the address?\n")
    contact = input("What is the contact\n")
    create_customer(name, address, contact)

def action_two():
    id_ = input("\nWhat is the ID?\n")
    name = input("What is the new name?\n")
    update_name(id_, name)

def action_three():
    id_ = input("\nWhat is the ID?\n")
    address = input("What is the new address?\n")
    update_address(id_, address)

def action_four():
    id_ = input("\nWhat is the ID?\n")
    contact = input("What is the new contact\n")
    update_contact(id_, contact)


