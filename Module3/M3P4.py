print("Enter the make of your vehicle:")
make = str(input())

print("Enter the model of your vehicle:")
model = str(input())

print("Enter your vehicle's MSRP:")
msrp = float(input())

print("Enter your vehicle's discount percent:")
discount = float(input())

amount_off = msrp * discount
discount_price = msrp - amount_off

print("Make: " + str(make) + 
      "\nModel: " + str(model) + 
      "\nMSRP: $" + str(msrp) + 
      "\nDiscount Percent: %" + str(discount) +
      "\nAmount off: $" + str(amount_off) + 
      "\nDiscounted price: $" + str(discount_price))