def apply_discount(price, discount):
    if not isinstance(price, (int or float)):
        return "The price should be a number"
    if not isinstance(discount, (int or float)):
        return "The discount should be a number"
    if price <= 0: 
        return "The price should be greater than 0"
    if discount < 0 or discount >100:
        return "The discount should be between 0 and 100"
    else:
        total = (price * discount)/100
        final_price = price - total
        apply_discount = final_price
        return apply_discount

    apply_discount(100, 20)
    apply_discount(200, 50)
    apply_discount(50, 0)
    apply_discount(0,100)
    apply_discount(74.5, 20.0)

print(apply_discount(100, 20))  # Expected output: 80.0
print(apply_discount(200, 50))  # Expected output: 100.0
print(apply_discount(50, 0))    # Expected output: 50.0
print(apply_discount(0, 100))   # Expected output: "The price should be greater than 0"
print(apply_discount(74.5, 20.0))  # Expected output: 59.6
