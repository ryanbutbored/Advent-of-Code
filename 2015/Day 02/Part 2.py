f = open("2015\\Day 02\\input.txt")
boxes = [[int(x) for x in line.strip().split("x")] for line in f.readlines()]
total = 0
for box in boxes:
    t = box[0] * box[1] * box[2]
    n = min(box)
    box.pop(box.index(n))
    t += (2 * n) +(2 * min(box))
    total += t
print(total)