num1 = int(input("Input your first number. "))
num2 = int(input("Input your second number. "))

if num1 > num2:
    print(num1)
else:
    print(num2)
count = 0
mcount = 0
word = "man"
sentence = "give a man a fish and you feed him for a day, teach a man to fish and you feed him for a lifetime"

ggg = True

while ggg == True:
    if word in sentence:
        mcount += 1
        if mcount > len(sentence):
            ggg = False

print(mcount)