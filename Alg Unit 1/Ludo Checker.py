ccnum = input("Please input your Credit Card number: ")
count = 0
corr = False
sumcc = 0


if len(ccnum) == 16:
    corr = True


while count <= 16:
    if corr == True:
        for i in ccnum:
            double = 0
            count = count + 1
            if (count % 2) == 0:
                sumcc = sumcc + int(i)
            else:
                double = int(i) * 2
                if double > 9:
                    double = double - 9
                    sumcc = sumcc + double
                else:
                    sumcc = sumcc + double

sumcc = sumcc / 2

if (sumcc % 10) == 0:
    print("Your credit card number is valid! ")
else:
    print("Please try again! Your credit card number does not seem to be valid. ")
