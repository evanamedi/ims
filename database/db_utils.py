from contextlib import contextmanager
from database.db import create_connection

@contextmanager
def db_cursor():
    cnx = create_connection()
    cursor = cnx.cursor()
    try:
        yield cursor
        cnx.commit() # commit transaction
    except Exception as e:
        cnx.rollback() # roll back transaction in case of error
        raise e # re-raise exception
    finally:
        cursor.close()
        cnx.close()
        