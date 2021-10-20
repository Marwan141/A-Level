students = int(input("Please input the number of student that will be dividing the books: "))
books = int(input("Please input the number of books: "))

even = False

numbooks = books // students
bookspstudent = books % students


boks = bookspstudent

while even == False:
    if bookspstudent > 0:
        books = books - 1
        bookspstudent = books % students
        print("Every student will have " + str(int(numbooks)) + " books, with "  + str(boks) + " left" )

    else:
        even = True
        print("Every student will have " + str(int(numbooks)) + " books")
