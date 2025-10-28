class CustomerList:
    """Manages a list of customers for a store."""
    
    # The buggy function is the constructor (__init__)!
    def __init__(self, store_name, customers=[]):
        self.store_name = store_name
        self.customers = customers
        print(f"Created list for {self.store_name}. Customers: {self.customers}")

    def add_customer(self, name):
        self.customers.append(name)
        print(f"Added {name} to {self.store_name}. Customers: {self.customers}")

# --- Let's demonstrate the bug ---

print("--- 🛒 Opening Store A ---")
store_a = CustomerList("Store A")
store_a.add_customer("Alice")
store_a.add_customer("Bob")

print("\n--- 🛒 Opening Store B ---")
store_b = CustomerList("Store B") 
store_b.add_customer("Charles")

print("\n--- 🏁 Final Results ---")
print(f"Final list for Store A: {store_a.customers}")
print(f"Final list for Store B: {store_b.customers}")
