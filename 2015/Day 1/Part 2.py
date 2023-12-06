f = open("2015\\Day 1\\input.txt")
line = f.readline()
total = 0
counter = 1
for c in line:
    if c == "(":
        total += 1
    elif c == ")":
        total -= 1
    if total == -1:
        print(counter)
    counter += 1

print(counter)