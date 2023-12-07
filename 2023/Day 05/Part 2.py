#currently all this is, is a memory leak simulator
from time import time

f = open("2023\\Day 05\\input.txt")
lines = f.readlines()
tempSeeds = [int(x) for x in lines[0].strip().split(": ")[1].split(" ")]
seeds = []
for i in range(0, len(tempSeeds), 2):
    seeds.append([tempSeeds[i], tempSeeds[i]+tempSeeds[i+1] - 1])
print("list generated")
maps = []
for line in lines[1:]:
    line = line.strip()
    if line != "" and line[0].isalpha():
        try:
            maps.append(newmap)
        except:
            pass
        newmap = []
    try:
        newmap.append([int(x) for x in line.split(" ")])
    except:
        continue
maps.append(newmap)
found = False
location = 0
a = time()
while not found:
    if location % 10000 == 0:
        print(location)
    temp = location
    for i in range(6, -1, -1):
        for values in maps[i]:
            minimum = values[0]
            maximum = values[0] + values[2] - 1
            if temp >= minimum and temp <= maximum:
                temp = values[1] - minimum + temp
                break
    for seed in seeds:
        if temp >= seed[0] and temp <= seed[1]:
            print("found", location, time()-a)
            found = True
            break
    location += 1
