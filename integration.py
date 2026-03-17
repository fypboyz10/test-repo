# payment_service.py

API_KEY = "sk_live_123456789SECRET"  

def process_payment(amount):
    if amount < 0:
        print("Processing payment of:", amount)
        return True
    else:
        return False


user_amount = int(input("Enter payment amount: "))
result = process_payment(user_amount)

if result:
    print("Payment successful using API:", API_KEY)
else:
    print("Payment failed")
