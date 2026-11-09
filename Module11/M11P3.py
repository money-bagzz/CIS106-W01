def calculate_commission(sales):
    if sales > 100000:
        commission = sales * 0.1
    else:
        commission = sales * 0.05
        
    target = sales * 0.05
    return commission, target
    
last_name = input("Enter last name: ")
last_name = last_name[0].upper() + last_name[1:]

sales = float(input("Enter sales: $"))
commission, target = calculate_commission(sales)

print("\n--Sales Report for", last_name + "--")
print("\nCommission: $", format(commission, ".2f"))
print("Next Year's Target: $", format(target, ".2f"))