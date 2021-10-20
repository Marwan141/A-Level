ogvalue = int(input("Please input the value of the goods: "))

if ogvalue >= 200:
    value = ogvalue * 0.9
    discount = "10%"
elif ogvalue < 199.99 and ogvalue > 100:
    value = ogvalue * 0.95
    discount = "5%"
else:
    discount = "0%"
    value = ogvalue

print("The value is " + str(ogvalue) + " The discount on your goods is " + discount + " Amount owed: " + str(value))