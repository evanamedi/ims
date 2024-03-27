# I find it easier to use the txt version of this when using as a reference,
# you can find the documentation here: notes/html-route-data.txt

suppliers_form_list = [
    ['add-supplier', [
        {'for_label': 'name', 'text':'New Supplier Name:', 'id':'supplier_name', 'name':'supplier_name'},
        {'for_label': 'address', 'text':'New Supplier Address:', 'id':'supplier_address', 'name':'supplier_address'},
        {'for_label': 'contact', 'text':'New Supplier Contact', 'id':'supplier_contact', 'name':'supplier_contact'}
    ]],
    
    ['update-supplier-field', [
        {'for_label': 'supplier-update-field', 'text': 'Supplier ID:', 'id':'update-id', 'name':'supplier_id'},
        {'for_label': 'field', 'text': 'Select', 'id': 'field', 'type': 'select', 'options': {'supplier_name': 'Update Name', 'supplier_address': 'Update Address', 'supplier_contact': 'Update Contact'}},
        {'for_label': 'new-value', 'text': 'New Field:', 'id': 'new-value', 'name':'new-value'}
    ]],
    
    ['get-supplier-by-id', [
        {'for_label': 'supplier-id', 'text': '(search) Supplier ID:', 'id': 'get-supplier-id', 'name': 'the-supplier-id'}
    ]],
    
    ['delete-supplier', [
        {'for_label': 'supplier_id', 'text': '(delete) Supplier ID:', 'id': 'delete-supplier-id', 'name': 'the-supplier-id'}
    ]]
]


products_form_list = [
    ['add-product_form', [
        {'for_label': 'supplier_id', 'text': 'Supplier ID', 'id': 'add_product_supplier_id', 'name': 'add_product_supplier_id'},
        {'for_label': 'product_name', 'text': 'Product Name', 'id': 'add_product_name', 'name': 'add_product_name'},
        {'for_label': 'product_description', 'text': 'Product Description', 'id': 'add_product_description', 'name': 'add_product_description'},
        {'for_label': 'product_price', 'text': 'Price', 'id': 'add_product_price', 'name': 'add_product_price'},
        {'for_label': 'product_quantity', 'text': 'Quantity', 'id': 'add_product_quantity', 'name': 'add_product_quantity'}
    ]],
    
    ['update-product-form', [
        {'for_label': 'product_id', 'text': 'Product ID', 'id': 'update_product_by_id', 'name': 'update_product_id'},
        {'for_label': 'update_field', 'text': 'Select', 'id': 'update_product_field', 'type': 'select', 'options': {'product_name': 'Update Name', 'product_description': 'Update Description', 'product_price': 'Update Price', 'product_quantity': 'Update Quantity'}},
        {'for_label': 'update_field_new', 'text': 'New Field', 'id': 'update_product_new_field', 'name': 'update_product_new_field'}
    ]],
    
    ['get-product-form', [
        {'for_label': 'product_id', 'text': 'Product ID', 'id': 'get_product_by_id', 'name': 'get_product_by_id'}
    ]],
    
    ['delete-product-form', [
        {'for_label': 'product_id', 'text': 'Product ID', 'id': 'delete_product_by_id', 'name': 'delete_product_by_id'}
    ]]
]


customers_form_list = [
    ['add_customer_form', [
        {'for_label': 'customer_name', 'text': 'Customer Name', 'id': 'add_customer_name', 'name': 'add_customer_name'},
        {'for_label': 'customer_address', 'text': 'Customer Address', 'id': 'add_customer_address', 'name': 'add_customer_address'},
        {'for_label': 'customer_contact', 'text': 'Customer Contact', 'id': 'add_customer_contact', 'name': 'add_customer_contact'}
    ]],
    
    ['update_customer_form', [
        {'for_label': 'customer_id', 'text': 'Customer ID', 'id': 'update_customer_by_id', 'name': 'update_customer_by_id'},
        {'for_label': 'update_field', 'text': 'Select', 'id': 'update_customer_field', 'type': 'select', 'options': {'customer_name': 'Update Name', 'customer_address': 'Update Address', 'customer_contact': 'Update Contact'}},
        {'for_label': 'update_field_new', 'text': 'New Field', 'id': 'update_customer_new_field', 'name': 'update_customer_new_field'}
    ]],
    
    ['get_customer_form', [
        {'for_label': 'customer_id', 'text': 'Customer ID', 'id': 'get_customer_by_id', 'name': 'get_customer_by_id'}
    ]],
    
    ['delete_customer_form', [
        {'for_label': 'customer_id', 'text': 'Customer ID', 'id': 'delete_customer_by_id', 'name': 'delete_customer_by_id'}
    ]]
]


orders_form_list = [
    ['add_order_form', [
        {'for_label': 'product_id', 'text': 'Product ID', 'id': 'add_order_product_id', 'name': 'add_order_product_id'},
        {'for_label': 'customer_id', 'text': 'Customer ID', 'id': 'add_order_customer_id', 'name': 'add_order_customer_id'},
        {'for_label': 'order_date', 'text': 'Order Date', 'id': 'add_order_date', 'name': 'add_order_date'},
        {'for_label': 'order_quantity', 'text': 'Order Quantity', 'id': 'add_order_quantity', 'name': 'add_order_quantity'}
    ]],
    
    ['update_order_form', [
        {'for_label': 'order_id', 'text': 'Order ID', 'id': 'update_order_by_id', 'name': 'update_order_by_id'},
        {'for_label': 'update_field', 'text': 'Select', 'id': 'update_order_field', 'type': 'select', 'options': {'product_id': 'Update Product', 'customer_id': 'Update Customer', 'order_date': 'Update Date', 'order_quantity': 'Update Quantity'}},
        {'for_label': 'update_field_new', 'text': 'New Field', 'id': 'update_order_new_field', 'name': 'update_order_new_field'}
    ]],
    
    ['get_order_form', [
        {'for_label': 'order_id', 'text': 'Order ID', 'id': 'get_order_by_id', 'name': 'get_order_by_id'}
    ]],
    
    ['delete_order_form', [
        {'for_label': 'order_id', 'text': 'Order ID', 'id': 'delete_order_by_id', 'name': 'delete_order_by_id'}
    ]]
]


sales_form_list = [
    ['add_sale_form', [
        {'for_label': 'product_id', 'text': 'Product ID', 'id': 'add_sale_product_id', 'name': 'add_sale_product_id'},
        {'for_label': 'customer_id', 'text': 'Customer ID', 'id': 'add_sale_customer_id', 'name': 'add_sale_customer_id'},
        {'for_label': 'sale_date', 'text': 'Sale Date', 'id': 'add_sale_date', 'name': 'add_sale_date'},
        {'for_label': 'sale_quantity', 'text': 'Sale Quantity', 'id': 'add_sale_quantity', 'name': 'add_sale_quantity'}
    ]],
    
    ['update_sale_form', [
        {'for_label': 'sale_id', 'text': 'Sale ID', 'id': 'update_sale_by_id', 'name': 'update_sale_by_id'},
        {'for_label': 'update_field', 'text': 'Select', 'id': 'update_sale_field', 'type': 'select', 'options': {'product_id': 'Update Product', 'customer_id': 'Update Customer', 'sale_date': 'Update Date', 'sale_quantity': 'Update Quantity'}},
        {'for_label': 'update_field_new', 'text': 'New Field', 'id': 'update_sale_new_field', 'name': 'update_sale_new_field'}
    ]],
    
    ['get_sale_form', [
        {'for_label': 'sale_id', 'text': 'Sale ID', 'id': 'get_sale_by_id', 'name': 'get_sale_by_id'}
    ]],
    
    ['delete_sale_form', [
        {'for_label': 'sale_id', 'text': 'Sale ID', 'id': 'delete_sale_by_id', 'name': 'delete_sale_by_id'}
    ]]
]