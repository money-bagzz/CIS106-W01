print("Enter the quantity of your item:")
quantity = int(input())

if (quantity >= 1000):
    unit_price = 3.00
else:
    unit_price = 5.00

extend_price = quantity * unit_price
tax = extend_price * 0.07
total = extend_price + tax

print("Quantity:\t" + str(quantity) + 
      "\nUnit price:\t$" + str(unit_price) +
      "\nExtended price:\t$" + str(extend_price) +
      "\nTax:\t$" + str(tax) +
      "\nTotal:\t$" + str(total))