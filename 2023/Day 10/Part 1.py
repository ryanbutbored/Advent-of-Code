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
path = []
while currentPipe != "S":
    path.append([x, y])
    coordsChange = [oldX-x, oldY-y]
    coordsChange = pipes[currentPipe][pipes[currentPipe].index(coordsChange)-1]
    oldX, oldY = x, y
    x = x + coordsChange[0]
    y = y + coordsChange[1]
    currentPipe = map[y][x]
print((len(path)//2)+1)