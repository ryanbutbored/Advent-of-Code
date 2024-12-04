f = open("input.txt")
lines = f.readlines()
list1 = []
list2 = []
for line in lines:
    line = line.strip().split("   ")
    list1.append(int(line[0]))
    list2.append(int(line[1]))

similarity = 0

for num in list1:
    similarity += list2.count(num) * num

print(similarity)
