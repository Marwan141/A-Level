num1 = 3
num2 = 5
final = []
total = 0
for i in range(0,1000):
    if i % num1 == 0 or i % num2 == 0:
        final.append(i)

for i in final:
    total = total + i
print(total)
