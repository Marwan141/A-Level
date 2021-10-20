premileage = int(input("Please input the mileage that the car had when it was last filled: "))
mileage = int(input("Please input the mileage of your car now: "))
total = int(input("Enter the number of litres taken to fill your tank: "))


gallon = total * 0.22

diff = mileage - premileage

milepergallon = diff / gallon

print("The number of miles per gallon your car is doing is: " +  str(milepergallon))
