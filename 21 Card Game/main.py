
icons = "♠ ♥ ♦"
result = ""
r1  = " _____\n|♠    |\n|     |\n|    A|\n ¯¯¯¯¯ "
r2  = " _____\n|♠    |\n|     |\n|    K|\n ¯¯¯¯¯ "
r3  = " _____\n|♠    |\n|     |\n|    Q|\n ¯¯¯¯¯ "
r4  = " _____\n|♠    |\n|     |\n|    J|\n ¯¯¯¯¯ "
r5  = " _____\n|♠    |\n|     |\n|    2|\n ¯¯¯¯¯ "
r6  = " _____\n|♠    |\n|     |\n|    3|\n ¯¯¯¯¯ "
r7  = " _____\n|♠    |\n|     |\n|    4|\n ¯¯¯¯¯ "
r8  = " _____\n|♦    |\n|     |\n|    A|\n ¯¯¯¯¯ "
r9  = " _____\n|♦    |\n|     |\n|    K|\n ¯¯¯¯¯ "
r10 = " _____\n|♦    |\n|     |\n|    Q|\n ¯¯¯¯¯ "
r11 = " _____\n|♦    |\n|     |\n|    J|\n ¯¯¯¯¯ "
r12 = " _____\n|♦    |\n|     |\n|    2|\n ¯¯¯¯¯ "
r13 = " _____\n|♦    |\n|     |\n|    3|\n ¯¯¯¯¯ "
r14 = " _____\n|♦    |\n|     |\n|    4|\n ¯¯¯¯¯ "
r15 = " _____\n|♥    |\n|     |\n|    A|\n ¯¯¯¯¯ "
r16 = " _____\n|♥    |\n|     |\n|    K|\n ¯¯¯¯¯ "
r17 = " _____\n|♥    |\n|     |\n|    Q|\n ¯¯¯¯¯ "
r18 = " _____\n|♥    |\n|     |\n|    J|\n ¯¯¯¯¯ "
r19 = " _____\n|♥    |\n|     |\n|    2|\n ¯¯¯¯¯ "
r20 = " _____\n|♥    |\n|     |\n|    3|\n ¯¯¯¯¯ "
r21 = " _____\n|♥    |\n|     |\n|    4|\n ¯¯¯¯¯ "

#==========================================================================================================
print("Welcome to the 21 Card Game")
inp1 = input("Press Enter to continue...")
if inp1 == "":
    print("Here are 21 cards. Choose any card you like:")
    print()
    print(" _____    _____    _____    _____    _____    _____    _____")
    print("|♠    |  |♠    |  |♠    |  |♠    |  |♠    |  |♠    |  |♠    |")
    print("|     |  |     |  |     |  |     |  |     |  |     |  |     |")
    print("|    A|  |    K|  |    Q|  |    J|  |    2|  |    3|  |    4|")
    print(" ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯ ")
    print(" _____    _____    _____    _____    _____    _____    _____")
    print("|♦    |  |♦    |  |♦    |  |♦    |  |♦    |  |♦    |  |♦    |")
    print("|     |  |     |  |     |  |     |  |     |  |     |  |     |")
    print("|    A|  |    K|  |    Q|  |    J|  |    2|  |    3|  |    4|")
    print(" ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯ ")
    print(" _____    _____    _____    _____    _____    _____    _____")
    print("|♥    |  |♥    |  |♥    |  |♥    |  |♥    |  |♥    |  |♥    |")
    print("|     |  |     |  |     |  |     |  |     |  |     |  |     |")
    print("|    A|  |    K|  |    Q|  |    J|  |    2|  |    3|  |    4|")
    print(" ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯ ")
    print()
    print("If you have done with choosing a card, help me to find your car with some info.")
    number1 = input("Enter the Row number(1-3), where your card is located: ")
    result += number1
    print("Let's do this again")    
    print()
    print(" _____    _____    _____    _____    _____    _____    _____")
    print("|♠    |  |♠    |  |♠    |  |♦    |  |♦    |  |♥    |  |♥    |")
    print("|     |  |     |  |     |  |     |  |     |  |     |  |     |")
    print("|    A|  |    J|  |    4|  |    Q|  |    3|  |    K|  |    2|")
    print(" ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯ ")
    print(" _____    _____    _____    _____    _____    _____    _____")
    print("|♠    |  |♠    |  |♦    |  |♦    |  |♦    |  |♥    |  |♥    |")
    print("|     |  |     |  |     |  |     |  |     |  |     |  |     |")
    print("|    K|  |    2|  |    A|  |    J|  |    4|  |    Q|  |    3|")
    print(" ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯ ")
    print(" _____    _____    _____    _____    _____    _____    _____")
    print("|♠    |  |♠    |  |♦    |  |♦    |  |♥    |  |♥    |  |♥    |")
    print("|     |  |     |  |     |  |     |  |     |  |     |  |     |")
    print("|    Q|  |    3|  |    K|  |    2|  |    A|  |    J|  |    4|")
    print(" ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯ ")
    number2 = input("Again look at these cards and Enter the row number of your card: ")
    result += number2
    print()
    print("One last step.")
    print(" _____    _____    _____    _____    _____    _____    _____")
    print("|♠    |  |♦    |  |♥    |  |♠    |  |♥    |  |♠    |  |♥    |")
    print("|     |  |     |  |     |  |     |  |     |  |     |  |     |")
    print("|    K|  |    J|  |    3|  |    4|  |    K|  |    3|  |    A|")
    print(" ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯ ")
    print(" _____    _____    _____    _____    _____    _____    _____")
    print("|♠    |  |♦    |  |♠    |  |♦    |  |♥    |  |♦    |  |♥    |")
    print("|     |  |     |  |     |  |     |  |     |  |     |  |     |")
    print("|    2|  |    4|  |    A|  |    Q|  |    2|  |    K|  |    J|")
    print(" ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯ ")
    print(" _____    _____    _____    _____    _____    _____    _____")
    print("|♦    |  |♥    |  |♠    |  |♦    |  |♠    |  |♦    |  |♥    |")
    print("|     |  |     |  |     |  |     |  |     |  |     |  |     |")
    print("|    A|  |    Q|  |    J|  |    3|  |    Q|  |    2|  |    4|")
    print(" ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯    ¯¯¯¯¯ ")
    number3 = input("Look at the following cards and Enter the row number of your card: ")
    result += number3
else:
    print("Restart the game to play again")
#==================================================================================================
if result == "112":
    print(r1)
elif result == "121":
    print(r2)
elif result == "133":
    print(r3)
elif result == "113":
    print(r4)
elif result == "122":
    print(r5)
elif result == "131":
    print(r6)
elif result == "111":
    print(r7)
elif result == "223":
    print(r8)
elif result == "232":
    print(r9)
elif result == "212":
    print(r10)
elif result == "221":
    print(r11)
elif result == "233":
    print(r12)
elif result == "213":
    print(r13)
elif result == "222":
    print(r14)
elif result == "331":
    print(r15)
elif result == "311":
    print(r16)
elif result == "323":
    print(r17)
elif result == "332":
    print(r18)
elif result == "312":
    print(r19)
elif result == "321":
    print(r20)
elif result == "333":
    print(r21)
else: 
    print('Wrong input')
print()
LAST = input("PRESS ENTER TO CLOSE...")