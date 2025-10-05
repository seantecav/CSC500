# ---------- Step 1–3: ItemToPurchase ----------
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)
        self.item_description = item_description

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${total_cost:.0f}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


# ---------- Step 4: ShoppingCart ----------
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # Step 8
    def add_item(self, item):
        self.cart_items.append(item)

    # Step 9
    def remove_item(self, item_name):
        for i, it in enumerate(self.cart_items):
            if it.item_name == item_name:
                self.cart_items.pop(i)
                return
        print("Item not found in cart. Nothing removed.")

    # Step 10
    def modify_item(self, updated_item):
        for it in self.cart_items:
            if it.item_name == updated_item.item_name:
                if updated_item.item_description != "none":
                    it.item_description = updated_item.item_description
                if updated_item.item_price != 0.0:
                    it.item_price = updated_item.item_price
                if updated_item.item_quantity != 0:
                    it.item_quantity = updated_item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    # Step 6a
    def get_num_items_in_cart(self):
        return sum(it.item_quantity for it in self.cart_items)

    # Step 6b
    def get_cost_of_cart(self):
        return sum(it.item_price * it.item_quantity for it in self.cart_items)

    # Step 6c
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        num_items = self.get_num_items_in_cart()
        print(f"Number of Items: {num_items}")

        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            return

        for it in self.cart_items:
            it.print_item_cost()

        print(f"Total: ${self.get_cost_of_cart():.0f}")

    # Step 6d
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for it in self.cart_items:
            it.print_item_description()


# ---------- Step 5: Menu ----------
def print_menu(cart):
    menu = (
        "MENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit"
    )

    choice = ""
    while choice != "q":
        print()
        print(menu)
        choice = input("Choose an option:\n").strip().lower()

        if choice == "a":
            # Step 8
            print("ADD ITEM TO CART")
            name = input("Enter the item name:\n").strip()
            description = input("Enter the item description:\n").strip()
            price = float(input("Enter the item price:\n"))
            quantity = int(input("Enter the item quantity:\n"))
            cart.add_item(ItemToPurchase(name, price, quantity, description))

        elif choice == "r":
            # Step 9
            print("REMOVE ITEM FROM CART")
            name = input("Enter name of item to remove:\n").strip()
            cart.remove_item(name)

        elif choice == "c":
            # Step 10
            print("CHANGE ITEM QUANTITY")
            name = input("Enter the item name:\n").strip()
            quantity = int(input("Enter the new quantity:\n"))
            cart.modify_item(ItemToPurchase(item_name=name, item_quantity=quantity))

        elif choice == "i":
            print()
            cart.print_descriptions()

        elif choice == "o":
            print()
            cart.print_total()

        elif choice == "q":
            break
        else:
            continue


# ---------- Step 7: Main ----------
def main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print()
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")
    print()

    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)


if __name__ == "__main__":
    main()
