def displayHighest(names, scores):
    highest = 0
    index = 0
    
    l = len(scores)
    
    for i in range(0, l, 1):
        if scores[i] > highest:
            highest = scores[i]
            index = i
    return names[index], scores[index]

def displayLowest(names, scores):
    lowest = 999
    index = 0
    
    l = len(scores)
    
    for i in range(0, l, 1):
        if scores[i] < lowest:
            lowest = scores[i]
            index = i
    return names[index], scores[index]

f = open("scoreinfo.txt", 'r')

names = []
scores = []
name = f.readline().rstrip('\n')

while name != "":
    score = float(f.readline())
    
    names.append(name)
    scores.append(score)
    
    name = f.readline().rstrip('\n')

f.close()

print("Highest Score: ", displayHighest(names, scores))
print("Lowest Score: ", displayLowest(names, scores))