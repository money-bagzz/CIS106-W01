names = [
    "Collins", "James", "John", "Joe", "Jane",
    "Tyrone", "Blevins", "Tyler", "Tim", "Dan"
    ]

def displayNames():
    for name in names:
        print(name)
        
def displayReverse():
    l = len(names)
    for i in range(l - 1, -1, -1):
        print(names[i])
        
print("List of Names:\n")
displayNames()

print("\nList of Names In Reverse Order:\n")
displayReverse()
