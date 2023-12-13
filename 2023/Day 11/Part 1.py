input = [list(line.strip()) for line in open("2023\\Day 11\\input.txt").readlines()]
rows = []
col = []
for i, row in enumerate(input):
    if not "#" in row:
        rows.append(i)
    if i == 0:
        for j in range(len(input[0])):
            empty = True
            for k in range(len(input)):
                if input[k][j] == "#":
                    empty = False
            if empty:
                col.append(j)
for i, num in enumerate(rows):
    input.insert(num+i, input[num+i][:])
for i, num in enumerate(col):
    for j in range(len(input)):
        input[j].insert(num+i, ".")
galaxies = []
for y, row in enumerate(input):
    for x, square in enumerate(row):
        if square == "#":
            galaxies.append((x,y))
total = 0
counted = []
for position in galaxies:
    for galaxy in galaxies:
        if not galaxy in counted and galaxy != position:
            total += ((galaxy[0] - position[0])**2)**0.5 + ((galaxy[1] - position[1])**2)**0.5
    counted.append(position)
print(int(total))