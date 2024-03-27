from api.api_utils import format_response
from flask import Blueprint, request
from logic.database_logic import Table
from logger import configure_logger

logger = configure_logger()
product_routes_v2 = Blueprint("product_routes_v2", __name__)

#save_to_db
@product_routes_v2.route("/v2/product/add", methods=["POST"])
def add_product():
    try:
        data = request.get_json()
        required_fields = ["supplier_id", "product_name", "product_description", "product_price", "product_quantity"]
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            logger.error(f"Missing required fields: {','.join(missing_fields)}")
            return format_response(400, f"Missing required fields: {','.join(missing_fields)}")
        new_product = Table('products', **data)
        new_product.save_to_db()
    except ValueError as e:
        logger.error(str(e))
        return format_response(400, str(e))
    logger.info("Product Added Successfully")
    return format_response(200, "Product Added Successfully")

# read_id_from_db()
@product_routes_v2.route("/v2/product/get/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id):
    try:
        product_table = Table("products")
        data = product_table.read_id_from_db(product_id)
        if not data:
            logger.error("Product Not Found")
            return format_response(400, "Product Not found")
    except ValueError as e:
        logger.error(str(e))
        return format_response(400, str(e))
    logger.info("Product Retrieved Successfully")
    return format_response(200, "Product Retrieved Successfully", data)

# delete_from_db()
@product_routes_v2.route("/v2/product/delete/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    try:
        product_table = Table("products")
        data = product_table.delete_from_db(product_id)
        if not data:
            logger.error("Product Not Found")
            return format_response(400, "Product Not Found")
    except ValueError as e:
        logger.error(str(e))
        return format_response(400, str(e))
    logger.info("Product Deleted Successfully")
    return format_response(200, "Product Deleted Successfully")

# update_field_in_db()
@product_routes_v2.route("/v2/product/update/<int:product_id>/<string:field>", methods=["PUT"])
def update_product_field(product_id, field):
    try:
        product_table = Table("products")
        data = request.get_json()
        if data is None:
            logger.error("Missing Data")
            return format_response(400, "Missing Data In Request Body")
        product_table.update_field_in_db(product_id, field, data[field])
    except ValueError as e:
        logger.error(str(e))
        return format_response(400, str(e))
    logger.info("Field Updated Successfully")
    return format_response(200, "Field Updated Successfully")

# select_all_from_db()
@product_routes_v2.route("/v2/product/all", methods=["GET"])
def get_all_products():
    product_table = Table("products")
    all_products = product_table.select_all_from_db()
    if not all_products:
        logger.error("No Products In Database")
        return format_response(400, "No Products In Database")
    logger.info("All Products Successfully Retrieved")
    return format_response(200, "All Products Successfully Retrieved", all_products)

# count_rows_in_db()
@product_routes_v2.route("/v2/product/count", methods=["GET"])
def get_product_count():
    product_table = Table("products")
    product_count = product_table.count_rows_in_db()
    if not product_count:
        logger.error("No Products In Database")
        return format_response(400, "No Products In Database")
    logger.info("Product Count Retrieved Successfully")
    return format_response(200, "Product Count Retrieved Successfully", product_count)

# # select_row_by_field()
# @product_routes_v2.route("/v2/product/select/<string:field>/<string:value>", methods=["GET"])
# def get_all_products_by_field(field, value):
#     try:
#         product_table = Table("products")
#         data = product_table.select_row_by_field(field, value)
#         if not data:
#             logger.error("Field or Value not found")
#             return format_response(400, "Field or Value Not Found")
#     except ValueError as e:
#         logger.error(str(e))
#         return format_response(400, str(e))
#     logger.info("Selected Rows Returned")
#     return format_response(200, "Selected Rows Returned", data)
