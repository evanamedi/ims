from database.db_utils import db_cursor
import mysql.connector as db
import logging

logger = logging.getLogger(__name__)

class Order:
    def __init__(self, product_id, order_date, order_quantity, id = None):
        self.id = id
        self.product_id = product_id
        self.order_date = order_date
        self.order_quantity = order_quantity

    def save_to_db(self):
        if not self.product_id or not self.order_date or not self.order_quantity:
            logger.warning("Insufficient Data for Creating Order")
            raise ValueError("Product #, date, and quantity must not be empty")

        with db_cursor() as cursor:
            try:
                if self.id is None:
                    cursor.execute(
                        "INSERT INTO orders (product_id, order_date, order_quantity) VALUES (%s, %s, %s)",
                        (self.product_id, self.order_date, self.order_quantity)
                    )
                    self.id = cursor.lastrowid
                    print("\nOrder added successfully\n")
                    logging.info("Order Added Successfully")
            except db.Error as e:
                print(f"Database error: {e}")
                logging.error(f"Database Error {e}")


    def update_field(self, field, value, message):
        with db_cursor() as cursor:
            try:
                cursor.execute(
                    f"UPDATE orders SET {field} = %s WHERE id = %s",
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

    def update_date(self, new_date):
        self.update_field("order_date", new_date, "Order")

    def update_quantity(self, new_quantity):
        self.update_field("order_quantity", new_quantity, "Quantity")


    @staticmethod
    def execute_and_print(query, parameter):
        with db_cursor() as cursor:
            cursor.execute(query, parameter)
            result = cursor.fetchall()
            if not result:
                print(f"Could not find order for: {parameter}")
                logging.warning(f"Could not find order for: {parameter}")
            else:
                for order in result:
                    print(f"\nOrder #: {order[0]} | Product #: {order[1]} | Order Date: {order[2]} | Order Quantity: {order[3]}\n")

    @staticmethod
    def get_all_orders():
        Order.execute_and_print("SELECT * FROM orders", None)

    @staticmethod
    def get_order_by_product(product):
        Order.execute_and_print("SELECT * FROM orders WHERE product_id = %s", (product,))