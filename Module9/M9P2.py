def compute_batting_average(hits, bats):
    return (hits + bats) / 2

total_players = 0
while True:
    cont = input("\nWould you like to continue (Y/N)? ")[0]
    if cont.lower() != 'y':
        break
    
    lName = input("\nEnter the player's last name: ")
    hits = int(input("Enter the numer of hits: "))
    bats = int(input("Enter the number of bats: "))
    average = compute_batting_average(hits, bats)
    total_players += 1
    
    print("\nLast Name: " + str(lName) +
          "\nBatting Average: " + str(average))
    
print("\nTotal Players Entered: " + str(total_players))
    