from api.supplier_routes_v2 import supplier_routes_v2
from api.product_routes_v2 import product_routes_v2
from api.order_routes_v2 import order_routes_v2
from api.customer_routes_v2 import customer_routes_v2
from api.sale_routes_v2 import sale_routes_v2

def register_blueprints(app):
    app.register_blueprint(supplier_routes_v2)
    app.register_blueprint(product_routes_v2)
    app.register_blueprint(order_routes_v2)
    app.register_blueprint(customer_routes_v2)
    app.register_blueprint(sale_routes_v2)