inp = int(input("Input number to check: "))
b = inp
t = 0
level = len(str(round(inp)))
while inp > 0:
    t += (inp % 10) ** level
    inp = (inp - (inp % 10)) / 10
print("Check result: ", end=str(b is int(t)))

