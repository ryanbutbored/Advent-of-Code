#BRUTE FORCE FOR THE WIN
f = open("2023\\Day 6\\input.txt", "r")
lines = f.readlines()
time = int("".join([x for x in lines[0].strip().split(":")[1].split(" ") if x != ""]))
distance = int("".join([x for x in lines[1].strip().split(":")[1].split(" ") if x != ""]))
total = 0
for i in range(time):
    if i * (time-i) > distance:
        total += 1
print(total)
