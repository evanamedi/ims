from api_v3.models import Supplier, Product, Customer, Order, Sale
from logic.get_ids import getID

# NEED MORE OPTIMAL SOLUTION FOR THIS DATA STRUCTURE

label = 'for_label'
idSelection = 'select_id'


suppliers_form_list = [
    'suppliers',
    
    ['createFormID', [
        {label: 'supplier_name', 'text':'New Supplier Name:', 'id':'supplier_name', 'name':'add_supplier_name'},
        {label: 'supplier_address', 'text':'New Supplier Address:', 'id':'supplier_address', 'name':'add_supplier_address'},
        {label: 'supplier_contact', 'text':'New Supplier Contact', 'id':'supplier_contact', 'name':'add_supplier_contact'}
    ]],
    
    ['updateFormID', [
        {label: 'supplier_id', 'text': 'Supplier ID:', 'id':'update_id', 'name':'update_supplier_id', 'type': idSelection, 'options': getID(Supplier)},
        {label: 'update_field', 'text': 'Select', 'id': 'update_field', 'type': 'select', 'options': {'supplier_name': 'Update Name', 'supplier_address': 'Update Address', 'supplier_contact': 'Update Contact'}},
        {label: 'update_field_new', 'text': 'New Field:', 'id': 'update_new_field', 'name':'update_supplier_new_field'}
    ]],
    
    ['getFormID', [
        {label: 'supplier_id', 'text': '(search) Supplier ID:', 'id': 'get_id', 'name': 'get_supplier_by_id', 'type': idSelection, 'options': getID(Supplier)}
    ]],
    
    ['deleteFormID', [
        {label: 'supplier_id', 'text': '(delete) Supplier ID:', 'id': 'delete_id', 'name': 'delete_supplier_by_id', 'type': idSelection, 'options': getID(Supplier)}
    ]]
]


products_form_list = [
    'products',
    
    ['createFormID', [
        {label: 'supplier_id', 'text': 'Supplier ID', 'id': 'supplier_id', 'name': 'add_product_supplier_id', 'type': idSelection, 'options': getID(Supplier)},
        {label: 'product_name', 'text': 'Product Name', 'id': 'product_name', 'name': 'add_product_name'},
        {label: 'product_description', 'text': 'Product Description', 'id': 'product_description', 'name': 'add_product_description'},
        {label: 'product_price', 'text': 'Price', 'id': 'product_price', 'name': 'add_product_price'},
        {label: 'product_quantity', 'text': 'Quantity', 'id': 'product_quantity', 'name': 'add_product_quantity'}
    ]],
    
    ['updateFormID', [
        {label: 'product_id', 'text': 'Product ID', 'id': 'update_id', 'name': 'update_product_id', 'type': idSelection, 'options': getID(Product)},
        {label: 'update_field', 'text': 'Select', 'id': 'update_field', 'type': 'select', 'options': {'product_name': 'Update Name', 'product_description': 'Update Description', 'product_price': 'Update Price', 'product_quantity': 'Update Quantity'}},
        {label: 'update_field_new', 'text': 'New Field', 'id': 'update_new_field', 'name': 'update_product_new_field'}
    ]],
    
    ['getFormID', [
        {label: 'product_id', 'text': '(search) Product ID', 'id': 'get_id', 'name': 'get_product_by_id', 'type': idSelection, 'options': getID(Product)}
    ]],
    
    ['deleteFormID', [
        {label: 'product_id', 'text': '(delete) Product ID', 'id': 'delete_id', 'name': 'delete_product_by_id', 'type': idSelection, 'options': getID(Product)}
    ]]
]


customers_form_list = [
    'customers',
    
    ['createFormID', [
        {label: 'customer_name', 'text': 'Customer Name', 'id': 'customer_name', 'name': 'add_customer_name'},
        {label: 'customer_address', 'text': 'Customer Address', 'id': 'customer_address', 'name': 'add_customer_address'},
        {label: 'customer_contact', 'text': 'Customer Contact', 'id': 'customer_contact', 'name': 'add_customer_contact'}
    ]],
    
    ['updateFormID', [
        {label: 'customer_id', 'text': 'Customer ID', 'id': 'update_id', 'name': 'update_customer_by_id', 'type': idSelection, 'options': getID(Customer)},
        {label: 'update_field', 'text': 'Select', 'id': 'update_field', 'type': 'select', 'options': {'customer_name': 'Update Name', 'customer_address': 'Update Address', 'customer_contact': 'Update Contact'}},
        {label: 'update_field_new', 'text': 'New Field', 'id': 'update_new_field', 'name': 'update_customer_new_field'}
    ]],
    
    ['getFormID', [
        {label: 'customer_id', 'text': '(search) Customer ID', 'id': 'get_id', 'name': 'get_customer_by_id', 'type': idSelection, 'options': getID(Customer)}
    ]],
    
    ['deleteFormID', [
        {label: 'customer_id', 'text': '(delete) Customer ID', 'id': 'delete_id', 'name': 'delete_customer_by_id', 'type': idSelection, 'options': getID(Customer)}
    ]]
]


orders_form_list = [
    'orders',
    
    ['createFormID', [
        {label: 'product_id', 'text': 'Product ID', 'id': 'product_id', 'name': 'add_order_product_id', 'type': idSelection, 'options': getID(Product)},
        {label: 'customer_id', 'text': 'Customer ID', 'id': 'customer_id', 'name': 'add_order_customer_id', 'type': idSelection, 'options': getID(Customer)},
        {label: 'order_date', 'text': 'Order Date', 'id': 'order_date', 'name': 'add_order_date'},
        {label: 'order_quantity', 'text': 'Order Quantity', 'id': 'order_quantity', 'name': 'add_order_quantity'}
    ]],
    
    ['updateFormID', [
        {label: 'order_id', 'text': 'Order ID', 'id': 'update_id', 'name': 'update_order_by_id', 'type': idSelection, 'options': getID(Order)},
        {label: 'update_field', 'text': 'Select', 'id': 'update_field', 'type': 'select', 'options': {'product_id': 'Update Product', 'customer_id': 'Update Customer', 'order_date': 'Update Date', 'order_quantity': 'Update Quantity'}},
        {label: 'update_field_new', 'text': 'New Field', 'id': 'update_new_field', 'name': 'update_order_new_field'}
    ]],
    
    ['getFormID', [
        {label: 'order_id', 'text': '(search) Order ID', 'id': 'get_id', 'name': 'get_order_by_id', 'type': idSelection, 'options': getID(Order)}
    ]],
    
    ['deleteFormID', [
        {label: 'order_id', 'text': '(delete) Order ID', 'id': 'delete_id', 'name': 'delete_order_by_id', 'type': idSelection, 'options': getID(Order)}
    ]]
]


sales_form_list = [
    'sale',
    
    ['createFormID', [
        {label: 'product_id', 'text': 'Product ID', 'id': 'product_id', 'name': 'add_sale_product_id', 'type': idSelection, 'options': getID(Product)},
        {label: 'customer_id', 'text': 'Customer ID', 'id': 'customer_id', 'name': 'add_sale_customer_id', 'type': idSelection, 'options': getID(Customer)},
        {label: 'sale_date', 'text': 'Sale Date', 'id': 'sale_date', 'name': 'add_sale_date'},
        {label: 'sale_quantity', 'text': 'Sale Quantity', 'id': 'sale_quantity', 'name': 'add_sale_quantity'}
    ]],
    
    ['updateFormID', [
        {label: 'sale_id', 'text': 'Sale ID', 'id': 'update_id', 'name': 'update_sale_by_id', 'type': idSelection, 'options': getID(Sale)},
        {label: 'update_field', 'text': 'Select', 'id': 'update_field', 'type': 'select', 'options': {'product_id': 'Update Product', 'customer_id': 'Update Customer', 'sale_date': 'Update Date', 'sale_quantity': 'Update Quantity'}},
        {label: 'update_field_new', 'text': 'New Field', 'id': 'update_new_field', 'name': 'update_sale_new_field'}
    ]],
    
    ['getFormID', [
        {label: 'sale_id', 'text': '(search) Sale ID', 'id': 'get_id', 'name': 'get_sale_by_id', 'type': idSelection, 'options': getID(Sale)}
    ]],
    
    ['deleteFormID', [
        {label: 'sale_id', 'text': '(delete) Sale ID', 'id': 'delete_id', 'name': 'delete_sale_by_id', 'type': idSelection, 'options': getID(Sale)}
    ]]
]