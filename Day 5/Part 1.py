f = open("Day 5\\input.txt")
lines = f.readlines()
seeds = [int(x) for x in lines[0].strip().split(": ")[1].split(" ")]
maps = []
for line in lines[1:]:
    line = line.strip()
    if line != "" and line[0].isalpha():
        try:
            maps.append(newmap)
        except:
            pass
        newmap = []
    try:
        newmap.append([int(x) for x in line.split(" ")])
    except:
        continue
maps.append(newmap)
i = 0
while i < len(seeds):
    for j in range(7):
        seed = seeds[i]
        for values in maps[j]:
            minimum = values[1]
            maximum = values[1] + values[2] - 1
            if seed >= minimum and seed <= maximum:
                seeds[i] = values[0] - minimum + seed
                break
    i += 1
print(min(seeds))