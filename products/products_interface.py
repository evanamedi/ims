import logging
from products.products_operations import action_one
from products.products_operations import action_two
from products.products_operations import action_three
from products.products_operations import action_four
from products.products_operations import action_five
from products.products_operations import get_all_products
from products.products_operations import get_product_by_name

logger = logging.getLogger(__name__)

def product_interface():
    actions = {
    1: action_one,
    2: action_two,
    3: action_three,
    4: action_four,
    5: action_five,
    6: get_all_products,
    7: lambda: get_product_by_name(input("Product Name: "))
}
    while True:
        try:
            action = int(input("\n--------------------Products Menu--------------------\n"
                            "\n1 Create New Product"
                            "\n2 Update Product Name"
                            "\n3 Update Product Description"
                            "\n4 Update Product Price"
                            "\n5 Update Product Quantity"
                            "\n6 Show All Products"
                            "\n7 Get Product Information"
                            "\n0 Return\n"))
            if action == 0:
                break
            elif action in actions:
                actions[action]()
            else:
                print("Invalid Input. Please enter a number between 0 and 7")
                logger.warning("Invalid Input. Value outside constraints")
        except ValueError:
            print("Invalid Input. Please enter a number")




