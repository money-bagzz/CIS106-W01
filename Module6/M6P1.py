print("Input the quantity: ")
quantity = int(input())

if quantity > 10000:
    price = 10
elif quantity >= 5000:
    price = 20
else:
    price = 30

extendedPrice = quantity * price
tax = 7
total = extendedPrice * (tax / 100)

print("Extended price: $" + str(extendedPrice))
print("Tax amount: " + str(tax) + "%")
print("Total: $" + str(total))