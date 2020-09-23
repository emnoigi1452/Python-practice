def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


i = input("Enter number: ")
if not i.isnumeric():
    print("Please enter a valid numeric value!")
    exit(-1)
else:
    print("The " + i + "th value in the sequence is " + str(fibonacci(int(i))))
