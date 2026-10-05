print("Enter employee's last name:")
lName = str(input())
print("Enter salary:")
salary = float(input())
print("Enter job level:")
level = int(input())

if level >= 10:
    bonus = .25
elif level >= 5:
    bonus = 0.2
else:
    bonus = 0.1
    
bonus_total = salary * bonus
print(str(lName) + "'s salary bonus: $" + str(bonus_total))