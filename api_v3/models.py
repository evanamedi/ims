from flask_sqlalchemy import SQLAlchemy
from api_v3.database import db


class Supplier(db.Model):
    __tablename__ = 'suppliers'
    
    id = db.Column(db.Integer, primary_key=True)
    supplier_name = db.Column(db.String)
    supplier_address = db.Column(db.String)
    supplier_contact = db.Column(db.String)
    products = db.relationship('Product', backref='supplier')

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.id'))
    product_name = db.Column(db.String)
    product_description = db.Column(db.String)
    product_price = db.Column(db.Integer)
    product_quantity = db.Column(db.Integer)
    orders = db.relationship('Order', backref='product')
    sales = db.relationship('Sale', backref='product')

class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String)
    customer_address = db.Column(db.String)
    customer_contact = db.Column(db.Integer)
    orders = db.relationship('Order', backref='Customer')
    sales = db.relationship('Sale', backref='Customer')

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    order_date = db.Column(db.Integer)
    order_quantity = db.Column(db.Integer)

class Sale(db.Model):
    __tablename__ = 'sales'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    sale_date = db.Column(db.Integer)
    sale_quantity = db.Column(db.Integer)