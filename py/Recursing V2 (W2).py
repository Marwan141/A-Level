slow = 0
medium = 0 
fast = 0

def inputdata(slow, medium, fast):
    timeTaken = int(input("Input the time taken: "))
    if timeTaken == 0:
        print(fast, medium, slow)
    elif timeTaken < 30:
        fast += 1
        inputdata(slow, medium, fast)
    elif timeTaken < 60:
        medium += 1
        inputdata(slow, medium, fast)
    else:
        slow += 1
        inputdata(slow, medium, fast)

inputdata(slow, medium, fast)