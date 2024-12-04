f = open("input.txt")
lines = f.readlines()
list1 = []
list2 = []
for line in lines:
    line = line.strip().split("   ")
    list1.append(int(line[0]))
    list2.append(int(line[1]))
list1.sort(reverse = True)
list2.sort(reverse = True)

distance = 0

for i, num in enumerate(list1):
    num2 = list2[i]
    if num > list2[i]:
        distance += num - num2
    else:
        distance += num2 - num

print(distance)
        
