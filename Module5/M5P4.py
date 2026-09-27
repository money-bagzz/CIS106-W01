print("Enter the name of the appliance:")
name = str(input())
print("\nEnter the cost of the appliance:")
cost = float(input())

if(cost > 1000):
    warranty = 0.1
else:
    warranty = 0.05
    
warranty_cost = cost * warranty
total = cost + warranty_cost

print("\nAppliance Name:\n" +
      str(name) + 
      "\nAppliance Cost:\n$" +
      str(cost) +
      "\nWarranty Cost:\n$" +
      str(warranty_cost) +
      "\nTotal:\n$" +
      str(total))