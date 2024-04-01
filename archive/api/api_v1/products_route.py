from archive.python.logger import configure_logger
from api.api_utils import format_response
from flask import Blueprint, request, url_for
from logic.products.products import Product

api_logger = configure_logger(__name__, "app.log")
product_routes = Blueprint("product_routes", __name__)

# CREATE NEW PRODUCT
@product_routes.route("/v1/product", methods=["POST"])
def add_product():
    data = request.get_json()
    required_fields = ["supplier_id", "product_name", "product_description", "product_price", "product_quantity"]
    
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        api_logger.error(f"Missing required fields: {','.join(missing_fields)}")
        return format_response(400, f"Missing required fields: {','.join(missing_fields)}")

    new_product = Product(data["supplier_id"], data["product_name"], data["product_description"], data["product_price"], data["product_quantity"])
    try:
        new_product.save_to_db()
        response = format_response(201, "Product added successfully", new_product.to_dict())
        response.headers["location"] = url_for("product_routes.get_product", product_id=new_product.id, _external=True)
        return response
    except Exception as e:
        api_logger.error(f"Faild to Add Product: {e}")
        return format_response(400, str(e))





@product_routes.route("/v1/product/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = Product.find_by_id(product_id)
    if product is None:
        return format_response(400, "Product Not Found")
    return format_response(200, "Product Retrieved Successfully", product.to_dict())





# DELETE PRODUCT
@product_routes.route("/v1/product/delete/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    rows_deleted = Product.delete_product(product_id)
    if rows_deleted == 0:
        return format_response(400, "Product Not Found")
    return format_response(200, "Product Deleted Successfully")





# GET INFORMATION
@product_routes.route("/v1/product/supplier/<int:id>", methods=["GET"])
def get_product_buy_supplier(id):
    try:
        products = Product.get_products_by_supplier(id)
        products_dict = [product.to_dict() for product in products]
        return format_response(200, "Product Retrieve Successfully", products_dict)
    except Exception as e:
        api_logger.error(f"Failed to retrieve Products: {e}")
        return format_response(500, str(e))

@product_routes.route("/v1/product/name/<string:name>", methods=["GET"])
def get_product_by_name(name):
    try:
        products = Product.get_product_by_name(name)
        products_dict = [product.to_dict() for product in products]
        return format_response(200, "Product Retrieved Successfully", products_dict)
    except Exception as e:
        api_logger.error(f"Failed to Retrieve Product: {e}")
        return format_response(500, str(e))

@product_routes.route("/v1/product/all", methods=["GET"])
def get_all_products():
    try:
        products = Product.get_all_products()
        products_dict = [product.to_dict() for product in products]
        return format_response(200, "Products Retrieved Successfully", products_dict)
    except Exception as e:
        api_logger.error(f"Failed to Retrieve Products: {e}")
        return format_response(500, str(e))





# UPDATING
@product_routes.route("/v1/product/<int:id>/<string:field>", methods=["PUT"])
def update_product_field(id, field):
    new_value = request.json.get("new_value")
    product = Product.find_by_id(id)
    if product:
        if field in ["name", "description", "price", "quantity"]:
            product.update_field(field, new_value)
            return format_response(200, f"Product {field} Updated Successfully", product.to_dict())
        else:
            return format_response(400, f"Invalid Field: {field}")
    else:
        return format_response(400, "Product not found")