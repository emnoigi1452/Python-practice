# Create function to add all integers to the list
def getNumbers(digits):
    numList = []
    for num in range(10 ** (int(digits) - 1), 10 ** int(digits)):
        if num % 11 == 0:
            numList.append(num)
    return numList


# Input digit count made by user, display all integers with this amount of digits
i = input("Enter digit count: ")
count = 0
if not i.isnumeric():
    print("Inputted value has to be numeric!")
    exit(-1)
else:
    if int(i) >= 10 or int(i) < 2:
        print("Digits count has to be between 2 and 9!")
        exit(-1)
    else:
        multiplesList = getNumbers(int(i))
        for d in multiplesList:
            if d is multiplesList[len(multiplesList) - 1]:
                print(d, end=". \n")
                count += 1
            else:
                print(d, end=", ")
                count += 1
        else:
            print("Process ends with " + str(count) + " results")
