from base import Session
from suppliers import Supplier, Product, Customer, Order, Sale

session = Session()

def save_to_db(instance):
    session.add(instance)
    session.commit()

def delete_from_db(instance):
    session.delete(instance)
    session.commit()

def read_id_from_db(cls, id):
    return session.query(cls).get(id)

def update_field_in_db(instance, field, new_value):
    setattr(instance, field, new_value)
    session.commit()

def select_all_from_db(cls):
    return session.query(cls).all()

def count_rows_in_db(cls):
    return session.query(cls).count()

def select_row_by_field(cls, field, value):
    return session.query(cls).filter(getattr(cls, field) == value).all()