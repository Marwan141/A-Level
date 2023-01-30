numOfNum = int(input("Enter the number of numbers you want to compare: "))
listOfNum = []
for i in range(0, numOfNum):
    inp = int(input("Enter a number:"))
    listOfNum.append(inp)
maxi = 0
maxnum = 0
for i in listOfNum:
    if listOfNum.count(i) > maxi:
        maxi = listOfNum.count(i)
        maxnum = i
        sad = False
    elif listOfNum.count(i) == maxi and i != maxnum:
        sad = True

if sad == True:
    print("Data was multimodal")
else:
    print("The most frequent number was: " + str(maxnum))
    print("It was entered: " + str(maxi) + " times")
