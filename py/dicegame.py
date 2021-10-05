import random

dice1 = random.randint(1,6)
print("Your first throw is: " + str(dice1))
dice2 = random.randint(1,6)
print("Your second throw is: " + str(dice2))

summ = dice1 + dice2
if dice1 == dice2:
    score = summ*2
    print("You threw a double, " + "your score is " + str(score))
else:
    print("Your score is " + str(summ))