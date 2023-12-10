#got really lazy with variable names on this one
f = open("2023\\Day 09\\input.txt")
sequences = [[int(x) for x in line.strip().split(" ")] for line in f.readlines()]
numbers = []
for sequence in sequences:
    temp1 = [sequence]
    while temp1[-1] != [0 for j in range(len(temp1[-1]))]:
        length = len(temp1[-1])
        temp2 = []
        for i in range(length-1):
            temp2.append(temp1[len(temp1)-1][i+1] - temp1[len(temp1)-1][i])
        temp1.append(temp2)
    for i in range(len(temp1)-3, -1, -1):
        temp1[i].append(temp1[i][-1] + temp1[i+1][-1])
    numbers.append(temp1[0][-1])
print(sum(numbers))
