number = int(input("Input your number: "))
strnum = str(number)
length = len(strnum)
newnumber = ""
count = 0


for num in strnum:
    count = count + 1
    newnumber = newnumber + strnum[length - count]


if newnumber == strnum:
    print("This is a Palindrome number. ")
else:
    print("This is not a Palindrome number. ")

