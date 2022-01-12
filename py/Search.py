listt = ["Anna", "Jon", "Ata"]
name = input("Enter the name: ")

found = False

n = 0
while n < len(listt):
    for i in listt:
        n += 1
        if i == name:
            print(i)
            found = True

if found == False:
    print(-1)