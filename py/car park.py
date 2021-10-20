import numpy as np
from array import *

park = [[],[]]
i = 0
c = 0


#while i <= 19:
    #i = i + 1
    #park[0].append(i)

#while c <= 24:
    #c = c + 1
    #park[1].append(c)

def emptyCarPark():
    carpark = np.empty_like(park)
    print(carpark)

def parkACar(array):
    reg = input("Please input the registration number: ")
    row = input("Input the row the car is parked: ")
    column = input("Input the column the car is parked in: ")
    park[0].append(row)
    park[1].append(column)

print(" 1. Reset all spaces in the car park. \n 2. Park a car \n 3. Remove a car \n 4. Display the car park grid \n 5. Quit")
choice = int(input("Enter your choice: "))

while choice != 5:
    if choice == 1:
        emptyCarPark()
        choice = 5
    elif choice == 2:
        parkACar(park)



print(park)

