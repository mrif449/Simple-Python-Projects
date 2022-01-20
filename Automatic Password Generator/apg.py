import random
while True:
    elements = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM1234567890(){[]},./'<>?|:!@#$%^&*"
    print("******Welcome to Automatic Password Generator******")
    amount = int(input("Enter how many password(s) you want to generate: "))
    length = int(input("Enter preferred length for your password: "))
    if amount == 1:
        print("Your password is: ")
    else:
        print(f"Your {amount} passwords are: ")
    for x in range(amount):
        result = ""
        for y in range(length):
            result += random.choice(elements)
        print(result)