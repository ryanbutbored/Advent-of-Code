f = open("2015\\Day 05\\input.txt", "r")
strings = f.readlines()
count = 0
bans = ["ab", "cd", "pq", "xy"]
for string in strings:
    doubles = False
    vowelCount = 0
    banned = False
    for i in range(len(string.strip())):
        if i != len(string.strip()) - 1:
            if string[i] == string[i+1]:
                doubles = True
        if string[i] in "aeiou":
            vowelCount += 1
    for ban in bans:
        if ban in string:
            banned = True
    if vowelCount > 2 and doubles and not banned:
        count += 1
print(count)