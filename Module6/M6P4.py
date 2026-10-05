print("Enter an amount of concert tickets: ")
tickets = int(input())

if tickets >= 25:
    price_per_ticket = 50
elif tickets >= 10:
    price_per_ticket = 60
elif tickets >= 5:
    price_per_ticket = 70
else:
    price_per_ticket = 75
    
total = tickets * price_per_ticket
print("Number of tickets: " + str(tickets))
print("Price per ticket: $" + str(price_per_ticket))
print("Total cost: $" + str(total))