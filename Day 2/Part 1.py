f = open("Day 2\\input.txt", "r")
lines = f.readlines()
RED = 12
GREEN = 13
BLUE = 14
total = 0
for line in lines:
    totalRed = 0
    totalGreen = 0
    totalBlue = 0
    line = line.strip().split(":")
    gameID = int(line[0].strip("Game "))
    sets = line[1].split(";")
    valid = True
    for set in sets:
        subset = set.split(",")
        for cubes in subset:
            if "red" in cubes:
                if int(cubes.replace("red", "").replace(" ", "")) > RED:
                    valid = False
            elif "green" in cubes:
                if int(cubes.replace("green", "").replace(" ", "")) > GREEN:
                    valid = False
            else:
                if int(cubes.replace("blue", "").replace(" ", "")) > BLUE:
                    valid = False
    if valid:
        total += gameID
print(total)