import argparse
from factory import create_app
from flask import Flask, render_template
from api_v3.database import db

from template_data.input_fields_data import suppliers_form_list, products_form_list, customers_form_list, orders_form_list, sales_form_list

app = create_app()

@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/suppliers")
def suppliers():
    return render_template("suppliers.html", form_list=suppliers_form_list, pageName=suppliers_form_list[0])

@app.route("/products")
def products():
    return render_template("products.html", form_list=products_form_list, pageName=products_form_list[0])

@app.route("/customers")
def customers():
    return render_template("customers.html", form_list=customers_form_list, pageName=customers_form_list[0])

@app.route("/orders")
def orders():
    return render_template("orders.html", form_list=orders_form_list, pageName=orders_form_list[0])

@app.route("/sales")
def sales():
    return render_template("sales.html", form_list=sales_form_list, pageName=sales_form_list[0])

if __name__ =="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--local', action='store_true', help='Run server locally')
    args = parser.parse_args()
    
    with app.app_context():
        db.create_all()
    
    if args.local:
        app.run(host='0.0.0.0', debug=True, port=8000)
    else:
        app.run(debug=True, port=8000)

