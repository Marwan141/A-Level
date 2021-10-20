choice = input("Choose C for Celcius to Fahrenheit, Choose F for Celcius to Fahrenheit: ")

if choice == "C":
    firsttemperature = float(input("Enter the 1st temperature: "))
    secondtemperature = float(input("Enter the 2nd temperature: "))
    thirdtemperature = float(input("Enter the 3rd temperature: "))
    fourthtemperature = float(input("Enter the 4th temperature: "))
    fifthtemperature = float(input("Enter the 5th temperature: "))

    print("Your first temperature is: " + str((firsttemperature * 9/5)))
    print("Your second temperature is: " + str((secondtemperature * 9/5)))
    print("Your third temperature is: " + str((thirdtemperature * 9/5)))
    print("Your fourth temperature is: " + str((fourthtemperature * 9/5)))
    print("Your fifth temperature is: " + str((fifthtemperature * 9/5)))
elif choice == "F":
    firsttemperature = float(input("Enter the 1st temperature: "))
    secondtemperature = float(input("Enter the 2nd temperature: "))
    thirdtemperature = float(input("Enter the 3rd temperature: "))
    fourthtemperature = float(input("Enter the 4th temperature: "))
    fifthtemperature = float(input("Enter the 5th temperature: "))

    print("Your first temperature is: " + str(((firsttemperature - 32) * 5/9)))
    print("Your second temperature is: " + str(((secondtemperature - 32) * 5/9)))
    print("Your third temperature is: " + str(((thirdtemperature - 32) * 5/9)))
    print("Your fourth temperature is: " + str(((fourthtemperature - 32) * 5/9)))
    print("Your fifth temperature is: " + str(((fifthtemperature - 32) * 5/9)))
else:
    print("Please choose a right letter. ")