
attempt = 1

def getPword(attempt):
    while attempt == 1:
        password = input("Please enter your password: ")
        if len(password) >= 6 and len(password) <= 8:
            attempt = 2
        else:
            print("Your password must be between 6 and 8 characters long. ")
    while attempt == 2:
        conpassword = input("Confirm your password: ")
        if conpassword == password:
            print("Password changed succesfully. ")
            attempt = 3
        else:
            print("The passwords do not match. ")
            attempt = 1
            while attempt == 1:
                password = input("Please enter your password: ")
                if len(password) >= 6 and len(password) <= 8:
                    attempt = 2


getPword(attempt)