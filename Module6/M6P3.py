print("Enter the principle amount of a CD:")
principle = float(input())
print("Enter the years to maturity of the CD")
maturity = int(input())

if principle > 100000 and maturity == 5:
    interest = 6
elif principle >= 50000 and maturity == 10:
    interest = 5
elif principle >= 50000 and maturity == 5:
    interest = 4
else:
    interest = 2
    
first_year_interest = principle * (interest / 100)
print("Principle: " + str(principle))
print("Interest rate: " + str(interest) + "%")
print("First year interest: " + str(first_year_interest))
    