def compute_average(score1, score2, score3):
    total_points = score1 + score2 + score3
    average = total_points / 3
    return total_points, average
    
# Just wanted to mess around with string indexing to make 
# sure the name is properly formatted.
last_name = input("Enter Last Name: ")
last_name = last_name[0].upper() + last_name[1:]

score1 = float(input("Enter Exam Score #1: %"))
score2 = float(input("Enter Exam Score #2: %"))
score3 = float(input("Enter Exam Score #3: %"))

total_points, average = compute_average(score1, score2, score3)

print("\n--Exam Results For", last_name + "--")
print("\nTotal Points:", format(total_points, ".2f"))
print("Exam Average: %", format(average, ".2f"))