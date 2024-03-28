from api.api_utils import format_response
from flask import Blueprint, request
from logic.database_logic import Table
from logger import configure_logger

logger = configure_logger()
customer_routes_v2 = Blueprint("customer_routes_v2", __name__)

# save_to_db
@customer_routes_v2.route("/v2/customer/add", methods=["POST"])
def add_customer():
    try:
        data = request.get_json()
        required_fields = ["customer_name", "customer_address", "customer_contact"]
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            logger.error(f"Missing required fields: {','.join(missing_fields)}")
            return format_response(400, f"Missing required fields: {','.join(missing_fields)}")
        new_customer = Table('customers', **data)
        new_customer.save_to_db()
    except ValueError as e:
        logger.error(str(e))
        return format_response(400, str(e))
    logger.info("Customer Added Successfully")
    return format_response(200, "Customer Added Successfully")

# read_id_from_db()
@customer_routes_v2.route("/v2/customer/get/<int:customer_id>", methods=["GET"])
def get_customer_by_id(customer_id):
    try:
        customer_table = Table("customers")
        data = customer_table.read_id_from_db(customer_id)
        if not data:
            logger.error("Customer Not Found")
            return format_response(400, "Customer Not found")
    except ValueError as e:
        logger.error(str(e))
        return format_response(400, str(e))
    logger.info("Customer Retrieved Successfully")
    return format_response(200, "Customer Retrieved Successfully", data)

# delete_from_db()
@customer_routes_v2.route("/v2/customer/delete/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    try:
        customer_table = Table("customers")
        customer_table.delete_from_db(customer_id)
    except ValueError as e:
        logger.error(str(e))
        return format_response(400, str(e))
    logger.info("Customer Deleted Successfully")
    return format_response(200, "Customer Deleted Successfully")

# update_field_in_db()
@customer_routes_v2.route("/v2/customer/update/<int:customer_id>/<string:field>", methods=["PUT"])
def update_customer_field(customer_id, field):
    try:
        customer_table = Table("customers")
        data = request.get_json()
        if data is None:
            logger.error("Missing Data")
            return format_response(400, "Missing Data In Request Body")
        customer_table.update_field_in_db(customer_id, field, data[field])
    except ValueError as e:
        logger.error(str(e))
        return format_response(400, str(e))
    logger.info("Field Updated Successfully")
    return format_response(200, "Field Updated Successfully")

# select_all_from_db()
@customer_routes_v2.route("/v2/customer/all", methods=["GET"])
def get_all_customers():
    customer_table = Table("customers")
    all_customers = customer_table.select_all_from_db()
    if not all_customers:
        logger.error("No Customers In Database")
        return format_response(400, "No Customers In Database")
    logger.info("All Customers Successfully Retrieved")
    return format_response(200,  ("customers", "Successfully Retrieved"), all_customers)

# count_rows_in_db()
@customer_routes_v2.route("/v2/customer/count", methods=["GET"])
def get_customer_count():
    customer_table = Table("customers")
    customer_count = customer_table.count_rows_in_db()
    if not customer_count:
        logger.error("No Customers In Database")
        return format_response(400, "No Customers In Database")
    logger.info("Customer Count Retrieved Successfully")
    return format_response(200, "Customer Count Retrieved Successfully", customer_count)

# # select_row_by_field()
# @customer_routes_v2.route("/v2/customer/select/<string:field>/<string:value>", methods=["GET"])
# def get_all_customers_by_field(field, value):
#     try:
#         customer_table = Table("customers")
#         data = customer_table.select_row_by_field(field, value)
#         if not data:
#             logger.error("Field or Value not found")
#             return format_response(400, "Field or Value Not Found")
#     except ValueError as e:
#         logger.error(str(e))
#         return format_response(400, str(e))
#     logger.info("Selected Rows Returned")
#     return format_response(200, "Selected Rows Returned", data)
