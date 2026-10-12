confirm = input("Do you want to continue this program? (Yes/No) ")
employees = 0
sum_gross_pay = 0

while str.lower(confirm[0]) == "y":
    last_name = input("Enter the employee's last name: ")
    hours = int(input("Enter hours worked: "))
    if hours > 40:
        hours *= 1.5
    pay_rate = float(input("Enter pay rate: "))
    
    gross_pay = hours * pay_rate
# %%
    sum_gross_pay += gross_pay

    employees += 1
    
    print("\nEmployee: " + last_name +
          "\nGross Pay: $" + str(gross_pay) + "\n")
    
    confirm = input("Do you want to continue this program? (Yes/No) ")
    
print("\nTotal Gross Pay: $" + str(sum_gross_pay) +
      "\nNumber of employees: " + str(employees))