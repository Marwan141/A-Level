import numpy as np
from array import *

park = [[],[]]
i = 0
c = 0

parking = {

}

count = 0
regnum = ""


def emptyCarPark():
    parking = {

    }

    print("The parking has been emptied. ")

def parkACar(array):
    reg = input("Please input the registration number: ")
    count =+ 1
    row = int(input("Input the row the car is parked: "))
    while row > 20:
        print("The row must be between 1 and 20")
        row = input("Input the row the car is parked: ")

    column = int(input("Input the column the car is parked in: "))
    while column > 25:
        print("The column must be between 1 and 25")
        column = input("Input the column the car is parked in: ")
    
    parking[reg] = [row,column]
    print(parking)

def removeCar(array):
    reg = input("Choose a registration number: ")
    del parking[reg]



print(" 1. Reset all spaces in the car park. \n 2. Park a car \n 3. Remove a car \n 4. Display the car park grid \n 5. Quit")
choice = int(input("Enter your choice: "))

while choice != 5:
    if choice == 1:
        emptyCarPark()
        
    elif choice == 2:
        parkACar(park)
        
    elif choice == 3:
        removeCar(park)
        print(parking)
    
    elif choice == 4:
        print(parking)
        
    choice = int(input("Choose again an option. "))

