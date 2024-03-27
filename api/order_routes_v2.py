from api.api_utils import format_response
from flask import Blueprint, request
from logic.database_logic import Table
from logger import configure_logger

logger = configure_logger()
order_routes_v2 = Blueprint("order_routes_v2", __name__)

# save_to_db
@order_routes_v2.route("/v2/order/add", methods=["POST"])
def add_order():
    try:
        data = request.get_json()
        required_fields = ["product_id", "customer_id", "order_date", "order_quantity"]
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            logger.error(f"Missing required fields: {','.join(missing_fields)}")
            return format_response(400, f"Missing required fields: {','.join(missing_fields)}")
        new_order = Table('orders', **data)
        new_order.save_to_db()
    except ValueError as e:
        logger.error(str(e))
        return format_response(400, str(e))
    logger.info("Order Added Successfully")
    return format_response(200, "Order Added Successfully")

# read_id_from_db()
@order_routes_v2.route("/v2/order/get/<int:order_id>", methods=["GET"])
def get_order_by_id(order_id):
    try:
        order_table = Table("orders")
        data = order_table.read_id_from_db(order_id)
        if not data:
            logger.error("Order Not Found")
            return format_response(400, "Order Not found")
    except ValueError as e:
        logger.error(str(e))
        return format_response(400, str(e))
    logger.info("Order Retrieved Successfully")
    return format_response(200, "Order Retrieved Successfully", data)

# delete_from_db()
@order_routes_v2.route("/v2/order/delete/<int:order_id>", methods=["DELETE"])
def delete_order(order_id):
    try:
        order_table = Table("orders")
        order_table.delete_from_db(order_id)
    except ValueError as e:
        logger.error(str(e))
        return format_response(400, str(e))
    logger.info("Order Deleted Successfully")
    return format_response(200, "Order Deleted Successfully")

# update_field_in_db()
@order_routes_v2.route("/v2/order/update/<int:order_id>/<string:field>", methods=["PUT"])
def update_order_field(order_id, field):
    try:
        order_table = Table("orders")
        data = request.get_json()
        if data is None:
            logger.error("Missing Data")
            return format_response(400, "Missing Data In Request Body")
        order_table.update_field_in_db(order_id, field, data[field])
    except ValueError as e:
        logger.error(str(e))
        return format_response(400, str(e))
    logger.info("Field Updated Successfully")
    return format_response(200, "Field Updated Successfully")

# select_all_from_db()
@order_routes_v2.route("/v2/order/all", methods=["GET"])
def get_all_orders():
    order_table = Table("orders")
    all_orders = order_table.select_all_from_db()
    if not all_orders:
        logger.error("No Orders In Database")
        return format_response(400, "No Orders In Database")
    logger.info("All Orders Successfully Retrieved")
    return format_response(200, "All Orders Successfully Retrieved", all_orders)

# count_rows_in_db()
@order_routes_v2.route("/v2/order/count", methods=["GET"])
def get_order_count():
    order_table = Table("orders")
    order_count = order_table.count_rows_in_db()
    if not order_count:
        logger.error("No Orders In Database")
        return format_response(400, "No Orders In Database")
    logger.info("Order Count Retrieved Successfully")
    return format_response(200, "Order Count Retrieved Successfully", order_count)

# # select_row_by_field()
# @order_routes_v2.route("/v2/order/select/<string:field>/<string:value>", methods=["GET"])
# def get_all_orders_by_field(field, value):
#     try:
#         order_table = Table("orders")
#         data = order_table.select_row_by_field(field, value)
#         if not data:
#             logger.error("Field or Value not found")
#             return format_response(400, "Field or Value Not Found")
#     except ValueError as e:
#         logger.error(str(e))
#         return format_response(400, str(e))
#     logger.info("Selected Rows Returned")
#     return format_response(200, "Selected Rows Returned", data)
