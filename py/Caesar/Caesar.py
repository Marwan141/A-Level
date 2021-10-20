choice = input("Choose E for Encryption or D for Decryption: ")
message = input("Enter your message: ")
shift = int(input("Enter the shift: "))


encryptedmsg = ""
decryptedmsg = ""


def encrypt():
    newmessage = ""
    for i in message:
        newletter = ord(i) + shift
        if i == "," or i == "." or i == ":" or i == ";" or i == "[" or i == "]" or i == " " or i.isnumeric():
            newletter = ord(i)
            newmessage = newmessage + chr(newletter)
        elif i.isupper():
            if newletter >= 65 and newletter <= 90:
                newmessage = newmessage + chr(newletter)
            elif newletter > 90:
                newletter = newletter - 26
                newmessage = newmessage + chr(newletter)
        elif i.islower():
            if newletter >= 97 and newletter <= 122:
                newmessage = newmessage + chr(newletter)
            elif newletter > 122:
                newletter = newletter - 26
                newmessage = newmessage + chr(newletter)
    print(newmessage)
    encryptedmsg = newmessage
    return encryptedmsg

def decrypt():
    newmessage = ""
    for i in message:
        newletter = ord(i) - shift
        print(newletter)
        if i == "," or i == "." or i == ":" or i == ";" or i == "[" or i == "]" or i == " " or i.isnumeric():
            newletter = ord(i)
            newmessage = newmessage + chr(newletter)
        elif i.isupper():
            if newletter >= 65 and newletter <= 90:
                newmessage = newmessage + chr(newletter)
            elif newletter < 65:
                newletter = newletter + 26
                newmessage = newmessage + chr(newletter)
        elif i.islower():
            if newletter >= 97 and newletter <= 122:
                newmessage = newmessage + chr(newletter)
            elif newletter < 97:
                newletter = newletter + 26
                newmessage = newmessage + chr(newletter)
    print(newmessage)
    decryptedmsg = newmessage
    return decryptedmsg

if choice == "E":
    encryptedmsg = encrypt()
    f = open("Result.txt" , "a")
    f.write(" " + encryptedmsg + "with shift of: " + str(shift))
    f.close()

elif choice == "D":
    decryptedmsg = decrypt()
    f = open("Result.txt" , "a")
    f.write(" " + decryptedmsg + " with shift of: " + str(shift))
    f.close()
else:
    print("Invalid choice. ")
    
