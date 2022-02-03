from time import sleep
string = "TABOO"
guess = 0
correct = False
lst3 = [".", ".", ".", ".", "."]
while guess <= 5:
    lst = []
    lst2 = []
    count = 0
    counter = 0
    guess += 1
    inp = input("")
    inp = inp.upper()
    while len(inp) != 5:
        print("Please enter your guess again.")
        inp = input("")
        inp = inp.upper()

    for i in inp:
        lst.append(i)
        
    for i in string:
        lst2.append(i)
        
    for i in string:
        count += 1
        if inp[count-1] in string:
            if lst[count-1] == lst2[count-1]:
                print(lst[count-1] + " is in the right spot!")
                lst3[count-1] = lst[count-1]
                counter += 1
                print(lst3)
                sleep(1)
            else:
                print(lst[count-1] + " is in the word but not the right position.")
                print(lst3)
                sleep(1)
                
        else:
            print(lst[count-1] + " is not in the word.")
            print(lst3)
            sleep(1)
            
    if counter == 5:
        print("You guessed it!")
        guess = 6
        correct = True

if correct != True:
    print("You used up all your tries, try again next time. ")
    
        

