def compute_tuition_owed(hours, dist_code):
    dist_code = dist_code[0].upper()
    tuition = 0.0
    if dist_code == 'I':
        tuition = hours * 250.0
    elif dist_code == 'O':
        tuition = hours * 550.0
        
    return tuition

total_tuition = 0.0
while True:
    cont = input("\nWould you like to continue (Y/N)? ")[0]
    if cont.lower() != 'y':
        break
    
    lName = input("\nEnter student last name: ")
    hours = int(input("Enter credit hours: "))
    dist_code = input("Enter district code: ")
    tuition = compute_tuition_owed(hours, dist_code)
    total_tuition += tuition
    
    print("\nStudent: " + lName +
          "\nTuition Owed: $" + str(tuition))
    
print("Total Tuition Owed: $" + str(total_tuition))
    