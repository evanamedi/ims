from flask import Flask, render_template
from flask_cors import CORS
from api.register_blueprints import register_blueprints


app = Flask(__name__)
CORS(app)
# CORS(app, origins=["http://localhost:5000", "http://example.com"]) this is for production environment
register_blueprints(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/suppliers")
def suppliers():
    return render_template("supplier.html")

@app.route("/products")
def products():
    return render_template("product.html")

@app.route("/test")
def test():
    return render_template('test_html.html')

if __name__ =="__main__":
    app.run(debug=True, port=8000)