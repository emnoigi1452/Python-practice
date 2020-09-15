def pcheck(num):
    isPrime = True
    if num < 2:
        return False
    else:
        for x in range(2, num):
            if num % x == 0:
                isPrime = False
                break
    return isPrime


def plist(start, end):
    l = []
    for i in range(start, end):
        if pcheck(i):
            l.append(i)
    return l


s = input("Get start value: ")
if not s.isnumeric():
    print("Value has to be numeric")
else:
    pass

e = input("Get end value: ")
if not e.isnumeric():
    print("Value has to be numeric!")
else:
    pass

getcount = 0

displayList = plist(int(s), int(e))
for k in displayList:
    if k is not displayList[-1]:
        if getcount % 10 == 0 and getcount != 0:
            print(k, end=", \n")
            getcount += 1
        else:
            print(k, end=", ")
            getcount += 1

    else:
        print(k, end=".\n")
        getcount += 1
print("Process end - Found " + str(getcount) + " prime values within the given range")
