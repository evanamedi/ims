from database.db_utils import db_cursor
import mysql.connector as db
import logging

logger = logging.getLogger(__name__)

class Sale:
    def __init__(self, product_id, customer_id, sale_date, sale_quantity, id = None):
        self.id = id
        self.product_id = product_id
        self.customer_id = customer_id
        self.sale_date = sale_date
        self.sale_quantity = sale_quantity

    def save_to_db(self):
        if not self.product_id or not self.customer_id or not self.sale_date or not self.sale_quantity:
            logger.warning("Insufficient Data for Creating user")
            raise ValueError("Product #, customer #, date, and quantity must not be empty")

        with db_cursor() as cursor:
            try:
                if self.id is None:
                    cursor.execute(
                        "INSERT INTO sales (product_id, customer_id, sale_date, sale_quantity) VALUES (%s, %s, %s, %s)",
                        (self.product_id, self.customer_id, self.sale_date, self.sale_quantity)
                    )
                    self.id = cursor.lastrowid
                    print("\nSale Added Successfully\n")
                    logging.info("Sale Added Successfully")
            except db.Error as e:
                print(f"Database error: {e}")
                logging.error(f"Database Error {e}")

    def update_field(self, field, value, message):
        with db_cursor() as cursor:
            try:
                cursor.execute(
                    f"UPDATE sales SET {field} = %s WHERE id = %s",
                    (value, self.id)
                )
                setattr(self, field, value)
                print(f"\n{message} Updated Successfully\n")
                logging.info(f"{message} Updated Successfully")
            except db.Error as e:
                print(f"Database error: {e}")
                logging.error(f"Database Error {e}")

    def update_product(self, new_id):
        self.update_field("product_id", new_id, "Product")

    def update_customer(self, customer):
        self.update_field("customer_id", customer, "Customer")

    def update_date(self, date):
        self.update_field("sale_date", date, "Date")

    def update_quantity(self, quantity):
        self.update_field("sale_quantity", quantity, "Quantity")

    @staticmethod
    def execute_and_print(query, parameter):
        with db_cursor() as cursor:
            cursor.execute(query, parameter)
            result = cursor.fetchall()
            if not result:
                print(f"Could not find sales for: {parameter}")
                logging.warning(f"Could not find sales for: {parameter}")
            else:
                for sale in result:
                    print(f"\nSale #: {sale[0]} | Product #: {sale[1]} | Customer #: {sale[2]} | Sale Date: {sale[3]} | Quantity: {sale[4]}")

    @staticmethod
    def get_all_sales():
        Sale.execute_and_print("SELECT * FROM sales", None)

    @staticmethod
    def get_product_sales(product):
        Sale.execute_and_print("SELECT * FROM sales WHERE product_id = %s", (product,))

    @staticmethod
    def get_customer_sales(customer):
        Sale.execute_and_print("SELECT * FROM sales WHERE customer_id = %s", (customer,))

    @staticmethod
    def get_date_sales(date):
        Sale.execute_and_print("SELECT * FROM sales WHERE sale_date = %s", (date,))