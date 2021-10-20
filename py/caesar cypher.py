#Choice of encryption or decryption
correct = "N"
while correct == "N":
    choice = input("Press 'E' for encryption or Press 'D' for decryption ")
    if choice == "E" or choice == "D":
        correct = "Y"

correctsign = "N"
correctsh = "N"

#Checks if signs are correct
while correctsign == "N":
    positiveornegative = input("Input '+' for a positive key or '-' for a negative key ")
    if positiveornegative == "+" or "-":
        correctsign = "Y"

#Checks if range of number is correct
while correctsh == "N":
    shift = int(input("Please input the key shift between 1 and 25 "))
    if shift >= 1 and shift <= 25:
        correctsh = "Y" 

#Message to be encrypted or decrypted
message = input("Please enter the message you want to encrypt or decrypt ")
length = len(message) - 1
secretMessageE = ""
secretMessageD = ""

#Encryption of message
if choice == "E":
    for character in message:
        number = ord(character)
        if character.lower() in 'abcdefghijklmnopqrstuvwxyz':
            number += shift

            if character.isupper(): 
                if number > ord('Z'):
                    number -= 26
                elif number < ord('A'):
                    number += 26
                else:
                    if number > ord('z'):
                        number -= 26
                    elif number < ord('a'):
                        number += 26
                        secretMessageE = secretMessageE + chr(number)
                    else:
                        secretMessageE = secretMessageE + character

#Decryption of message
elif choice == "D":
    for character in message:
        number = ord(character)
        if character.lower() in 'abcdefghijklmnopqrstuvwxyz':
            number += shift
            if character.isupper(): 
                if number > ord('Z'):
                    number -= 26
                elif number < ord('A'):
                    number += 26
                else:
                    if number > ord('z'):
                        number -= 26
                    elif number < ord('a'):
                        number += 26
                        secretMessageD = secretMessageD + chr(number)
                    else:
                        secretMessageD = secretMessageD + character
print(secretMessageD)
            