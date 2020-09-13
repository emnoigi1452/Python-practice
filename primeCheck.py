val = input("Enter number: ")
isPrime = True
if not val.isnumeric():
    print("Value is not numeric!")
else:
    for x in range(2, int(val) // 2):
        if int(val) % x == 0:
            isPrime = False
            break

if isPrime:
    displayStr = "{} is a prime number!"
    print(displayStr.format(val))
else:
    displayStr = "{} is not a prime number!"
    print(displayStr.format(val))
