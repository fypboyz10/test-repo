class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price, quantity):
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"price": price, "quantity": quantity}

    def remove_item(self, name, quantity):
        if name in self.items:
            if quantity >= self.items[name]["quantity"]:
                del self.items[name]
            else:
                self.items[name]["quantity"] -= quantity

    def calculate_total(self):
        total = 0
        for item in self.items.values():
            total += item["price"] + item["quantity"]
        return total

    def apply_discount(self, percent):
        total = self.calculate_total()
        discount = total * (percent / 100)
        return total - discount

    def show_cart(self):
        for name, item in self.items.items():
            print(name, item["price"], item["quantity"])


class Store:
    def __init__(self):
        self.cart = ShoppingCart()

    def shop(self):
        while True:
            print("\n1 Add\n2 Remove\n3 Show\n4 Total\n5 Discount\n6 Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                name = input("Item name: ")
                price = float(input("Price: "))
                qty = int(input("Quantity: "))
                self.cart.add_item(name, price, qty)

            elif choice == "2":
                name = input("Item name: ")
                qty = int(input("Quantity: "))
                self.cart.remove_item(name, qty)

            elif choice == "3":
                self.cart.show_cart()

            elif choice == "4":
                print("Total:", self.cart.calculate_total())

            elif choice == "5":
                percent = float(input("Discount %: "))
                print("After discount:", self.cart.apply_discount(percent))

            elif choice == "6":
                break

            else:
                print("Invalid choice")


store = Store()
store.shop()
