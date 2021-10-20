print("""Menu  
1. Music
2. History 
3. Design and Technology
4. Exit""")

choice = int(input("Please enter your choice: "))

if choice == 1:
    print("You chose Music.")
elif choice == 2:
    print("You chose History.")
elif choice == 3:
    print("You chose Design and Techonology.")
elif choice == 4:
    print("Goodbye.")
else:
    print("Choose a valid number. ")