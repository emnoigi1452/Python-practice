userInput = input("Enter number amount: ")
numberList = []
if not userInput.isnumeric():
    print("Number amount has to be a valid integer!")
    exit(-1)
else:
    for i in range(0, int(userInput)):
        inputNum = input("")
        if not inputNum.isnumeric():
            print("Value is not numeric!")
            exit(-1)
        else:
            numberList.append(int(inputNum))


            def greatestVal():
                greatest = numberList[0]
                for x in numberList:
                    if greatest < x:
                        greatest = x
                return greatest


            def smallestVal():
                smallest = numberList[0]
                for z in numberList:
                    if smallest > z:
                        smallest = z
                return smallest


            def averageVal():
                n = 0
                for j in numberList:
                    n += j
                return n / len(numberList)

print("Given list of numbers: " + str(numberList))
print("Length: " + str(len(numberList)) + " elements")
print("Larges value: " + str(greatestVal()))
print("Smallest value: " + str(smallestVal()))
print("Average value: " + str(averageVal()))
