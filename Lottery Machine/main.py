import random
RUN_LIMIT = 20000
MAX_AMOUNT = 50000
MAX_BET = 5000
MIN_BET = 100
MAX_LINES = 3
checks = [0,0,0]
array = ["A","B","C"]
account = 0
bet_values = []
for x in range(len(array)):
    bet_values.append(random.randint(1,4))

def deposit():
    global account
    while True:
        amount = input("Enter an Amount to Deposit: ৳")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break    
            else:
                print("Minimum amount of Deposit is 1")
        else:
            print("Please Enter a valid amount")
    account = amount

def runner(balance):
    global account
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ৳{account}")
        else:
            print(f"You are betting ৳{bet} on {lines} lines. Total bet is equal to: ৳{total_bet}")
            line_run(0)
            line_run(1)
            line_run(2)
            break
    
    global checks
    temp_bal = account
    counter = 0
    for x in checks:
        if x == 1:
            counter += 1
    if counter == 0:
            account -= bet*lines
            print(f"Sorry you did not won anything. Your Balance ৳{account}")
    else:
            for x in range(counter):
                account = account + bet*(random.randint(1,4))
            print(f"You have won {counter} lines. You won ৳{account-temp_bal} \nYour balace is ৳{account}")
    print(checks)
    return lines,bet

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? ৳")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ৳{MIN_BET} - ৳{MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

def get_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number.")
    return lines

def line_run(number):
    global checks
    global array
    unique = []
    results = []
    for x in range(RUN_LIMIT):
        print(array[random.randint(0,len(array)-1)],end="\r")
        if x != RUN_LIMIT-1:
            print(array[random.randint(0,len(array)-1)],end="\r")
        else:
            results.append(array[random.randint(0,len(array)-1)])

    for x in range(RUN_LIMIT):
        if x != RUN_LIMIT-1:
            print(results[0],"|",array[random.randint(0,len(array)-1)],end="\r")
        else:
            results.append(array[random.randint(0,len(array)-1)])

    for x in range(RUN_LIMIT):
        if x != RUN_LIMIT-1:
            print(results[0],"|",results[1],"|",array[random.randint(0,len(array)-1)],end="\r")
        else:
            results.append(array[random.randint(0,len(array)-1)])

    print(results[0],"|",results[1],"|",results[2]+"")
    for a in results:
        if a not in unique:
            unique.append(a)
    if len(unique) == 1:
        checks[number] = 1
    for x in results:
        results.pop()

balance = deposit()
def main():
    while True:
        answer = input("Press enter to play (x to quit).")
        print(account)
        if answer == "x" or account<=0 or account<MIN_BET:
            print(f"Goodbye you have ৳{account}")
            break
        runner(account)
        checks[0] = 0
        checks[1] = 0
        checks[2] = 0
main()

