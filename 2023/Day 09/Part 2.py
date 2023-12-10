#got really lazy with variable names on this one too (copy paste for the win)
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
        temp1[i].insert(0, temp1[i][0] - temp1[i+1][0])
    numbers.append(temp1[0][0])
print(sum(numbers))
