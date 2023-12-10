from math import lcm
f = open("2023\\Day 08\\input.txt")
lines = f.readlines()
directions = lines[0].strip()
map = {}
for line in lines[2:]:
    line = line.strip().split(" = ")
    map[line[0]] = line[1].replace("(", "").replace(")", "").split(", ")

current = [x for x in map.keys() if x[2] == "A"]
counts = []
for node in current:
    i = 0
    counter = 0
    found = False
    while not found:
        if i == len(directions):
            i = 0
        if directions[i] == "L":
            index = 0
        else:
            index = 1
        node = map[node][index]
        i += 1
        counter += 1
        if node[2] == "Z":
            counts.append(counter)
            found = True

print(lcm(*counts))
