# ------------------------------------------------------------------------------
# Author:        Venkata Rahul Jammalamadaka
# Version:       Python 2.7.14
# Last updated:
# ------------------------------------------------------------------------------




import sys


class Product(object):
    def __init__(self, items, quantity):
        self.items = items
        self.quantity = quantity


class InvalidQuantity(Exception):
    def __init__(self, message):
        self.message = message


class InvalidProductId(Exception):
    def __init__(self, message):
        self.message = message


Inventory = {
    1: Product('Apple', 10),
    2: Product('Orange', 12),
    3: Product('Banana', 6),
    4: Product('Peach', 5),
    5: Product('Avocado', 3)
}
# To add more items, Inventory[6] = Product('Grapes', 8)


# Displays all the products in the inventory
def display_inventory():
    print("\nId\t|\tItems\t|\tQty")
    print("--------------------------------------")
    for key in Inventory.keys():
        print (str(key) + "\t|\t" + str(Inventory[key].items) + "\t|\t" + str(Inventory[key].quantity))


# Updates the inventory quantity after the order has been placed
def purchase_product(product_id, purchase_qty):
    if product_id in Inventory and product_id > 0:
        if 0 < purchase_qty <= Inventory[product_id].quantity:
            Inventory[product_id].quantity -= purchase_qty
            print("\n--- Your items have been ordered. ---")
            display_inventory()
        else:
            # Exception for an invalid Product_Quantity input
            raise InvalidQuantity("Please enter the correct quantity available from Inventory")
    else:
        # Exception for an invalid Product_Id input
        raise InvalidProductId("Please enter the correct productId available from Inventory")


# To Continue with the order from the inventory
def proceed_with_order():
    status = raw_input("\nDo you wish to continue (yes/no):")
    if status.lower() == 'yes':
        pass
    elif status.lower() == 'no':
        print("\n--- Thanks for placing the order. ---")
        sys.exit(0)
    else:
        print("Invalid Input. Terminating...")
        sys.exit(-1)


def order_management():
    while True:
        try:
            display_inventory()
            print("\nWhat would you like to order today ?")
            item_id = int(raw_input("Please enter the product id: "))
            item_quantity = int(raw_input("Please enter the Qty: "))
            purchase_product(item_id, item_quantity)
            proceed_with_order()

        except ValueError:
            print("Please enter a valid number available from the Inventory")

        except InvalidQuantity, q:
            print(q.message)

        except InvalidProductId, p:
            print(p.message)


if __name__ == "__main__":
    order_management()