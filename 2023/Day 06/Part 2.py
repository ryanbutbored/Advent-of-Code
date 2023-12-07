import time as t

#BRUTE FORCE FOR THE WIN
f = open("2023\\Day 06\\input.txt", "r")
lines = f.readlines()
time = int("".join([x for x in lines[0].strip().split(":")[1].split(" ") if x != ""]))
distance = int("".join([x for x in lines[1].strip().split(":")[1].split(" ") if x != ""]))
a = t.time()
for i in range(time):
    if i * (time-i) > distance:
        break

for j in range(time-1, -1, -1):
    if j * (time-j) > distance:
        break

print(j-i+1)
print(t.time()-a)