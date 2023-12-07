import hashlib

f = open("2015\\Day 04\\input.txt")
letters = f.readlines()
i = 0
while True:
    newstring = letters[0] + str(i)
    if hashlib.md5(newstring.encode("ascii")).hexdigest()[0:5] == "00000":
        print(i)
        break
    i += 1