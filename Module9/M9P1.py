def compute_extended(quantity, price):
    ep = quantity * price
    if ep > 100000:
        return ep * 0.1
    return ep

total_extended_price = 0.0
while True:
    cont = input("\nWould you like to continue (Y/N)? ")[0]
    if cont.lower() != 'y':
        break
        
    quantity = int(input("\nEnter the quantity of your item: "))
    price = float(input("Enter the price of your item: "))
    extended_price = compute_extended(quantity, price)
    total_extended_price += extended_price
    
    print("\nQuantity: " + str(quantity) +
          "\nPrice: $" + str(price) +
          "\nExtended Price: $" + str(extended_price))
    
print("\nTotal Extended Price: $" + str(total_extended_price))