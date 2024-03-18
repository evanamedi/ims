from flask import Flask, render_template
from flask_cors import CORS
from api.supplier_route import supplier_routes
from api.products_route import product_routes

app = Flask(__name__)
CORS(app)
# CORS(app, origins=["http://localhost:5000", "http://example.com"]) this is for production environment
app.register_blueprint(supplier_routes)
app.register_blueprint(product_routes)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/suppliers")
def suppliers():
    return render_template("supplier.html")

@app.route("/products")
def products():
    return render_template("product.html")

if __name__ =="__main__":
    app.run(debug=True)