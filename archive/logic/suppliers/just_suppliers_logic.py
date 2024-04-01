from database.db_utils import db_cursor

class Supplier:
    def __init__(self, supplier_name, supplier_address, supplier_contact, id=None):
        self.id = id
        self.supplier_name = supplier_name
        self.supplier_address = supplier_address
        self.supplier_contact = supplier_contact

    def to_dict(self):
        return {
            "id": self.id,
            "supplier_name": self.supplier_name,
            "supplier_address": self.supplier_address,
            "supplier_contact": self.supplier_contact
        }

    def save_to_db(self):
        with db_cursor() as cursor:
            if self.id is None:
                cursor.execute(
                    "INSERT INTO suppliers (supplier_name, supplier_address, supplier_contact) VALUES (%s, %s, %s)",
                    (self.supplier_name, self.supplier_address, self.supplier_contact)
                )
                self.id = cursor.lastrowid

    def update_field(self, field, value):
        field_mapping = {
            "name": "supplier_name",
            "address": "supplier_address",
            "contact": "supplier_contact"
        }
        
        db_field = field_mapping.get(field)
        with db_cursor() as cursor:
            cursor.execute(
                f"UPDATE suppliers SET {db_field} = %s WHERE id = %s",
                (value, self.id)
                )
            setattr(self, db_field, value)

    def update_name(self, new_name):
        self.update_field("name", new_name)

    def update_address(self, new_address):
        self.update_field("address", new_address)

    def update_contact(self, new_contact):
        self.update_field("contact", new_contact)

    @staticmethod
    def execute_and_print(query, parameter):
        with db_cursor() as cursor:
            cursor.execute(query, parameter)
            result = cursor.fetchall()
            suppliers = []
            for supplier in result:
                print(f"\nID: {supplier[0]} | Name: {supplier[1]} | Address: {supplier[2]} | Contact: {supplier[3]}\n")
                suppliers.append(Supplier(supplier[1], supplier[2], supplier[3], supplier[0]))
        return suppliers

    @staticmethod
    def get_all_suppliers():
        return Supplier.execute_and_print("SELECT * FROM suppliers", None)

    @staticmethod
    def get_supplier_by_name(name):
        return Supplier.execute_and_print("SELECT * FROM suppliers WHERE supplier_name LIKE %s", ("%" + name + "%", ))

    @staticmethod
    def find_by_id(supplier_id):
        result = Supplier.execute_and_print("SELECT * FROM suppliers WHERE id = %s", (supplier_id,))
        return result[0] if result else None