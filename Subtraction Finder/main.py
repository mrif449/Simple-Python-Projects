print("Take a 3 digit Number.")
print()
print("Your 3 digits can not be same, at least one digit should be different")
print()
conf1 = input("If Done, enter 'y': ")
if conf1 == 'y':
    print("Let's reverse the digit of your number")
    print("Such as, if you had taken 456, make it 654")
    print("Done?")
    print()
    print("Now subtract the reversed number from your chosen number")
    print("Example (456-654)")
    number = int(input("Enter the first or last digit of your number(if it is a 2 digit number enter 0): "))
    if number != 0:
        print("Is it the last or first digit?")
        digit = input("if last digit then enter 'l', else enter 'f': ")
        if digit == 'l':
            print("Was your reversed number greater than your choosed number?")
            yes_no = input("if Yes, enter 'y', else enter 'n': ")
            if yes_no == 'y':
                result1 = str((number-9))
                result2 = result1+str(9)+str(number)
                print("Your subtraction result is: ",result2)
            else:
                result1 = str((9-number))
                result2 = result1 + str(9) + str(number)
                print("Your subtraction result is: ", result2)
        else:
            print("Was your enterd first or last digit has (-) before?")
            yes_no = input("if Yes, enter 'y', else enter 'n': ")
            if yes_no == 'n':
                result1 = str((9-number))
                result2 = str(number)+str(9)+result1
                print("Your subtraction result is: ", result2)
            else:
                result1 = str((9 - number))
                result2 = "-"+str(number)+str(9)+result1
                print("Your subtraction result is: ", result2)
    else:
        conf2= input("If your substracted number has (-) before enter 'y', else enter 'n':")
        if conf2 == 'n':
            print("Your subtraction result is: 99")
        else:
            print("Your subtraction result is: -99")

else:
    print("Take a number and start again.")