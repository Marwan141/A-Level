name = input("Enter your name: " "\n")
print("Enter times table, start number and end number: ")

table = int(input())
startnum = int(input())
endnum = int(input())

def multiples(table, startnum, endnum, pupilName):
    print("Hello, " + pupilName + "..." + " here is your times table.")
    for i in range(startnum, (endnum + 1)):
        print(str(startnum) + " x " + str(i) + " = " + str(startnum * i) )

multiples(table, startnum, endnum, name)