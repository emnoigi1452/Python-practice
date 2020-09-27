def divList(num):
    l = []
    for i in range(1, int(num / 2) + 1):
        if num % i == 0:
            l.append(i)
        else:
            pass
    return l


def perfectCheck(num):
    s = 0
    lc = divList(num)
    for j in lc:
        s += j
    if s == num:
        print("Number is perfect!")
        pass
    else:
        print("Number is not perfect!")
        pass


n = input("Enter number: ")
if n.isnumeric():
    perfectCheck(int(n))
else:
    print("Not an integer!")
    exit(-1)
