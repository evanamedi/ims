from api.api_utils import format_response
from flask import Blueprint, request
from logic.database_logic import Table
from logger import configure_logger

logger = configure_logger()
sale_routes_v2 = Blueprint("sale_routes_v2", __name__)

# save_to_db
@sale_routes_v2.route("/v2/sale", methods=["POST"])
def add_sale():
    try:
        data = request.get_json()
        required_fields = ["product_id", "customer_id", "sale_date", "sale_quantity"]
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            logger.error(f"Missing required fields: {','.join(missing_fields)}")
            return format_response(400, f"Missing required fields: {','.join(missing_fields)}")
        new_sale = Table('sales', **data)
        new_sale.save_to_db()
    except ValueError as e:
        logger.error(str(e))
        return format_response(400, str(e))
    logger.info("Sale Added Successfully")
    return format_response(200, "Sale Added Successfully")

# read_id_from_db()
@sale_routes_v2.route("/v2/sale/<int:sale_id>", methods=["GET"])
def get_sale_by_id(sale_id):
    try:
        sale_table = Table("sales")
        data = sale_table.read_id_from_db(sale_id)
        if not data:
            logger.error("Sale Not Found")
            return format_response(400, "Sale Not found")
    except ValueError as e:
        logger.error(str(e))
        return format_response(400, str(e))
    logger.info("Sale Retrieved Successfully")
    return format_response(200, "Sale Retrieved Successfully", data)

# delete_from_db()
@sale_routes_v2.route("/v2/sale/delete/<int:sale_id>", methods=["DELETE"])
def delete_sale(sale_id):
    try:
        sale_table = Table("sales")
        data = sale_table.delete_from_db(sale_id)
        if not data:
            logger.error("Sale Not Found")
            return format_response(400, "Sale Not Found")
    except ValueError as e:
        logger.error(str(e))
        return format_response(400, str(e))
    logger.info("Sale Deleted Successfully")
    return format_response(200, "Sale Deleted Successfully")

# update_field_in_db()
@sale_routes_v2.route("/v2/sale/update/<int:sale_id>/<string:field>", methods=["PUT"])
def update_sale_field(sale_id, field):
    try:
        sale_table = Table("sales")
        data = request.get_json()
        if data is None:
            logger.error("Missing Data")
            return format_response(400, "Missing Data In Request Body")
        sale_table.update_field_in_db(sale_id, field, data[field])
    except ValueError as e:
        logger.error(str(e))
        return format_response(400, str(e))
    logger.info("Field Updated Successfully")
    return format_response(200, "Field Updated Successfully")

# select_all_from_db()
@sale_routes_v2.route("/v2/sale/all", methods=["GET"])
def get_all_sales():
    sale_table = Table("sales")
    all_sales = sale_table.select_all_from_db()
    if not all_sales:
        logger.error("No Sales In Database")
        return format_response(400, "No Sales In Database")
    logger.info("All Sales Successfully Retrieved")
    return format_response(200, "All Sales Successfully Retrieved", all_sales)

# count_rows_in_db()
@sale_routes_v2.route("/v2/sale/sale_count", methods=["GET"])
def get_sale_count():
    sale_table = Table("sales")
    sale_count = sale_table.count_rows_in_db()
    if not sale_count:
        logger.error("No Sales In Database")
        return format_response(400, "No Sales In Database")
    logger.info("Sale Count Retrieved Successfully")
    return format_response(200, "Sale Count Retrieved Successfully", sale_count)

# select_row_by_field()
@sale_routes_v2.route("/v2/sale/select/<string:field>/<string:value>", methods=["GET"])
def get_all_sales_by_field(field, value):
    try:
        sale_table = Table("sales")
        data = sale_table.select_row_by_field(field, value)
        if not data:
            logger.error("Field or Value not found")
            return format_response(400, "Field or Value Not Found")
    except ValueError as e:
        logger.error(str(e))
        return format_response(400, str(e))
    logger.info("Selected Rows Returned")
    return format_response(200, "Selected Rows Returned", data)
