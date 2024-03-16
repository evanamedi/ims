from flask import Flask
from flask_cors import CORS
from api.supplier_route import supplier_routes
from api.products_route import product_routes

app = Flask(__name__)
CORS(app)
# CORS(app, origins=["http://localhost:5000", "http://example.com"]) this is for production environment
app.register_blueprint(supplier_routes)
app.register_blueprint(product_routes)

@app.route("/supplier")
def supplier_page():
    print(app.static_folder)
    return app.send_static_file("supplier.html")

@app.route("/product")
def product_page():
    print(app.static_folder)
    return app.send_static_file("product.html")

if __name__ =="__main__":
    app.run(debug=True)