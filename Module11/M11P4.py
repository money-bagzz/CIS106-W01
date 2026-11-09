def compute_average(score1, score2, score3, handicap):
    average = (score1 + score2 + score3) / 3
    handicap_avg = average + handicap
    return average, handicap_avg

last_name = input("Enter last name: ")
last_name = last_name[0].upper() + last_name[1:]

score1 = float(input("Enter Game Score #1: "))
score2 = float(input("Enter Game Score #2: "))
score3 = float(input("Enter Game Score #3: "))

handicap = int(input("Enter handicap: "))
average, handicap_avg = compute_average(score1, score2, score3, handicap)

print("\n--Bowling Report for", last_name + "--")
print("\nAverage Score:", format(average, ".2f"))
print("Average Score With Handicap:", format(handicap_avg, ".2f"))