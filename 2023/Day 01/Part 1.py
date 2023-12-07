f = open("2023\\Day 01\\input.txt")
lines = f.readlines()
total = 0
for line in lines:
    #search from start of line for 1st digit
    for i in range(len(line)):
        if line[i].isnumeric():
            first = line[i]
            break
    #search from end of line for last digit
    for i in range(len(line)-1, -1, -1):
        if line[i].isnumeric():
            last = line[i]
            break
    total += int(first+last)
print(total)