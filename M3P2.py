print("Enter your last name:")
last_name = str(input())

print("Enter your midterm exam score:")
midterm = int(input())

print("Enter your final exam score:")
final = int(input())

total_points = (0.4 * midterm) + (0.6 * final)
print(last_name + " - Total exam points: " + str(total_points))