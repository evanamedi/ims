from flask import Flask, render_template
from flask_cors import CORS
from api.register_blueprints import register_blueprints
from template_data.input_fields_data import suppliers_form_list, products_form_list, customers_form_list, orders_form_list, sales_form_list


app = Flask(__name__)
CORS(app)
# CORS(app, origins=["http://localhost:5000", "http://example.com"]) this is for production environment
register_blueprints(app)

@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/suppliers")
def suppliers():
    return render_template("suppliers.html", form_list=suppliers_form_list)

@app.route("/products")
def products():
    return render_template("products.html", form_list=products_form_list)

@app.route("/customers")
def customers():
    return render_template("customers.html", form_list=customers_form_list)

@app.route("/orders")
def orders():
    return render_template("orders.html", form_list=orders_form_list)

@app.route("/sales")
def sales():
    return render_template("sales.html", form_list=sales_form_list)

if __name__ =="__main__":
    app.run(debug=True, port=8000)