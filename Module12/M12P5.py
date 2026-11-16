def displayPlayers(names, averages):
    for i in range(0, len(names), 1):
        print(names[i], averages[i])
        
def searchPlayer(names, averages, query):
    for i in range(0, len(names), 1):
        if names[i].lower() == query.lower():
            print("Player Name:", names[i])
            print("Battling Average:", averages[i])
            return
    
    print("Name not found")

f = open("battleaverages.txt", "r")

names = []
averages = []

name = f.readline().rstrip('\n')

while name != "":
    average = float(f.readline())
    
    names.append(name)
    averages.append(average)
    
    name = f.readline().rstrip('\n')
    
f.close()

print("Player List:")
displayPlayers(names, averages)
    
query = input("\nEnter a player's last name (Q to quit): ")

while query.upper() != 'Q':
    
    searchPlayer(names, averages, query)
    query = input("\nEnter a player's last name (Q to quit): ")