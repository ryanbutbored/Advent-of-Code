def searchLine(line, allowed):
    #find lowest occurence of any number (digit or word)
    lowIndex = 99999999
    first = None
    for possibility in allowed:
        try:
            newIndex = line.index(possibility)
            if newIndex < lowIndex:
                lowIndex = newIndex
                temp = allowed.index(possibility)
                #convert index to correct digit
                if temp > 8:
                    first = str(temp-8)
                else:
                    first = str(temp+1)
        except:
            continue
    return first

f = open("2023\\Day 01\\input.txt")
lines = f.readlines()
total = 0
allowed = list("123456789") + ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
#by reversing the line and all the search parameters, you will find the last digit with exactly the same method
revAllowed = list("123456789")
for i in range(9,18):
    revAllowed.append(allowed[i][::-1])

for line in lines:
   total += int(searchLine(line, allowed) + searchLine(line[::-1], revAllowed))
print(total)