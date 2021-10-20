
def fizzbuzz(x):
    for i in range(x + 1):
        if i == 0:
            pass
        elif (i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        elif (i % 3 == 0):
            print("Fizz")
        elif (i % 5 == 0):
            print("Buzz")
        else:
            print(i)
            
    
fizzbuzz(500)