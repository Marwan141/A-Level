bags = int(input("Input the number of bags: "))
sweets = int(input("Input the number of sweets: "))

if sweets > bags:
    if (sweets % 2) == 0:
        if (bags % 2) == 0:
            if (sweets % bags) == 0:
                print("Each bag will have: " + str((sweets // bags)) + " sweets")
            else:
                print("It cannot be done.")
    else:
        if (bags % 2) == 0:
            print("It cannot be done. ")
        else:
            print("It can be done ")
else:
    print("The number sweets must be larger than the number of bags. ")
