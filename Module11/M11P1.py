def calc_discount(quantity, price, discount_price):
    total = quantity * price
    discount_amt = total * (discount_price / 100)
    discount_price = total - discount_amt
    return discount_amt, discount_price

quantity = int(input("Enter Quantity: "))
price = float(input("Enter Price: $"))
discount_rate = float(input("Enter Discount Rate: %"))
discount_amt, discount_price = calc_discount(quantity, price, discount_rate)

# Found a nifty way to format strings online! Here's a link:
# https://www.w3schools.com/python/python_string_formatting.asp
print("\n-- Results --")
print("\nQuantity: ", quantity)
print("Price Per Item: $", format(price, ".2f"))
print("Total Cost: $", format(price * quantity, ".2f"))
print("Discount Amount: $", format(discount_amt, ".2f"))
print("Discounted Price: $", format(discount_price, ".2f"))