from logger import configure_logger
from api.api_utils import format_response
from flask import Blueprint, request, url_for
from suppliers.suppliers import Supplier


api_logger = configure_logger(__name__, True)
supplier_routes = Blueprint("supplier_routes", __name__)

# CREATE NEW SUPPLIER
@supplier_routes.route("/v1/supplier", methods=["POST"])
def add_supplier():
    data = request.get_json()
    required_fields = ["supplier_name", "supplier_address", "supplier_contact"]
    
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        api_logger.error(f"Missing required fields: {','.join(missing_fields)}")
        return format_response(400, f"Missing required fields: {','.join(missing_fields)}")

    new_supplier = Supplier(data["supplier_name"], data["supplier_address"], data["supplier_contact"])
    try:
        new_supplier.save_to_db()
        response = format_response(201, "Supplier added successfully", new_supplier.to_dict())
        response.headers["location"] = url_for("supplier_routes.get_supplier", supplier_id=new_supplier.id, _external=True)
        return response
    except Exception as e:
        api_logger.error(f"Failed to add supplier: {e}")
        return format_response(400, str(e))




@supplier_routes.route("/v1/supplier/<int:supplier_id>", methods=["GET"])
def get_supplier(supplier_id):
    supplier = Supplier.find_by_id(supplier_id)
    if supplier is None:
        return format_response(400, "Supplier Not Found")
    return format_response(200, "Supplier retrieved successfully", supplier.to_dict())





# GET INFORMATION
@supplier_routes.route("/v1/supplier/name/<string:name>", methods=["GET"])
def get_supplier_by_name(name):
    try:
        suppliers = Supplier.get_supplier_by_name(name)
        suppliers_dict = [supplier.to_dict() for supplier in suppliers]
        return format_response(200, "Supplier retrieved successfully", suppliers_dict)
    except Exception as e:
        api_logger.error(f"Failed to retrieve supplier: {e}")
        return format_response(500, str(e))

@supplier_routes.route("/v1/supplier/all", methods=["GET"])
def get_all_supplier():
    try:
        suppliers = Supplier.get_all_suppliers()
        suppliers_dict = [supplier.to_dict() for supplier in suppliers]
        return format_response(200, "Suppliers retrieved successfully", suppliers_dict)
    except Exception as e:
        api_logger.error(f"Failed to retrieve suppliers: {e}")
        return format_response(500, str(e))





# UPDATING
@supplier_routes.route("/v1/supplier/<int:id>/<string:field>", methods=["PUT"])
def update_supplier_field(id, field):
    new_value = request.json.get("new_value")
    supplier = Supplier.find_by_id(id)
    if supplier:
        if field in ["name", "address", "contact"]:
            supplier.update_field(field, new_value)
            return format_response(200, f"Supplier {field} updated successfully", supplier.to_dict())
        else:
            return format_response(400, f"Invalid field: {field}")
    else:
        return format_response(400, "Supplier not found")