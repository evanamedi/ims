from database.db_utils import db_cursor
import mysql.connector as db
from logger import configure_logger
"""
This class is used to interact with the database for all tables. 
Any changes or additions to this class will apply to all tables listed in SCHEMAS.
If any tables are added or deleted from the database, they must be reflected in the dict below.
As seen in __init__ (**kwargs) this is designed to be flexible and be a single point of access for all database commands.
"""

logger = configure_logger()

# Table entry point
class Table:
    SCHEMAS = {
        'suppliers': ["id", "supplier_name", "supplier_address", "supplier_contact"],
        'products': ["id", "supplier_id", "product_name", "product_description", "product_price", "product_quantity"],
        'orders': ["id", "product_id", "order_date", "order_quantity"],
        'customers': ["id", "customer_id", "customer_address", "customer_contact"],
        'sales': ["id", "product_id", "customer_id", "sale_date", "sale_quantity"]
        
    }

    def __init__(self, table_name, **kwargs):
        self.table_name = table_name
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):  # Converts instance variables (excluding "table_name") into to a dict. This preps the data for the SQL queries
        return {key: getattr(self, key) for key in vars(self) if key != 'table_name'}

    def save_to_db(self):   # Create a new row in the table
        try:
            data = self.to_dict()
            columns = ', '.join(data.keys())
            placeholders = ', '.join(['%s'] * len(data))
            query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
            with db_cursor() as cursor:
                cursor.execute(query, list(data.values()))
                logger.info("Added Successfully")
        except db.Error as e:
            logger.error(f"Error Saving To Database: {e}")
            raise

    def delete_from_db(self, id):   # Delete a row from the table
        try:
            query = f"DELETE FROM {self.table_name} WHERE id = %s"
            with db_cursor() as cursor:
                cursor.execute(query, (id,))
                logger.info("Deleted Successfully")
        except db.Error as e:
            logger.error(f"Error Deleting from Database: {e}")
            raise

    def read_id_from_db(self, id):     # Retrieve a row by ID
        try:
            query = f"SELECT * FROM {self.table_name} WHERE id = %s"
            with db_cursor() as cursor:
                cursor.execute(query, (id,))
                logger.info("ID Retrieved Successfully")
                return cursor.fetchall()
        except db.Error as e:
            logger.error(f"Error Retrieving ID: {e}")
            raise

    def update_field_in_db(self, id, field, new_value):     # Update any field in the row
        try:
            if field not in self.SCHEMAS[self.table_name]:
                raise ValueError(f"Invalid field: {field}")
            query = f"UPDATE {self.table_name} SET {field} = %s WHERE id = %s"
            with db_cursor() as cursor:
                cursor.execute(query, (new_value, id))
                logger.info("Field Updated Successfully")
        except db.Error as e:
            logger.error(f"Error Updating Field: {e}")
            raise

    def select_all_from_db(self):   # Select all rows from a table
        try:
            query = f"SELECT * FROM {self.table_name}"
            with db_cursor() as cursor:
                cursor.execute(query)
                logger.info("Rows Retrieved Successfully")
                return cursor.fetchall()
        except db.Error as e:
            logger.error(f"Error Retrieving Rows: {e}")
            raise

    def count_rows_in_db(self):  # Count how many rows in a table
        try:
            query = f"SELECT COUNT(*) FROM {self.table_name}"
            with db_cursor() as cursor:
                cursor.execute(query)
                logger.info("Rows Retrieved Successfully")
                return cursor.fetchall()[0]
        except db.Error as e:
            logger.error(f"Error Retrieving Rows: {e}")
            raise

    def select_row_by_field(self, field, value):    # Select all records in table where specified field matches given value
        try:
            if field not in self.SCHEMAS[self.table_name]:
                raise ValueError(f"Invalid field: {field}")
            query = f"SELECT * FROM {self.table_name} WHERE {field} = %s"
            with db_cursor() as cursor:
                cursor.execute(query, (value,))
                logger.info("Records Retrieved Successfully")
                return cursor.fetchall()
        except db.Error as e:
            logger.error(f"Error Selecting Records: {e}")