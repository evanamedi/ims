from suppliers.suppliers import Supplier

def create_new_supplier(name, address, contact):
    new_supplier = Supplier(name, address, contact)
    new_supplier.save_to_db()

def update_existing_supplier(name, address, contact, id):
    existing_supplier = Supplier(name, address, contact, id)
    existing_supplier.save_to_db()

def update_supplier_name(id, new_name):
    existing_supplier = Supplier(None, None, None, id)
    existing_supplier.update_name(new_name)

def update_supplier_address(id, new_address):
    existing_supplier = Supplier(None, None, None, id)
    existing_supplier.update_address(new_address)

def update_supplier_contact(id, new_contact):
    existing_supplier = Supplier(None, None, None, id)
    existing_supplier.update_contact(new_contact)

def get_all_suppliers():
    return Supplier.get_all_suppliers()

def get_supplier_by_name(name):
    return Supplier.get_supplier_by_name(name)

def action_one():
    name = input("Enter Supplier Name: ")
    address = input("Enter Supplier Address: ")
    contact = input("Enter Supplier Contact: ")
    create_new_supplier(name, address, contact)

def action_two():
    id_ = input("Enter Supplier ID: ")
    name = input("Enter New Name: ")
    update_supplier_name(id_, name)


def action_three():
    id_ = input("Enter Supplier ID: ")
    address = input("Enter New Address: ")
    update_supplier_address(id_, address)


def action_four():
    id_ = input("Enter Supplier ID: ")
    contact = input("Enter New Contact: ")
    update_supplier_contact(id_, contact)