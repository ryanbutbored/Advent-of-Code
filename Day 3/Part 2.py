class Gear:
    def __init__(self, y, x):
        self.x = x
        self.y = y
        self.parts = []

def checkForGears(gears, y, x, num):
    if schematic[y][x] == "*":
        found = False
        for gear in gears:
            if gear.x == x and gear.y == y:
                gear.parts.append(num)
                found = True
        if not found:
            gear = Gear(y, x)
            gear.parts.append(num)
            gears.append(gear)
    return gears


def extractNumber(line, x):
    front = x
    end = x
    while front > 0 and line[front].isnumeric():
        front -= 1
    while end < len(line)-1 and line[end].isnumeric():
        end += 1
    num = line[front:end+1]
    newnum = ""
    for c in num:
        if c.isnumeric():
            newnum += c
    return int(newnum), end

f = open("Day 3\\input.txt")
schematic = f.readlines()
lineLength = len(schematic[0].strip())
allowed = "0123456789."
total = 0
gears = []

for i in range(len(schematic)):
    line = schematic[i].strip()
    j = 0
    while j < lineLength:
        counted = False
        #check each digit in each line if it is next to a symbol, if it is then extract the whole number from the line then move on to the next value after the numberS
        if line[j].isnumeric():
            if i > 0:
                if not schematic[i-1][j] in allowed:
                    num, newJ = extractNumber(line, j)
                    counted = True
                    gears = checkForGears(gears, i-1, j, num)
                if j > 0:
                    if not (schematic[i-1][j-1] in allowed or counted):
                        num, newJ = extractNumber(line, j)
                        counted = True
                        gears = checkForGears(gears, i-1, j-1, num)
                if j < lineLength-1:
                    if not (schematic[i-1][j+1] in allowed or counted):
                        num, newJ = extractNumber(line, j)
                        counted = True
                        gears = checkForGears(gears, i-1, j+1, num)
            if i < len(schematic)-1:
                if not (schematic[i+1][j] in allowed or counted):
                    num, newJ = extractNumber(line, j)
                    counted = True
                    gears = checkForGears(gears, i+1, j, num)
                if j > 0:
                    if not (schematic[i+1][j-1] in allowed or counted):
                        num, newJ = extractNumber(line, j)
                        counted = True
                        gears = checkForGears(gears, i+1, j-1, num)
                if j < lineLength-1:
                    if not (schematic[i+1][j+1] in allowed or counted):
                        num, newJ = extractNumber(line, j)
                        counted = True
                        gears = checkForGears(gears, i+1, j+1, num)
            if j > 0:
                if not (schematic[i][j-1] in allowed or counted):
                    num, newJ = extractNumber(line, j)
                    counted = True
                    gears = checkForGears(gears, i, j-1, num)
            if j < lineLength-1:
                if not (schematic[i][j+1] in allowed or counted):
                    num, newJ = extractNumber(line, j)
                    counted = True
                    gears = checkForGears(gears, i, j+1, num)
        if counted:
            j = newJ
        j += 1
for gear in gears:
    if len(gear.parts) == 2:
        total += gear.parts[0] * gear.parts[1]
print(total)