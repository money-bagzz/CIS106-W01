print("Enter a part number:")
partNum = int(input())
print("Enter the part's quantity:")
quantity = int(input())

if partNum == 10 or partNum == 55:
    unit_cost = 1.00
elif partNum == 99:
    unit_cost = 2.00
elif partNum == 80 or partNum == 70:
    unit_cost = 3.00
else:
    unit_cost = 5.00
    
total = quantity * unit_cost
print("Part number: " + str(partNum))
print("Cost per unit: $" + str(unit_cost))
print("Total cost: $" + str(total))