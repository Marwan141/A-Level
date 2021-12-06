area = float(input("Input the area of the room in m^2 : "))
unpaintable = float(input("Input the unpaintable area of the room: "))
coats = int(input("Input the number of coats of paint required: "))

ltrs = (area - unpaintable) / 11

total = ltrs * coats

print("The total amount of litres you need to pain the room is: " + str(total) + " liters." )