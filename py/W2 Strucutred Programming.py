slow = 0
medium = 0
fast = 0

boool = True

while boool:
     timeTaken = int(input("Enter the time taken: "))
     if timeTaken == 0:
        print(fast, medium, slow)
        boool = False
     elif timeTaken < 30:
        fast += 1
     elif timeTaken < 60:
        medium += 1
     else:
        slow += 1


