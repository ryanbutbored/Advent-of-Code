f = open("2023\\Day 10\\input.txt")
map = [list(line.strip()) for line in f.readlines()]
for i, line in enumerate(map):
    if "S" in line:
        y = i-1
        break
x = line.index("S")
currentPipe = "|"
oldX = x 
oldY = y+1
pipes = {"|":[[0, 1], [0, -1]],
         "-":[[1, 0], [-1, 0]],
         "L":[[1, 0], [0, -1]],
         "J":[[-1, 0], [0, -1]],
         "7":[[-1, 0], [0, 1]],
         "F":[[1, 0], [0, 1]]}
path = [[oldX, oldY]]
while currentPipe != "S":
    path.append([x, y])
    coordsChange = pipes[currentPipe][pipes[currentPipe].index([oldX-x, oldY-y])-1]
    oldX, oldY = x, y
    x = x + coordsChange[0]
    y = y + coordsChange[1]
    currentPipe = map[y][x]

count = 0
for y, row in enumerate(map):
    cross = 0
    for x in range(len(row)):
        if [x, y] in path and map[y][x] in ["S", "|", "L", "J"]:
            cross += 1
            continue
        if not [x, y] in path and cross % 2 == 1:
            count += 1
print(count)