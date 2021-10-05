average = 0
cont = "Y"
count = 1

while cont == "Y":
    test = input("Input your test result. If you do not want to continue press 'N'. ")
    if test == "N":
        cont = "N"
    else:
        average = (average + int(test))
        tot = average / count
        print("Your average is " + str(tot))
        count += 1

if tot < 40:
    print("You have failed the year. ")
elif tot < 50:
    print("You must retake to pass the year. ")
else:
    print("You have passed. ")
     