f = open("2015\\Day 2\\input.txt")
boxes = [[int(x) for x in line.strip().split("x")] for line in f.readlines()]
total = 0
for box in boxes:
    t = (2 * box[0] * box[1]) + (2 * box[0] * box[2]) + (2 * box[1] * box[2])
    n = min(box)
    box.pop(box.index(n))
    t += n * min(box)
    total += t
print(total)