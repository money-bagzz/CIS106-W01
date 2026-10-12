# Found this nifty way to put string input 
# messages in the variable declaration
confirm = input("Do you want to continue this program? (Yes/No) ")

# Added this to ensure a fair input system
while str.lower(confirm[0]) == "y":
    last_name = input("Enter student's last name: ")
    score1 = float(input("Enter the first exam score: "))
    score2 = float(input("Enter the second exam score: "))
    
    average = (score1 + score2) / 2
    print("\nLast name: " +
          str(last_name) +
          "\nExam average: " +
          str(average) + "\n")
    
    confirm = input("Do you want to continue this program? (Yes/No) ")