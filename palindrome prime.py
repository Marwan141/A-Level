N = 42
countadd = 0
countsub = 0
flag = False
flagsub = False
#add

strn = str(N)
for i in strn:
    print("f")
    if int(i) % 2 == 0:
        flag = True
    else:
        flag = False
    
while flag == False:
    print("k")
    new = N + 1
    print(new)
    countadd += 1
    stri = str(new)
    for i in stri:
        if int(i) % 2 == 0:
            flag = True
        else:
            flag = False

#sub
while flagsub == False:
    new = N - 1
    countsub += 1
    stri = str(new)
    for i in stri:
        if int(i) % 2 == 0:
            flagsub = True
        else:
            flagsub = False

if countsub > countadd:
    print(countadd)
else:
    print(countsub)