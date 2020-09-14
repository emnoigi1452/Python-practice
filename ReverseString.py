def rStr(string):
    rstr = ""
    for x in range(len(string) - 1, -1, -1):
        rstr += string[x]
    return rstr


i = input("String: ")
print("Reverse: " + rStr(i))
