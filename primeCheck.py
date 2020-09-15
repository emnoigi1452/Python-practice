val = input("Enter number: ")
if not val.isnumeric():
    print("Value is not numeric!")
else:
    pass

isPrime = True
if int(val) < 2:
    print("The value '" + val + "' is not a prime number!")
elif int(val) == 2 or int(val) == 3:
    print("The value '" + val + "' is a prime number!")
else: 
    # Run loop to check if the value is prime or not
    for x in range(2, int(val)):
        if int(val) % x == 0:
            isPrime = False
            break
        else:
            pass
    if not isPrime:
        print("The value '" + val + "' is not a prime number!")
    else:
        print("The value '" + val + "' is a prime number!")
