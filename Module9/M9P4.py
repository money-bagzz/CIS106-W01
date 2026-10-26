def compute_pay_rate(code, hours):
    code = code[0].upper()
    if code == 'L':
        return 25.0
    elif code == 'A':
        return 30.0
    elif code == 'J':
        return 50.0
    else:
        return 0.0
        
total_gross_pay = 0.0
while True:
    cont = input("\nWould you like to continue (Y/N)? ")[0]
    if cont.lower() != 'y':
        break
    
    lName = input("\nEnter the employee's last name: ")
    code = input("Enter your job code (L, A, J): ")
    hours = int(input("Enter hours worked: "))
    pay_rate = compute_pay_rate(code, hours)
    
    if hours > 40:
        reg_pay = 40 * pay_rate
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * pay_rate * 1.5
        gross_pay = reg_pay + overtime_pay
    else:
        gross_pay = hours * pay_rate
    
    total_gross_pay += gross_pay
    print("\nEmployee: " + lName +
          "\nGross Pay: $" + str(gross_pay))
    
print("Total Gross Pay: $" + str(total_gross_pay))