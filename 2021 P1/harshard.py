inpNum = int(input("Enter the nth number you want."))
notFound = True
currentNum = 0
whichHarsh = 0
while notFound:
    total = 0
    spltList = []
    currentNum += 1
    for x in str(currentNum):
        spltList.append(x)
    for n in spltList:
        total += int(n)
    if (currentNum % total) == 0:
        whichHarsh += 1
        if whichHarsh == inpNum:
            notFound = False

print(currentNum)
