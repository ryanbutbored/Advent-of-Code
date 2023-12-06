f = open("2023\\Day 2\\input.txt", "r")
lines = f.readlines()
total = 0
for line in lines:
    maxRed = 0
    maxGreen = 0
    maxBlue = 0
    line = line.strip().split(":")
    sets = line[1].split(";")
    for set in sets:
        subset = set.split(",")
        for cubes in subset:
            if "red" in cubes:
                if int(cubes.replace("red", "").replace(" ", "")) > maxRed:
                    maxRed = int(cubes.replace("red", "").replace(" ", "")) 
            elif "green" in cubes:
                if int(cubes.replace("green", "").replace(" ", "")) > maxGreen:
                    maxGreen = int(cubes.replace("green", "").replace(" ", ""))
            else:
                if int(cubes.replace("blue", "").replace(" ", "")) > maxBlue:
                    maxBlue = int(cubes.replace("blue", "").replace(" ", ""))
    power = maxRed * maxGreen * maxBlue
    total += power
print(total)