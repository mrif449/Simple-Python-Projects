import random

range_number = input("Enter your guess limit: ").split("-")
user_number = int(input("Enter a number: "))
random_number = random.randrange(int(range_number[0]),int(range_number[1]))
if user_number == random_number:
    print("Congratulations :)")
else:
    print('Sorry :( The number was',random_number)
loop = input("Press Enter to Close...")