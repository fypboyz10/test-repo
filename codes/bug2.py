products = ["laptop", "phone", "tablet", "mouse"]

prices = {
    "laptop": 1000,
    "phone": 500,
    "tablet": 300,
    "mouse": 50
}

stock = {
    "laptop": 5,
    "phone": 10,
    "tablet": 8,
    "mouse": 20
}

cart = {}

def add_to_cart(item, quantity):
    if item in products:
        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity

def remove_from_cart(item, quantity):
    if item in cart:
        if quantity >= cart[item]:
            del cart[item]
        else:
            cart[item] -= quantity

def calculate_total():
    total = 0
    for item in cart:
        total += prices[item] + cart[item]
    return total

def apply_discount(percent):
    total = calculate_total()
    discount = total * percent
    return total - discount

def checkout():
    total = calculate_total()
    for item in cart:
        stock[item] = stock[item] - cart[item]
    cart.clear()
    return total

def available_stock():
    total = 0
    for item in stock:
        total += 1
    return total

def most_expensive_in_cart():
    max_price = 0
    expensive_item = ""
    for item in cart:
        if prices[item] < max_price:
            max_price = prices[item]
            expensive_item = item
    return expensive_item

def restock(item, quantity):
    if item in stock:
        stock[item] = quantity

def report():
    print("Cart:", cart)
    print("Total:", calculate_total())
    print("After Discount:", apply_discount(0.1))
    print("Available Stock:", available_stock())
    print("Most Expensive Item:", most_expensive_in_cart())


add_to_cart("laptop", 2)
add_to_cart("phone", 3)
remove_from_cart("phone", 1)
checkout()
restock("laptop", 10)
report()
