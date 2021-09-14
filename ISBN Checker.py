code = int(input("Input the ISBN number: "))
num = 0
newNum = 0

checkNum = 0

if len(str(code)) == 13:
    for i in str(code):
        num = num + 1
        if (num % 2) == 0:
            newNum = newNum + (int(i) * 3)
        elif num == 13:
            checkNum = i
        else:
            newNum = newNum + int(i) 


checker = (newNum % 10) - 10


if checker or -checker  == checkNum:
    print("The ISBN number is valid. ")
    