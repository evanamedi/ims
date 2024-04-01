import logging
from orders.order_operations import action_one
from orders.order_operations import action_two
from orders.order_operations import action_three
from orders.order_operations import action_four
from orders.order_operations import get_all_orders
from orders.order_operations import get_order_by_product


logger = logging.getLogger(__name__)

def order_interface():
    actions = {
    1: action_one,
    2: action_two,
    3: action_three,
    4: action_four,
    5: get_all_orders,
    6: lambda: get_order_by_product(input("Enter Product #: "))
}

    while True:
        try:
            action = int(input("\n--------------------Order Menu--------------------"
                            "\n1 Create New Order"
                            "\n2 Update Product"
                            "\n3 Update Date"
                            "\n4 Update Quantity"
                            "\n5 Show All Orders"
                            "\n6 Search All Orders for Product"
                            "\n0 Return\n"))
            if action == 0:
                break
            elif action in actions:
                actions[action]()
            else:
                print("Invalid Input. Please enter a number between 0 and 6")
                logger.warning("Invalid Input. Value outside constraints")
        except ValueError:
            print("Invalid Input. Please enter a number")
            logger.warning("Invalid Input. Not Integer")




