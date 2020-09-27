def reverseInt(num):
    x = ""
    if int(num) < 0:
        for i in range(len(num) - 1, 0, -1):
            x += num[i]
        return int(x) * -1
    else:
        for i in range(len(num) - 1, -1, -1):
            x += num[i]
        return int(x)


n = input("Enter number: ")
e = 0
try:
    print(str(reverseInt(n)))
except:
    print("Error occurred!")
    e += 1
finally:
    print("Executed with " + str(e) + " errors")
