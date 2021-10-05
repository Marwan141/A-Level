import math

choice = input("Choose what shape you want to calculate the area for: T for Triangle, C for Circle and R for rectangle ")



if choice == "T":
    base = float(input("Enter the base of the triangle: "))

    height = float(input("Enter the height of the triangle: "))

    area = 0.5*base*height

    print("The area of the triangle is: " + str(area))
elif choice == "C":

    radius = float(input("Enter the radius of the circle: "))

    area = math.pi*radius**2

    print("The area of the circle is: " + str(area))
elif choice == "R":
    width = float(input("Enter the width of the rectangle: "))

    length = float(input("Enter the length of the rectangle: "))

    area = length*width

    print("The area of the rectangle is: " + str(area))