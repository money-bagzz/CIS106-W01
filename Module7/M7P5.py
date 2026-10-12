confirm = input("Do you want to continue this program? (Yes/No) ")
sum_discount = 0

while str.lower(confirm[0]) == "y":
    quantity = int(input("Enter the quantity for an item: "))
    price = float(input("Enter the price for the item: "))
    
    extended_price = quantity * price
    if extended_price > 10000:
        discount_amount = extended_price * 0.25
    else:
        discount_amount = extended_price * 0.1
    total = extended_price - discount_amount
    sum_discount += discount_amount
    
    print("\nExtended price: $" + str(extended_price) +
          "\nDiscount amount: $" + str(discount_amount) +
          "\nTotal: $" + str(total) + "\n")
    
    confirm = input("Do you want to continue this program? (Yes/No) ")
    
print("\nTotal discount amount: $" + str(sum_discount))