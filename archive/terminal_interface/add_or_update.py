# from suppliers.supplier_interface import supplier_interface
# from products.products_interface import product_interface
# from customers.customer_interface import customer_interface
# from orders.order_interface import order_interface
# from sales.sale_interface import sale_interface

# def add_update():
#     action = 0
#     while True:
#         try:
#             action = int(input("\n--------------------Update Menu--------------------"
#                             "\n1 Suppliers"
#                             "\n2 Products"
#                             "\n3 Customers"
#                             "\n4 Orders"
#                             "\n5 Sales"
#                             "\n0 Return\n"))
#         except ValueError:
#             print("Invalid Input. Please enter a number")
        
#         if action == 0:
#             break

#         elif action == 1:
#             supplier_interface()

#         elif action == 2:
#             product_interface()

#         elif action == 3:
#             customer_interface()

#         elif action == 4:
#             order_interface()

#         elif action == 5:
#             sale_interface()

#         else: 
#             print("Invalid Input")