from flask import Blueprint
from flask_restful import Api
from api_v3_resources.supplier import SupplierResource, SupplierQueryResource
from api_v3_resources.product import ProductResource, ProductQueryResource
from api_v3_resources.customer import CustomerResource, CustomerQueryResource
from api_v3_resources.order import OrderResource, OrderQueryResource
from api_v3_resources.sale import SaleResource, SaleQueryResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

resourceTable = {
    'suppliers': (SupplierResource, SupplierQueryResource),
    'products': (ProductResource, ProductQueryResource),
    'customers': (CustomerResource, CustomerQueryResource),
    'orders': (OrderResource, OrderQueryResource),
    'sales': (SaleResource, SaleQueryResource)
}

for table, (resource, query_resource) in resourceTable.items():
    api.add_resource(resource, f'/v3/{table}/<int:id>', f'/v3/{table}/create')
    api.add_resource(query_resource, f'/v3/{table}/query/<operation>', f'/v3/{table}/query/<operation>/<field>/<value>')
