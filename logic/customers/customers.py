from database.db_utils import db_cursor
import mysql.connector as db
import logging

logger = logging.getLogger(__name__)

def customers():
    with db_cursor() as cursor:
        cursor.execute("SELECT * FROM customers;")
        result = cursor.fetchall()
        return result

class Customer:
    def __init__(self, customer_name, customer_address, customer_contact, id = None):
        self.id = id
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.customer_contact = customer_contact

    def save_to_db(self):
        if not self.customer_name or not self.customer_address or not self.customer_contact:
            logger.warning("Insufficient Data for Creating Customer")
            raise ValueError("Customer name, address, and contact must not be empty")

        with db_cursor() as cursor:
            try:
                if self.id is None:
                    cursor.execute(
                        "INSERT INTO customers (customer_name, customer_address, customer_contact) VALUES (%s, %s, %s)",
                        (self.customer_name, self.customer_address, self.customer_contact)
                    )
                    self.id = cursor.lastrowid
                    print("\nCustomer added successfully\n")
                    logging.info("Customer Added Successfully")
            except db.Error as e:
                print(f"Database error: {e}")
                logging.error(f"Database Error {e}")


    def update_field(self, field, value, message):
        with db_cursor() as cursor:
            try:
                cursor.execute(
                    f"UPDATE customers SET {field} = %s WHERE id = %s",
                    (value, self.id)
                )
                setattr(self, field, value)
                print(f"\n{message} Updated Successfully\n")
                logging.info(f"{message} Updated Successfully")
            except db.Error as e:
                print(f"Database error: {e}")
                logging.error(f"Database Error {e}")

    def update_name(self, new_name):
        self.update_field("customer_name", new_name, "Name")

    def update_address(self, new_address):
        self.update_field("customer_address", new_address, "Address")

    def update_contact(self, new_contact):
        self.update_field("customer_contact", new_contact, "Contact")



    @staticmethod
    def execute_and_print(query, parameter):
        with db_cursor() as cursor:
            cursor.execute(query, parameter)
            result = cursor.fetchall()
            if not result:
                print(f"Could not find Customer: {parameter}")
                logging.warning(f"Could not find Customer: {parameter}")
            else:
                for customer in result:
                    print(f"\nID: {customer[0]}, Name: {customer[1]}, Address: {customer[2]}, Contact: {customer[3]}\n")

    @staticmethod
    def get_all_customers():
        Customer.execute_and_print("SELECT * FROM customers", None)

    @staticmethod
    def get_customer_by_name(name):
        Customer.execute_and_print("SELECT * FROM customers WHERE customer_name LIKE %s", ("%" + name + "%", ))