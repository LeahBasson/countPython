lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
theSum = 1

for number in range (lower, upper + 1):
    printText = f"{theSum + number} = {theSum} + {number}"
    theSum += number # short form of expression, its the same as theSum = theSum + number
    
    print(printText)
print(f"The cummulated value is {theSum}")