print("Enter an item (A or B) and its quantity:")
item = str(input())
quantity = int(input())

if(item.upper() == 'A'):
    item = 'A'
    unit_price = 10.00;
else:
    item = 'B'
    unit_price = 20.00;
    
extend_price = unit_price * quantity;

print("Item\tUnit Price\tExtended Price\n" +
      str(item) + "\t\t$" + str(unit_price) + "\t\t$" + str(extend_price))