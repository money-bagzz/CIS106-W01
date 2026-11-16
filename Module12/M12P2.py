names = [
    "Collins", "James", "John", "Joe", "Jane",
    "Tyrone", "Blevins", "Tyler", "Tim", "Dan"
    ]
scores = [
    99.9, 40.7, 87.2, 30.4, 20.8,
    100.0, 89.4, 77.2, 43.6, 2.9
    ]
l = len(names)
    
def displayNames():
    for i in range(0, l, 1):
        print(names[i], str(scores[i]))
        
def displayReverse():
    for i in range(l - 1, -1, -1):
        print(names[i], str(scores[i]))
        
print("List of Names/Scores:\n")
displayNames()

print("\nList of Names/Scores In Reverse Order:\n")
displayReverse()
