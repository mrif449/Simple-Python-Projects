print("Welcome to this Game.")
print()
inp1 = input("Enter 's' to start the Game: ")
if inp1.lower() == "s":
    print("Take any number you want")
    inp2 = input("Enter 'y' to jump on the next step: ")
    if inp2.lower() == "y":
        print("Multiply their number by 2")
        print()
        print("Done?")
        inp3 = input("If Yes, Enter 'y': ")
        if inp3.lower() == "y":
            print("Now, multiply the new number by 5.")
            inp4 = input("If you are done, Enter 'y': ")
            if inp4.lower() == 'y':
                print("You are going really good.")
                print("Now you need to divide current number by your original number.")
                print()
                print("Sorry for the boring y input.")
                inp5 = input("If you complete doing that, Press 'y': ")
                if inp5.lower() == "y":
                    print("Last step:")
                    print("Subtract 6 from their current number.")
                    inp6 = input("If you are done, Let me know by entening 'y': ")
                    if inp6.lower() == "y":
                        print("Let me surprise you.")
                        print()
                        print("YOU RESULT IS 4!!!")
                    else:
                        print("Sorry, you just missed the surprise.")
                else:
                    print("Please, restart the game")
            else:
                print("Please start over.")
        else:
            print("To continue the game, you have to restart the game.")
    else:
        print("Please restart the game")
else:
    print("Have a good day.")