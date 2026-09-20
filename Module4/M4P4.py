print("Enter your first name:")
name = str(input())

print("Enter the number of steps walked today:")
steps = int(input())

cals_burnt = steps * 0.25
print(name + ", you burnt " + str(cals_burnt) + " calories!")