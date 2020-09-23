def reverseArray(default):
    if len(default) == 0:
        print("Array is empty!")
        pass
    else:
        rAr = []
        for k in range(len(default) - 1, -1, -1):
            rAr.append(default[k])
        return rAr


ar = []
reverse = []
print("Input array elements - Type nothing to stop: ")
while True:
    i = input("")
    if not i.isnumeric() and len(i) != 0:
        print("Input has to be numeric!")
        exit(-1)
    elif len(i) == 0:
        break
    else:
        ar.append(int(i))
print("Given array: " + str(ar))
reverse = reverseArray(ar)
print("Reversed array: " + str(reverse))
