s = input()
lst = []

for i in s:
    lst += i.lower()
reversed_list = lst[::-1]

if lst == reversed_list:
    print(True)
else:
    print(False)
