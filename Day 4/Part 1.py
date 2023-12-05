f = open("Day 4\\input.txt")
cards = f.readlines()
total = 0
for card in cards:
    numbers = card.strip().split(":")[1].split("|")
    winning = []
    for num in numbers[0].split(" "):
        if num != "":
            winning.append(num)
    chosen = []
    for num in numbers[1].split(" "):
        if num != "":
            chosen.append(num)
    first = True
    points = 0
    for num in chosen:
        if num in winning:
            if first:
                first = False
                points = 1
            else:
                points *= 2
    total += points
print(total)