#can't use a queue system unless you have a quantum computer unfortunately so this works well

f = open("Day 4\\input.txt")
cards = []
lines = f.readlines()
for line in lines:
    numbers = line.strip().split(":")[1].split("|")
    winning = []
    for num in numbers[0].split(" "):
        if num != "":
            winning.append(num)
    chosen = []
    for num in numbers[1].split(" "):
        if num != "":
            chosen.append(num)
    cards.append([winning, chosen, 1])

for i in range(len(cards)):
    card = cards[i]
    winning = card[0]
    chosen = card[1]
    amount = card[2]
    wins = 0
    for num in chosen:
        if num in winning:
            wins += 1
    if wins > 0:
        for j in range(1, wins+1):
            cards[i+j][2] += amount

total = 0
for card in cards:
    total += card[2]

print(total)

