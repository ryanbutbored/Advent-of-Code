f = open("2015\\Day 05\\input.txt", "r")
strings = f.readlines()
count = 0
bans = ["ab", "cd", "pq", "xy"]
for string in strings:
    string = string.strip()
    doubles = False
    pairs = False
    for i in range(len(string)):
        if i < len(string) - 2:
            if string[i] == string[i+2]:
                doubles = True
        if i != len(string) - 1:
            if len(string.replace(string[i] + string[i+1], "")) < len(string) - 3:
                pairs = True
    if pairs and doubles:
        count += 1
print(count)