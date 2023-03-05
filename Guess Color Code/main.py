import random

ARRAY = ["R", "W", "B", "G", "Y", "V"]

mystery = []
for x in range(4):
    mystery.append(random.choice(ARRAY))

#print(mystery)
prize = 0
trys = 10
for x in range(trys):
    position = 0
    user_input = list((input("Enter Your Guess: ").split()))
    for y in range(4):
        if user_input[y].upper() == mystery[y]:
            position += 1
    if position == 4:
        prize += (trys-x)*10
        
        break
    else:
        print(f"You have {position} correct position(s).\n {trys-1-x} Try(s) left.")
print(f"The correct code was {mystery}.")
print(f"Congratulations!! The Vault is unlocked now. You got ${prize}💰")