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

f = open("2023\\Day 03\\input.txt")
schematic = f.readlines()
lineLength = len(schematic[0].strip())
allowed = "0123456789."
total = 0
for i in range(len(schematic)):
    line = schematic[i].strip()
    j = 0
    while j < lineLength:
        counted = False
        #check each digit in each line if it is next to a symbol, if it is then extract the whole number from the line then move on to the next value after the numbers
        if line[j].isnumeric():
            if i > 0:
                if not (schematic[i-1][j] in allowed or counted):
                    num, j = extractNumber(line, j)
                    counted = True
                if j > 0:
                    if not (schematic[i-1][j-1] in allowed or counted):
                        num, j = extractNumber(line, j)
                        counted = True
                if j < lineLength-1:
                    if not (schematic[i-1][j+1] in allowed or counted):
                        num, j = extractNumber(line, j)
                        counted = True
            if i < len(schematic)-1:
                if not (schematic[i+1][j] in allowed or counted):
                    num, j = extractNumber(line, j)
                    counted = True
                if j > 0:
                    if not (schematic[i+1][j-1] in allowed or counted):
                        num, j = extractNumber(line, j)
                        counted = True
                if j < lineLength-1:
                    if not (schematic[i+1][j+1] in allowed or counted):
                        num, j = extractNumber(line, j)
                        counted = True
            if j > 0:
                if not (schematic[i][j-1] in allowed or counted):
                    num, j = extractNumber(line, j)
                    counted = True
            if j < lineLength-1:
                if not (schematic[i][j+1] in allowed or counted):
                    num, j = extractNumber(line, j)
                    counted = True
        if counted:
            total += num
        j += 1
print(total)