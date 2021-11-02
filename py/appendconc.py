import datetime
import math

def appendToList(n):
    alist = []
    t0 = datetime.datetime.now()
    for i in range(n):
        alist.append(i)
    t1 = datetime.datetime.now()
    runtime = (t1 - t0) 
    print(runtime, "time taken to append")

def concatenateList(n):
    alist = []
    t0 = datetime.datetime.now()
    for i in range(n):
        alist = alist + [i]
    t1 = datetime.datetime.now()
    runtime = (t1 - t0)
    print(runtime, "time taken to concatenate")

k = int(input("How many items do u want to add to ur list"))
appendToList(k)
concatenateList(k)
quit = input()



