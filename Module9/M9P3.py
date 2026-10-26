def compute_miles_per_gallon(miles, gallons):
    return miles * gallons

trips = 0
while True:
    cont = input("\nWould you like to continue (Y/N)? ")[0]
    if cont.lower() != 'y':
        break
    
    city = input("\nEnter the destination city: ")
    miles = float(input("Enter the amount of miles travelled: "))
    gallons = float(input("Enter the amount of gallons used: "))
    mpg = compute_miles_per_gallon(miles, gallons)
    trips += 1
    
    print("\nDestination City: " + city +
          "\nMiles: " + str(miles) +
          "\nMiles Per Gallon: " + str(mpg))
    
print("Total number of trips: " + str(trips))