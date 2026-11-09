quantity = int(input("Enter Quantity: "))
unit_price = float(input("Enter Unit Price: "))

def compute_total():
    total = quantity * unit_price
    tax = total * 0.07
    return total, tax

total, tax = compute_total()

print("\n--Results--")
print("\nTotal: $", format(total, ".2f"))
print("Tax: $", format(tax, ".2f"))