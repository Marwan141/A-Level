stri = " "
total = 0

for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
            stri = stri + str(i) + str(j) + str(k)
            total = i**3 + j**3 + k**3
            if int(stri) == total:
                print(stri)
                print(total)
