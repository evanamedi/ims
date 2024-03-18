from database.db_utils import db_cursor
import mysql.connector as db
from logger import configure_logger

app_logger = configure_logger(__name__, "app.log")

class Product:
    def __init__(self, supplier_id, product_name, product_description, product_price, product_quantity, id = None):
        self.id = id
        self.supplier_id = supplier_id
        self.product_name = product_name
        self.product_description = product_description
        self.product_price = product_price
        self.product_quantity = product_quantity

    def to_dict(self):
        return {
            "id": self.id,
            "supplier_id": self.supplier_id,
            "product_name": self.product_name,
            "product_description": self.product_description,
            "product_price": self.product_price,
            "product_quantity": self.product_quantity
        }

    def save_to_db(self):
        if not self.supplier_id or not self.product_name or not self.product_description or not self.product_price or not self.product_quantity:
            app_logger.warning("Insufficient Data for Adding Product")
            raise ValueError("Supplier #, Product Name, Description, Price, and Quantity must not be empty")

        with db_cursor() as cursor:
            try:
                if self.id is None:
                    cursor.execute(
                        "INSERT INTO products (supplier_id, product_name, product_description, product_price, product_quantity) VALUES (%s, %s, %s, %s, %s)",
                        (self.supplier_id, self.product_name, self.product_description, self.product_price, self.product_quantity)
                    )
                    self.id = cursor.lastrowid
                    print("Product Added Successfully\n")
                    app_logger.info("Product Added Successfully")
            except db.Error as e:
                print(f"Database Error: {e}")
                app_logger.error(f"Database Error {e}")


    def update_field(self, field, value):
        field_mapping = {
            "name": "product_name",
            "description": "product_description",
            "price": "product_price",
            "quantity": "product_quantity"
        }

        db_field = field_mapping.get(field)
        if db_field is None:
            raise ValueError(f"Invalid field: {field}")

        with db_cursor() as cursor:
            try:
                cursor.execute(
                    f"UPDATE products SET {db_field} = %s WHERE id = %s",
                    (value, self.id)
                )
                setattr(self, db_field, value)
                print(f"\n{field.capitalize} Updated Successfully\n")
                app_logger.info(f"{field.capitalize} Updated Successfully")
            except db.Error as e:
                print(f"Database Error: {e}")
                app_logger.error(f"Database Error {e}")

    def update_name(self, new_name):
        self.update_field("name", new_name)

    def update_info(self, new_description):
        self.update_field("description", new_description)

    def update_price(self, new_price):
        self.update_field("price", new_price)

    def update_quantity(self, new_quantity):
        self.update_field("quantity", new_quantity)


    @staticmethod
    def execute_and_print(query, parameter):
        with db_cursor() as cursor:
            cursor.execute(query, parameter)
            result = cursor.fetchall()
            products = []
            if not result:
                print(f"Product Not Found: {parameter}")
                app_logger.warning(f"Product Not Found {parameter}")
            else:
                for product in result:
                    print(f"\nID: {product[0]} | Supplier ID: {product[1]} | Product Name: {product[2]} | Product Description: {product[3]} | Product Price: {product[4]} | Product Quantity: {product[5]}\n")
                    products.append(Product(product[1], product[2], product[3], product[4], product[5], product[0]))
            return products

    @staticmethod
    def get_all_products():
        return Product.execute_and_print("SELECT * FROM products", None)

    @staticmethod
    def get_product_by_name(name):
        return Product.execute_and_print("SELECT * FROM products WHERE product_name LIKE %s", ("%" + name + "%", ))

    @staticmethod
    def find_by_id(product_id):
        result = Product.execute_and_print("SELECT * FROM products WHERE id = %s", (product_id,))
        return result[0] if result else None

    @staticmethod
    def get_products_by_supplier(supplier_id):
        return Product.execute_and_print("SELECT * FROM products WHERE supplier_id = %s", (supplier_id,))

    @staticmethod
    def delete_product(product_id):
        with db_cursor() as cursor:
            cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
            return cursor.rowcount