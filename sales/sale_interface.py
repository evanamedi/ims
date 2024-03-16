import logging
from sales.sale_operations import action_one
from sales.sale_operations import action_two
from sales.sale_operations import action_three
from sales.sale_operations import action_four
from sales.sale_operations import action_five
from sales.sale_operations import get_all_sales
from sales.sale_operations import get_product_sales
from sales.sale_operations import get_customer_sales
from sales.sale_operations import get_date_sales

logger = logging.getLogger(__name__)

def sale_interface():
    actions = {
    1: action_one,
    2: action_two,
    3: action_three,
    4: action_four,
    5: action_five,
    6: get_all_sales,
    7: lambda: get_product_sales(input("Enter Product #: ")),
    8: lambda: get_customer_sales(input("Enter Customer #: ")),
    9: lambda: get_date_sales(input("Enter Date: "))
}

    while True:
        try:
            action = int(input("\n--------------------Sales Menu--------------------"
                            "\n1 Create New Sale"
                            "\n2 Update Product"
                            "\n3 Update Customer"
                            "\n4 Update Date"
                            "\n5 Update Quantity"
                            "\n6 Get All Sales"
                            "\n7 Get Sales by Product"
                            "\n8 Get Sales by Customer"
                            "\n9 Get Sales by Date"
                            "\n0 Return\n"))
            if action == 0:
                break
            elif action in actions:
                actions[action]()
            else:
                print("Invalid Input. Please enter a number between 0 and 9")
                logger.warning("Invalid Input. Value outside constraints")
        except ValueError:
            print("Invalid Input. Please enter a number")
            logger.warning("Invalid Input. Not Integer")
