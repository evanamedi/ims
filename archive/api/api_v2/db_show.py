from database.db_utils import db_cursor
from mysql.connector import ProgrammingError

def show_database():    # Fetch and return all tables in database
    with db_cursor() as cursor:
        cursor.execute("SHOW TABLES;")
        result = cursor.fetchall()
    return result

def show_table(table_name: str):    # Fetch and return all rows from specified table
    try:
        with db_cursor() as cursor:
            cursor.execute(f"SELECT * FROM {table_name};")
            result = cursor.fetchall()
        return result
    except ProgrammingError:
        return f"Error: The table '{table_name}' does not exist.\n"