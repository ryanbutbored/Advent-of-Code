f = open("2023\\Day 06\\input.txt", "r")
lines = f.readlines()
times = [int(x) for x in lines[0].strip().split(":")[1].split(" ") if x != ""]
distances = [int(x) for x in lines[1].strip().split(":")[1].split(" ") if x != ""]
wins = []
for i, time in enumerate(times):
    totalWins = 0
    for j in range(time+1):
        distance = j * (time-j)
        if distance > distances[i]:
            totalWins += 1
    wins.append(totalWins)
total = 1
for win in wins:
    total *= win

print(total)