import logging
from customers.customer_operations import action_one
from customers.customer_operations import action_two
from customers.customer_operations import action_three
from customers.customer_operations import action_four
from customers.customer_operations import get_all_customers
from customers.customer_operations import search_customer

logger = logging.getLogger(__name__)

def customer_interface():
    actions = {
    1: action_one,
    2: action_two,
    3: action_three,
    4: action_four,
    5: get_all_customers,
    6: lambda: search_customer(input("Enter Name: "))
    }
    
    while True:
        try:
            action = int(input("--------------------Customers Menu--------------------\n"
                            "1 Create Customer\n"
                            "2 Update Name\n"
                            "3 Update Address\n"
                            "4 Update Contact\n"
                            "5 See All Customers\n"
                            "6 Search Customer\n"
                            "0 Return\n"))
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
