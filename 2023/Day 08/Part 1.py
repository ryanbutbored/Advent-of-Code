f = open("2023\\Day 08\\input.txt")
lines = f.readlines()
directions = lines[0].strip()
map = {}
for line in lines[2:]:
    line = line.strip().split(" = ")
    map[line[0]] = line[1].replace("(", "").replace(")", "").split(", ")
current = "AAA"
target = "ZZZ"
counter = 0
i = 0
while current != target:
    if i == len(directions):
        i = 0
    if directions[i] == "L":
        current = map[current][0]
    else:
        current = map[current][1]
    i += 1
    counter += 1
print(counter)