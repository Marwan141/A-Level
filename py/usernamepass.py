correct = "N"

#User input
while correct == "N":
    username = input("Enter username: ")
    password = input("Enter password: ")
    ConPassword = input("Confirm password: ")
    count = 0


    #Loop through capital alphabet to check cond2
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for f in password:
        for i in alphabet:
            if f == i:
                count = count + 1
    
    #Check conditions for password
    if password == ConPassword and len(password) >= 10 and count >= 1:
        print("Welcome @" + username + ", you are succesfully signed in. ")
        correct = "Y"
    else:
        print("Please re-enter your password.")


