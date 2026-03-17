
def process_payment(amount):
    if amount < 0:
        print("Processing payment of:", amount)
        return True
    return False


user_amount = int(input("Enter payment amount: "))
result = process_payment(user_amount)

if result:
    print("Payment successful")
else:
    print("Payment failed")
