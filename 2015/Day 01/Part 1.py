f = open("2015\\Day 01\\input.txt")
line = f.readline()
total = 0
for c in line:
    if c == "(":
        total += 1
    elif c == ")":
        total -= 1

print(total)