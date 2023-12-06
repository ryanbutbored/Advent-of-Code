def changePosition(currentX, currentY, instruction):
    match instruction:
        case ">":
            currentX += 1
        case "<":
            currentX -= 1
        case "^":
            currentY += 1
        case "v":
            currentY-= 1
    return currentX, currentY

class House:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.presents = 1

houses = [House(0,0)]

f = open("2015\\Day 03\\input.txt")
instructions = f.readline()
currentX = 0
currentY = 0
currentRX = 0
currentRY = 0

for i, instruction in enumerate(instructions):
    if i % 2 == 0:
        currentX, currentY = changePosition(currentX, currentY, instruction)
        found = False
        for house in houses:
            if currentX == house.x and currentY == house.y:
                house.presents += 1
                found = True
        if not found:
            houses.append(House(currentX, currentY))
    else:
        currentRX, currentRY = changePosition(currentRX, currentRY, instruction)
        found = False
        for house in houses:
            if currentRX == house.x and currentRY == house.y:
                house.presents += 1
                found = True
        if not found:
            houses.append(House(currentRX, currentRY))

print(len(houses))
