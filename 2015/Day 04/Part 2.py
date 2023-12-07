import hashlib
import time

f = open("2015\\Day 04\\input.txt")
letters = f.readlines()
i = 0
a = time.time()
while True:
    newstring = letters[0] + str(i)
    if hashlib.md5(newstring.encode("ascii")).hexdigest()[0:6] == "000000":
        print(i)
        print("took", time.time()-a, "seconds")
        break
    i += 1