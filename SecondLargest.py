def secondLargest(ar):
    if (len(ar)) == 0:
        l = 0
        l2 = 0
        pass
    else:
        l = ar[0]
        l2 = ar[0]
        for n in range(0, len(ar) - 1):
            if l < ar[n]:
                l = ar[n]
        for i in range(0, len(ar) - 1):
            if l2 < ar[i] < l:
                l2 = ar[i]
        return l2


ray = []
print("Input array elements (Type nothing to end): ")
while True:
    reader = input("")
    if reader.isnumeric():
        ray.append(int(reader))
    elif not reader.isnumeric() and len(reader) != 0:
        print("Input is not integer!")
        exit(-1)
    elif len(reader) == 0:
        break
print(str(ray))
print("Second largest value in array: " + str(secondLargest(ray)))