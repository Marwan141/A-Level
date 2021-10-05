width: float(input("Enter the width of the rectangle: "))
length: float(input("Enter the length of the rectangle: "))

if length == width:
    area = length * width
    print("This is a square of area " + str(area))
else:
    area = length * width
    print("This is a rectangle of area " + str(area))
