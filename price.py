def calculate_discount(price, discount_percent):
    """Calculate the final price after applying discount"""
    discount_amount = price * discount_percent / 100
    final_price = price - discount_amount  # Corrected: subtract discount instead of adding
    return final_price

def apply_sales_tax(price, tax_percent):
    """Apply sales tax to the price"""
    tax_amount = price * tax_percent / 100
    final_price = price + tax_amount
    return final_price

def checkout(item_price, discount=10, tax=8):
    """Process checkout: apply discount then tax"""
    # Apply discount first
    discounted_price = calculate_discount(item_price, discount)
    
    # Apply tax on discounted price
    final_price = apply_sales_tax(discounted_price, tax)  # Corrected: use discounted price
    
    return final_price

# Test the checkout process
original_price = 100
print(f"Original Price: ${original_price}")
print(f"Discount: 10%")
print(f"Tax: 8%")
print(f"Final Price: ${checkout(original_price):.2f}")
