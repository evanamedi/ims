from api.api_utils import format_response
from flask import Blueprint, request
from logic.database_logic import Table
from logger import configure_logger

logger = configure_logger()
supplier_routes_v2 = Blueprint("supplier_routes_v2", __name__)

# save_to_db
@supplier_routes_v2.route("/v2/supplier/add", methods=["POST"])
def add_supplier():
    try:
        data = request.get_json()
        required_fields = ["supplier_name", "supplier_address", "supplier_contact"]
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            logger.error(f"Missing required fields: {','.join(missing_fields)}")
            return format_response(400, f"Missing required fields: {','.join(missing_fields)}")
        new_supplier = Table('suppliers', **data)
        new_supplier.save_to_db()
    except ValueError as e:
        logger.error(str(e))
        return format_response(400, str(e))
    logger.info("Supplier Added Successfully")
    return format_response(200, "Supplier Added Successfully")

# read_id_from_db()
@supplier_routes_v2.route("/v2/supplier/<int:supplier_id>", methods=["GET"])
def get_supplier_by_id(supplier_id):
    try:
        supplier_table = Table("suppliers")
        data = supplier_table.read_id_from_db(supplier_id)
        if not data:
            logger.error("Supplier Not Found")
            return format_response(400, "Supplier Not found")
    except ValueError as e:
        logger.error(str(e))
        return format_response(400, str(e))
    logger.info("Supplier Retrieved Successfully")
    return format_response(200, "Supplier Retrieved Successfully", data)

# delete_from_db()
@supplier_routes_v2.route("/v2/supplier/delete/<int:supplier_id>", methods=["DELETE"])
def delete_supplier(supplier_id):
    try:
        supplier_table = Table("suppliers")
        data = supplier_table.delete_from_db(supplier_id)
        if not data:
            logger.error("Supplier Not Found")
            return format_response(400, "Supplier Not Found")
    except ValueError as e:
        logger.error(str(e))
        return format_response(400, str(e))
    logger.info("Supplier Deleted Successfully")
    return format_response(200, "Supplier Deleted Successfully")

# update_field_in_db()
@supplier_routes_v2.route("/v2/supplier/update/<int:supplier_id>/<string:field>", methods=["PUT"])
def update_supplier_field(supplier_id, field):
    try:
        supplier_table = Table("suppliers")
        data = request.get_json()
        if data is None:
            logger.error("Missing Data")
            return format_response(400, "Missing Data In Request Body")
        supplier_table.update_field_in_db(supplier_id, field, data[field])
    except ValueError as e:
        logger.error(str(e))
        return format_response(400, str(e))
    logger.info("Field Updated Successfully")
    return format_response(200, "Field Updated Successfully")

# select_all_from_db()
@supplier_routes_v2.route("/v2/supplier/all", methods=["GET"])
def get_all_suppliers():
    supplier_table = Table("suppliers")
    all_suppliers = supplier_table.select_all_from_db()
    if not all_suppliers:
        logger.error("No Suppliers In Database")
        return format_response(400, "No Suppliers In Database")
    logger.info("All Suppliers Successfully Retrieved")
    return format_response(200, "All Suppliers Successfully Retrieved", all_suppliers)

# count_rows_in_db()
@supplier_routes_v2.route("/v2/supplier/count", methods=["GET"])
def get_supplier_count():
    supplier_table = Table("suppliers")
    supplier_count = supplier_table.count_rows_in_db()
    if not supplier_count:
        logger.error("No Suppliers In Database")
        return format_response(400, "No Suppliers In Database")
    logger.info("Supplier Count Retrieved Successfully")
    return format_response(200, "Supplier Count Retrieved Successfully", supplier_count)

# select_row_by_field()
# @supplier_routes_v2.route("/v2/supplier/select/<string:field>/<string:value>", methods=["GET"])
# def get_all_suppliers_by_field(field, value):
#     try:
#         supplier_table = Table("suppliers")
#         data = supplier_table.select_row_by_field(field, value)
#         if not data:
#             logger.error("Field or Value not found")
#             return format_response(400, "Field or Value Not Found")
#     except ValueError as e:
#         logger.error(str(e))
#         return format_response(400, str(e))
#     logger.info("Selected Rows Returned")
#     return format_response(200, "Selected Rows Returned", data)