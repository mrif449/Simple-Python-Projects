space = "   "
print("****Welcome to Tic-Tac-Toe****")

print(" 0 | 1 | 2 \n----------\n 3 | 4 | 5 \n----------\n 6 | 7 | 8 ")
x = " X "
o = " O "
empty = "   "
array = ["   ","   ","   ","   ","   ","   ","   ","   ","   "]
for i in range(9):
    if i == 0:
            print("Your Turn: ")
            print()
            command = int(input('Enter the index: '))
            array[command] = o
            print(f"{array[0]}|{array[1]}|{array[2]}\n----------\n{array[3]}|{array[4]}|{array[5]}\n----------\n{array[6]}|{array[7]}|{array[8]}")
            if command != 4:
                array[4] = x
            else:
                array[0] = x
            print("Computer's turn: ")
            print()
            print(f"{array[0]}|{array[1]}|{array[2]}\n----------\n{array[3]}|{array[4]}|{array[5]}\n----------\n{array[6]}|{array[7]}|{array[8]}")
            print()
    elif i == 1:
        print("Your Turn: ")
        print()
        command = int(input('Enter the index: '))
        array[command] = o
        print(f"{array[0]}|{array[1]}|{array[2]}\n----------\n{array[3]}|{array[4]}|{array[5]}\n----------\n{array[6]}|{array[7]}|{array[8]}")
        if (array[1] == o and array[2] == o) or (array[1] == o and array[3] == o) or (array[1] == o and array[5] == o) or (array[1] == o and array[6] == o) or (array[1] == o and array[7] == o) or (array[2] == o and array[3] == o) or (array[2] == o and array[6] == o) or (array[2] == o and array[7] == o) or (array[3] == o and array[5] == o) or (array[3] == o and array[6] == o) or (array[3] == o and array[7] == o) or (array[5] == o and array[6] == o) or (array[5] == o and array[7] == o):
            array[0] = x
        elif (array[0] == o and array[2] == o) or (array[0] == o and array[5] == o) or (array[0] == o and array[8] == o) or (array[3] == o and array[8] == o) or (array[4] == o and array[7] == o):
            array[1] = x
        elif (array[0] == o and array[1] == o) or (array[4] == o and array[6] == o) or (array[5] == o and array[8] == o):
            array[2] = x
        elif (array[0] == o and array[6] == o) or (array[0] == o and array[7] == o) or (array[1] == o and array[8] == o) or (array[4] == o and array[5] == o):
            array[3] = x
        elif (array[2] == o and array[8] == o) or (array[4] == o and array[3] == o):
            array[5] = x
        elif (array[0] == o and array[3] == o) or (array[4] == o and array[2] == o) or (array[7] == o and array[8] == o) or (array[4] == o and array[8] == o):
            array[6] = x
        elif (array[4] == o and array[1] == o) or (array[6] == o and array[8] == o):
            array[7] = x
        elif (array[2] == o and array[5] == o) or (array[6] == o and array[7] == o):
            array[8] = x
        print("Computer's turn: ")
        print()
        print(f"{array[0]}|{array[1]}|{array[2]}\n----------\n{array[3]}|{array[4]}|{array[5]}\n----------\n{array[6]}|{array[7]}|{array[8]}")
        print()
    
    
    elif i == 2:
        print("Your Turn: ")
        print()
        command = int(input('Enter the index: '))
        array[command] = o
        print(f"{array[0]}|{array[1]}|{array[2]}\n----------\n{array[3]}|{array[4]}|{array[5]}\n----------\n{array[6]}|{array[7]}|{array[8]}")
        if (array[0] == o and array[4] == o and array[8] == o) or (array[0] == o and array[1] == o and array[2] == o) or (array[0] == o and array[3] == o and array[6] == o) or (array[1] == o and array[4] == o and array[7] == o) or (array[2] == o and array[4] == o and array[6] == o) or (array[3] == o and array[4] == o and array[5] == o) or (array[6] == o and array[7] == o and array[8] == o):
            print("You Win!!!")
            break
        elif (array[1] == x and array[2] == x) or (array[3] == x and array[6] == x) or (array[4] == x and array[8] == x):
            if array[0] == space:
                array[0] = x
            
        elif (array[0] == x and array[2] == x) or (array[4] == x and array[7] == x):
            if array[0] == space:
                array[1] = x
            
        elif (array[0] == x and array[1] == x) or (array[4] == x and array[6] == x) or (array[5] == x and array[8] == x):
            if array[2] == space:
                array[2] = x
            
        elif (array[0] == x and array[6] == x) or (array[4] == x and array[5] == x):
            if array[3] == space:
                array[3] = x
            
        elif (array[0] == x and array[8] == x) or (array[1] == x and array[7] == x) or (array[2] == x and array[6] == x) or (array[3] == x and array[5] == x):
            if array[4] == space:
                array[4] = x
        elif (array[3] == x and array[4] == x) or (array[2] == x and array[8] == x):
            if array[5] == space:
                array[5] = x
            
        elif (array[0] == x and array[3] == x) or (array[2] == x and array[4] == x) or (array[7] == x and array[8] == x):
            if array[6] == space:
                array[6] = x
            
        elif (array[1] == x and array[4] == x) or (array[6] == x and array[8] == x):
            if array[7] == space:
                array[7] = x
            
        elif (array[0] == x and array[4] == x) or (array[2] == x and array[5] == x) or (array[6] == x and array[67] == x):
            if array[8] == space:
                array[8] = x
        if (array[0] == x and array[4] == x and array[8] == x) or (array[0] == x and array[1] == x and array[2] == x) or (array[0] == x and array[3] == x and array[6] == x) or (array[1] == x and array[4] == x and array[7] == x) or (array[2] == x and array[4] == x and array[6] == x) or (array[3] == x and array[4] == x and array[5] == x) or (array[3] == x and array[4] == x and array[5] == x) or (array[6] == x and array[7] == x and array[8] == x):
            print("Computer's turn: ")
            print()
            print(f"{array[0]}|{array[1]}|{array[2]}\n----------\n{array[3]}|{array[4]}|{array[5]}\n----------\n{array[6]}|{array[7]}|{array[8]}")
            print("Computer Wins!!!")
            break
        else:
            for z in range(len(array)):
                if array[z] == space:
                    array[z] = x
                    break
        print(f"{array[0]}|{array[1]}|{array[2]}\n----------\n{array[3]}|{array[4]}|{array[5]}\n----------\n{array[6]}|{array[7]}|{array[8]}")
        if (array[0] == x and array[4] == x and array[8] == x) or (array[0] == x and array[1] == x and array[2] == x) or (array[0] == x and array[3] == x and array[6] == x) or (array[1] == x and array[4] == x and array[7] == x) or (array[2] == x and array[4] == x and array[6] == x) or (array[3] == x and array[4] == x and array[5] == x) or (array[3] == x and array[4] == x and array[5] == x) or (array[6] == x and array[7] == x and array[8] == x):
            print("Computer's turn: ")
            print()
            print(f"{array[0]}|{array[1]}|{array[2]}\n----------\n{array[3]}|{array[4]}|{array[5]}\n----------\n{array[6]}|{array[7]}|{array[8]}")
            print("Computer Wins!!!")
            break
    elif i == 3:
        print("Your Turn: ")
        print()
        command = int(input('Enter the index: '))
        array[command] = o
        print(f"{array[0]}|{array[1]}|{array[2]}\n----------\n{array[3]}|{array[4]}|{array[5]}\n----------\n{array[6]}|{array[7]}|{array[8]}")
        print()
        if (array[0] == o and array[4] == o and array[8] == o) or (array[0] == o and array[1] == o and array[2] == o) or (array[0] == o and array[3] == o and array[6] == o) or (array[1] == o and array[4] == o and array[7] == o) or (array[2] == o and array[4] == o and array[6] == o) or (array[3] == o and array[4] == o and array[5] == o) or (array[6] == o and array[7] == o and array[8] == o) or (array[5] == o and array[2] == o and array[8] == o):
            print("You Win!!!")
            break
        elif (array[1] == x and array[2] == x) or (array[3] == x and array[6] == x) or (array[4] == x and array[8] == x):
            if array[0] == space:
                array[0] = x
            
        elif (array[0] == x and array[2] == x) or (array[4] == x and array[7] == x):
            if array[0] == space:
                array[1] = x
            
        elif (array[0] == x and array[1] == x) or (array[4] == x and array[6] == x) or (array[5] == x and array[8] == x):
            if array[2] == space:
                array[2] = x
            
        elif (array[0] == x and array[6] == x) or (array[4] == x and array[5] == x):
            if array[3] == space:
                array[3] = x
            
        elif (array[0] == x and array[8] == x) or (array[1] == x and array[7] == x) or (array[2] == x and array[6] == x) or (array[3] == x and array[5] == x):
            if array[4] == space:
                array[4] = x
        elif (array[3] == x and array[4] == x) or (array[2] == x and array[8] == x):
            if array[5] == space:
                array[5] = x
            
        elif (array[0] == x and array[3] == x) or (array[2] == x and array[4] == x) or (array[7] == x and array[8] == x):
            if array[6] == space:
                array[6] = x
            
        elif (array[1] == x and array[4] == x) or (array[6] == x and array[8] == x):
            if array[7] == space:
                array[7] = x
            
        elif (array[0] == x and array[4] == x) or (array[2] == x and array[5] == x) or (array[6] == x and array[67] == x):
            if array[8] == space:
                array[8] = x
        if (array[0] == x and array[4] == x and array[8] == x) or (array[0] == x and array[1] == x and array[2] == x) or (array[0] == x and array[3] == x and array[6] == x) or (array[1] == x and array[4] == x and array[7] == x) or (array[2] == x and array[4] == x and array[6] == x) or (array[3] == x and array[4] == x and array[5] == x) or (array[3] == x and array[4] == x and array[5] == x) or (array[6] == x and array[7] == x and array[8] == x):
            print("Computer's turn: ")
            print()
            print(f"{array[0]}|{array[1]}|{array[2]}\n----------\n{array[3]}|{array[4]}|{array[5]}\n----------\n{array[6]}|{array[7]}|{array[8]}")
            print("Computer Wins!!!")
            break
        else:
            for z in range(len(array)):
                if array[z] == space:
                    array[z] = x
                    break
        if (array[0] == o and array[3] == o and array[2] == o and array[7] == o):
            print("Computer's turn: ")
            print()
            print(f"{array[0]}|{array[1]}|{array[2]}\n----------\n{array[3]}|{array[4]}|{array[5]}\n----------\n{array[6]}|{array[7]}|{array[8]}")
            print("DRAW!!!")
            break
        print("Computer's turn: ")
        print()
        print(f"{array[0]}|{array[1]}|{array[2]}\n----------\n{array[3]}|{array[4]}|{array[5]}\n----------\n{array[6]}|{array[7]}|{array[8]}")
        if (array[0] == x and array[4] == x and array[8] == x) or (array[0] == x and array[1] == x and array[2] == x) or (array[0] == x and array[3] == x and array[6] == x) or (array[1] == x and array[4] == x and array[7] == x) or (array[2] == x and array[4] == x and array[6] == x) or (array[3] == x and array[4] == x and array[5] == x) or (array[3] == x and array[4] == x and array[5] == x) or (array[6] == x and array[7] == x and array[8] == x):
            print("Computer Wins!!!")
            break
    elif i == 4:
        print("Your Turn: ")
        print()
        command = int(input('Enter the index: '))
        array[command] = o
        print(f"{array[0]}|{array[1]}|{array[2]}\n----------\n{array[3]}|{array[4]}|{array[5]}\n----------\n{array[6]}|{array[7]}|{array[8]}")
        print()
        if (array[0] == o and array[4] == o and array[8] == o) or (array[0] == o and array[1] == o and array[2] == o) or (array[0] == o and array[3] == o and array[6] == o) or (array[1] == o and array[4] == o and array[7] == o) or (array[2] == o and array[4] == o and array[6] == o) or (array[3] == o and array[4] == o and array[5] == o) or (array[6] == o and array[7] == o and array[8] == o) or (array[6] == o and array[7] == o and array[8] == o):
            print("You Win!!!")
            break
        else:
            print("DRAW!!!")
command3 = input("Press Enter to close...")