st = input()
word = input()
cc = 0
totalstr = ""

if (word.upper() in st) or (word.lower() in st) or (word in st):
    for i in st:
        if i == " ":
            cc += 1
            if totalstr == word or totalstr.upper() == word or totalstr.lower() == word:
                print("The position is " + str(cc))
            totalstr = ""
        else:
            totalstr = totalstr + i
            
    if totalstr == word or totalstr.upper() == word or totalstr.lower() == word:
                print("The position is " + str(cc + 1))
else:
    print("The word is not in the string. ")
