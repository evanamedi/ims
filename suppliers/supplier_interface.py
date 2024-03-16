import logging
from suppliers.supplier_operations import action_one
from suppliers.supplier_operations import action_two
from suppliers.supplier_operations import action_three
from suppliers.supplier_operations import action_four
from suppliers.supplier_operations import get_all_suppliers
from suppliers.supplier_operations import get_supplier_by_name


logger = logging.getLogger(__name__)

def supplier_interface():
    actions = {
        1: action_one,
        2: action_two,
        3: action_three,
        4: action_four,
        5: get_all_suppliers,
        6: lambda: get_supplier_by_name(input("Enter Supplier: "))
    }

    while True:
        try:
            action = int(input("\n--------------------Suppliers Menu--------------------\n"
                            "\n1 Create Supplier"
                            "\n2 Update Supplier Name"
                            "\n3 Update Supplier Address"
                            "\n4 Update Supplier Contact"
                            "\n5 See All Suppliers"
                            "\n6 Supplier Information"
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




