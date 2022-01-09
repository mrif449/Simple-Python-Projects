print("Welcome to Base Converter Calculator!!!")
print("You can select your calculation mode by entering the serial number, or write 'close' stop calculating.")
print()
print("Note: You can also close the whole program by pressing Enter after closing calculation menu or manually.")

#Options:
print("Basic Bases:")
print("Decimal = 10")
print("Binary = 2")
print("Octal = 8")
print("Hexa-Decimal = 16")
print("...............................")
print("Let's Start...")
print("Press Enter to Start...")
inp = input("or Anything to Stop...")
while True:
    if inp == "":
        
        
        #Selecting Calculation Mode:
        #command = (input("Select your calculation mode (1-14): "))
        i_base = int(input("Enter the input Base: "))
        o_base = int(input("Enter the output Base: "))

        #Decimal to Binary
        if i_base == 10 and o_base == 2: 
            number = int(input("Enter the Decimal number: "))
            temp = number
            string = ""
            temp_list = []
            while temp > 0:
                string += str(temp%2)
                temp = temp //  2
            for x in string:
                temp_list.append(x)
            temp_list.reverse()
            result = ""
            for y in temp_list:
                result += y
            print("=============================")
            print("Your result is",result)
            print("=============================")

        #Decimal to Octal
        elif i_base == 10 and o_base == 8:
            number = int(input("Enter the Decimal number: "))
            temp = number
            string = ""
            temp_list = []
            while temp > 0:
                string += str(temp%8)
                temp = temp //  8
            for x in string:
                temp_list.append(x)
            temp_list.reverse()
            result = ""
            for y in temp_list:
                result += y
            print("=============================")
            print("Your result is",result)
            print("=============================")

        #Decimal to Hexa-Decimal
        elif i_base == 10 and o_base == 16:
            number = int(input("Enter the Decimal number: "))
            temp = number
            string = ""
            temp_list = []
            while temp > 0:
                temp2 = temp%16
                if temp2 == 10:
                    string += "A"
                elif temp2 == 11:
                    string += "B"
                elif temp2 == 12:
                    string += "C"
                elif temp2 == 13:
                    string += "D"
                elif temp2 == 14:
                    string += "E"
                elif temp2 == 15:
                    string += "F"
                else:
                    string += str(temp%16)
                temp = temp //  16
            for x in string:
                temp_list.append(x)
            temp_list.reverse()
            result = ""
            for y in temp_list:
                result += y
            print("=============================")
            print("Your result is",result)
            print("=============================")

        #Binary to Decimal
        elif i_base == 2 and o_base == 10:
            number = int(input("Enter the Binary number: "))
            string = str(number)
            count = 0
            sum = 0
            for x in string:
                count += 1
            string_list = []
            for b in string:
                string_list.append(int(b))
            temp_list = []
            for y in range(0,count):
                temp_list.append(int(y))
            temp_list.reverse()
            for x in range(0,len(string_list)):
                sum += (string_list[x]*(2**temp_list[x]))
            print("=============================")
            print("Your result is",sum)
            print("=============================")

        #Binary to Octal
        elif i_base == 2 and o_base == 8:
            number = int(input("Enter the Binary number: "))
            string = str(number)
            count = 0
            sum = 0
            for x in string:
                count += 1
            string_list = []
            for b in string:
                string_list.append(int(b))
            temp_list = []
            for y in range(0,count):
                temp_list.append(int(y))
            temp_list.reverse()
            for x in range(0,len(string_list)):
                sum += (string_list[x]*(2**temp_list[x]))
            number2 = sum
            temp = number2
            string = ""
            temp_list = []
            while temp > 0:
                string += str(temp%8)
                temp = temp //  8
            for x in string:
                temp_list.append(x)
            temp_list.reverse()
            result = ""
            for y in temp_list:
                result += y
            print("=============================")
            print("Your result is",result)
            print("=============================")

        #Binary to Hexa-Decimal
        elif i_base == 2 and o_base == 16:
            number = int(input("Enter the Binary number: "))
            string = str(number)
            count = 0
            sum = 0
            for x in string:
                count += 1
            string_list = []
            for b in string:
                string_list.append(int(b))
            temp_list = []
            for y in range(0,count):
                temp_list.append(int(y))
            temp_list.reverse()
            for x in range(0,len(string_list)):
                sum += (string_list[x]*(2**temp_list[x]))
            number2 = sum
            temp = number2
            string = ""
            temp_list = []
            while temp > 0:
                temp2 = temp%16
                if temp2 == 10:
                    string += "A"
                elif temp2 == 11:
                    string += "B"
                elif temp2 == 12:
                    string += "C"
                elif temp2 == 13:
                    string += "D"
                elif temp2 == 14:
                    string += "E"
                elif temp2 == 15:
                    string += "F"
                else:
                    string += str(temp%16)
                temp = temp //  16
            for x in string:
                temp_list.append(x)
            temp_list.reverse()
            result = ""
            for y in temp_list:
                result += y
            print("=============================")
            print("Your result is",result)
            print("=============================")
        #Octal to Decimal
        elif i_base == 8 and o_base == 10:
            number = int(input("Enter the Octal number: "))
            string = str(number)
            count = 0
            sum = 0
            for x in string:
                count += 1
            string_list = []
            for b in string:
                string_list.append(int(b))
            temp_list = []
            for y in range(0,count):
                temp_list.append(int(y))
            temp_list.reverse()
            for x in range(0,len(string_list)):
                sum += (string_list[x]*(8**temp_list[x]))
            print("=============================")
            print("Your result is",sum)
            print("=============================")

        #Octal to Binary
        elif i_base == 8 and o_base == 2:
            number = int(input("Enter the Octal number: "))
            string = str(number)
            count = 0
            sum = 0
            for x in string:
                count += 1
            string_list = []
            for b in string:
                string_list.append(int(b))
            temp_list = []
            for y in range(0,count):
                temp_list.append(int(y))
            temp_list.reverse()
            for x in range(0,len(string_list)):
                sum += (string_list[x]*(8**temp_list[x]))
            number2 = sum
            temp = number2
            string = ""
            temp_list = []
            while temp > 0:
                string += str(temp%2)
                temp = temp //  2
            for x in string:
                temp_list.append(x)
            temp_list.reverse()
            result = ""
            for y in temp_list:
                result += y
            print("=============================")
            print("Your result is",result)
            print("=============================")

        #Octal to Hexa-Decimal
        elif i_base == 8 and o_base == 16:
            number = int(input("Enter the Octal number: "))
            string = str(number)
            count = 0
            sum = 0
            for x in string:
                count += 1
            string_list = []
            for b in string:
                string_list.append(int(b))
            temp_list = []
            for y in range(0,count):
                temp_list.append(int(y))
            temp_list.reverse()
            for x in range(0,len(string_list)):
                sum += (string_list[x]*(8**temp_list[x]))
            number2 = sum
            temp = number2
            string = ""
            temp_list = []
            while temp > 0:
                temp2 = temp%16
                if temp2 == 10:
                    string += "A"
                elif temp2 == 11:
                    string += "B"
                elif temp2 == 12:
                    string += "C"
                elif temp2 == 13:
                    string += "D"
                elif temp2 == 14:
                    string += "E"
                elif temp2 == 15:
                    string += "F"
                else:
                    string += str(temp%16)
                temp = temp //  16
            for x in string:
                temp_list.append(x)
            temp_list.reverse()
            result = ""
            for y in temp_list:
                result += y
            print("=============================")
            print("Your result is",result)
            print("=============================")

        #Hexa-Decimal to Decimal
        elif i_base == 16 and o_base == 10:
            string = input("Enter the Hexa-Decimal Number: ")
            count = 0
            sum = 0
            for x in string:
                count += 1
            string_list = []
            for b in string:
                if b.upper() == "A":
                    string_list.append(10)
                elif b.upper() == "B":
                    string_list.append(11)
                elif b.upper() == "C":
                    string_list.append(12)
                elif b.upper() == "D":
                    string_list.append(13)
                elif b.upper() == "E":
                    string_list.append(14)
                elif b.upper() == "F":
                    string_list.append(15)
                else:
                    string_list.append(int(b))
            temp_list = []
            for y in range(0,count):
                temp_list.append(int(y))
            temp_list.reverse()
            for x in range(0,len(string_list)):
                sum += (string_list[x]*(16**temp_list[x]))
            print("=============================")
            print("Your result is",sum)
            print("=============================")

        #Hexa-Decimal to Binary
        elif i_base == 16 and o_base == 2:
            string = input("Enter the Hexa-Decimal Number: ")
            count = 0
            sum = 0
            for x in string:
                count += 1
            string_list = []
            for b in string:
                if b.upper() == "A":
                    string_list.append(10)
                elif b.upper() == "B":
                    string_list.append(11)
                elif b.upper() == "C":
                    string_list.append(12)
                elif b.upper() == "D":
                    string_list.append(13)
                elif b.upper() == "E":
                    string_list.append(14)
                elif b.upper() == "F":
                    string_list.append(15)
                else:
                    string_list.append(int(b))
            temp_list = []
            for y in range(0,count):
                temp_list.append(int(y))
            temp_list.reverse()
            for x in range(0,len(string_list)):
                sum += (string_list[x]*(16**temp_list[x]))
            number2 = sum
            temp = number2
            string = ""
            temp_list = []
            while temp > 0:
                string += str(temp%2)
                temp = temp //  2
            for x in string:
                temp_list.append(x)
            temp_list.reverse()
            result = ""
            for y in temp_list:
                result += y
            print("=============================")
            print("Your result is",result)
            print("=============================")

        #Hexa-Decimal to Octal
        elif i_base == 16 and o_base == 8:
            string = input("Enter the Hexa-Decimal Number: ")
            count = 0
            sum = 0
            for x in string:
                count += 1
            string_list = []
            for b in string:
                if b.upper() == "A":
                    string_list.append(10)
                elif b.upper() == "B":
                    string_list.append(11)
                elif b.upper() == "C":
                    string_list.append(12)
                elif b.upper() == "D":
                    string_list.append(13)
                elif b.upper() == "E":
                    string_list.append(14)
                elif b.upper() == "F":
                    string_list.append(15)
                else:
                    string_list.append(int(b))
            temp_list = []
            for y in range(0,count):
                temp_list.append(int(y))
            temp_list.reverse()
            for x in range(0,len(string_list)):
                sum += (string_list[x]*(16**temp_list[x]))
            number2 = sum
            temp = number2
            string = ""
            temp_list = []
            while temp > 0:
                string += str(temp%8)
                temp = temp //  8
            for x in string:
                temp_list.append(x)
            temp_list.reverse()
            result = ""
            for y in temp_list:
                result += y
            print("=============================")
            print("Your result is",result)
            print("=============================")
        
        #Decimal to Other Base:
        elif i_base == 10:
            if o_base == 3:
                number = int(input("Enter the Decimal number: "))
                temp = number
                string = ""
                temp_list = []
                while temp > 0:
                    string += str(temp%3)
                    temp = temp //  3
                for x in string:
                    temp_list.append(x)
                temp_list.reverse()
                result = ""
                for y in temp_list:
                    result += y
                print("=============================")
                print("Your result is",result)
                print("=============================")
            elif o_base == 4:
                number = int(input("Enter the Decimal number: "))
                temp = number
                string = ""
                temp_list = []
                while temp > 0:
                    string += str(temp%4)
                    temp = temp //  4
                for x in string:
                    temp_list.append(x)
                temp_list.reverse()
                result = ""
                for y in temp_list:
                    result += y
                print("=============================")
                print("Your result is",result)
                print("=============================")
            elif o_base == 5:
                number = int(input("Enter the Decimal number: "))
                temp = number
                string = ""
                temp_list = []
                while temp > 0:
                    string += str(temp%5)
                    temp = temp //  5
                for x in string:
                    temp_list.append(x)
                temp_list.reverse()
                result = ""
                for y in temp_list:
                    result += y
                print("=============================")
                print("Your result is",result)
                print("=============================")
            elif o_base == 6:
                number = int(input("Enter the Decimal number: "))
                temp = number
                string = ""
                temp_list = []
                while temp > 0:
                    string += str(temp%6)
                    temp = temp //  6
                for x in string:
                    temp_list.append(x)
                temp_list.reverse()
                result = ""
                for y in temp_list:
                    result += y
                print("=============================")
                print("Your result is",result)
                print("=============================")
            elif o_base == 7:
                number = int(input("Enter the Decimal number: "))
                temp = number
                string = ""
                temp_list = []
                while temp > 0:
                    string += str(temp%7)
                    temp = temp //  7
                for x in string:
                    temp_list.append(x)
                temp_list.reverse()
                result = ""
                for y in temp_list:
                    result += y
                print("=============================")
                print("Your result is",result)
                print("=============================")
            elif o_base == 9:
                number = int(input("Enter the Decimal number: "))
                temp = number
                string = ""
                temp_list = []
                while temp > 0:
                    string += str(temp%9)
                    temp = temp //  9
                for x in string:
                    temp_list.append(x)
                temp_list.reverse()
                result = ""
                for y in temp_list:
                    result += y
                print("=============================")
                print("Your result is",result)
                print("=============================")
            elif o_base == 11:
                number = int(input("Enter the Decimal number: "))
                temp = number
                string = ""
                temp_list = []
                while temp > 0:
                    temp2 = temp%11
                    if temp2 == 10:
                        string += "A"
                    else:
                        string += str(temp%11)
                    temp = temp //  11
                for x in string:
                    temp_list.append(x)
                temp_list.reverse()
                result = ""
                for y in temp_list:
                    result += y
                print("=============================")
                print("Your result is",result)
                print("=============================")
            elif o_base == 12:
                number = int(input("Enter the Decimal number: "))
                temp = number
                string = ""
                temp_list = []
                while temp > 0:
                    temp2 = temp%12
                    if temp2 == 10:
                        string += "A"
                    elif temp2 == 11:
                        string += "B"
                    else:
                        string += str(temp%12)
                    temp = temp //  12
                for x in string:
                    temp_list.append(x)
                temp_list.reverse()
                result = ""
                for y in temp_list:
                    result += y
                print("=============================")
                print("Your result is",result)
                print("=============================")
            elif o_base == 13:
                number = int(input("Enter the Decimal number: "))
                temp = number
                string = ""
                temp_list = []
                while temp > 0:
                    temp2 = temp%13
                    if temp2 == 10:
                        string += "A"
                    elif temp2 == 11:
                        string += "B"
                    elif temp2 == 12:
                        string += "C"
                    else:
                        string += str(temp%13)
                    temp = temp //  13
                for x in string:
                    temp_list.append(x)
                temp_list.reverse()
                result = ""
                for y in temp_list:
                    result += y
                print("=============================")
                print("Your result is",result)
                print("=============================")
            elif o_base == 14:
                number = int(input("Enter the Decimal number: "))
                temp = number
                string = ""
                temp_list = []
                while temp > 0:
                    temp2 = temp%14
                    if temp2 == 10:
                        string += "A"
                    elif temp2 == 11:
                        string += "B"
                    elif temp2 == 12:
                        string += "C"
                    elif temp2 == 13:
                        string += "D"
                    else:
                        string += str(temp%14)
                    temp = temp //  14
                for x in string:
                    temp_list.append(x)
                temp_list.reverse()
                result = ""
                for y in temp_list:
                    result += y
                print("=============================")
                print("Your result is",result)
                print("=============================")
            elif o_base == 15:
                number = int(input("Enter the Decimal number: "))
                temp = number
                string = ""
                temp_list = []
                while temp > 0:
                    temp2 = temp%15
                    if temp2 == 10:
                        string += "A"
                    elif temp2 == 11:
                        string += "B"
                    elif temp2 == 12:
                        string += "C"
                    elif temp2 == 13:
                        string += "D"
                    elif temp2 == 14:
                        string += "E"
                    else:
                        string += str(temp%15)
                    temp = temp //  15
                for x in string:
                    temp_list.append(x)
                temp_list.reverse()
                result = ""
                for y in temp_list:
                    result += y
                print("=============================")
                print("Your result is",result)
                print("=============================")
            elif o_base == 17:
                number = int(input("Enter the Decimal number: "))
                temp = number
                string = ""
                temp_list = []
                while temp > 0:
                    temp2 = temp%17
                    if temp2 == 10:
                        string += "A"
                    elif temp2 == 11:
                        string += "B"
                    elif temp2 == 12:
                        string += "C"
                    elif temp2 == 13:
                        string += "D"
                    elif temp2 == 14:
                        string += "E"
                    elif temp2 == 15:
                        string += "F"
                    elif temp2 == 16:
                        string += "G"
                    else:
                        string += str(temp%17)
                    temp = temp //  17
                for x in string:
                    temp_list.append(x)
                temp_list.reverse()
                result = ""
                for y in temp_list:
                    result += y
                print("=============================")
                print("Your result is",result)
                print("=============================")
            elif o_base == 18:
                number = int(input("Enter the Decimal number: "))
                temp = number
                string = ""
                temp_list = []
                while temp > 0:
                    temp2 = temp%18
                    if temp2 == 10:
                        string += "A"
                    elif temp2 == 11:
                        string += "B"
                    elif temp2 == 12:
                        string += "C"
                    elif temp2 == 13:
                        string += "D"
                    elif temp2 == 14:
                        string += "E"
                    elif temp2 == 15:
                        string += "F"
                    elif temp2 == 16:
                        string += "G"
                    elif temp2 == 17:
                        string += "H"
                    else:
                        string += str(temp%18)
                    temp = temp //  18
                for x in string:
                    temp_list.append(x)
                temp_list.reverse()
                result = ""
                for y in temp_list:
                    result += y
                print("=============================")
                print("Your result is",result)
                print("=============================")
            elif o_base == 19:
                number = int(input("Enter the Decimal number: "))
                temp = number
                string = ""
                temp_list = []
                while temp > 0:
                    temp2 = temp%19
                    if temp2 == 10:
                        string += "A"
                    elif temp2 == 11:
                        string += "B"
                    elif temp2 == 12:
                        string += "C"
                    elif temp2 == 13:
                        string += "D"
                    elif temp2 == 14:
                        string += "E"
                    elif temp2 == 15:
                        string += "F"
                    elif temp2 == 16:
                        string += "G"
                    elif temp2 == 17:
                        string += "H"
                    elif temp2 == 18:
                        string += "I"
                    else:
                        string += str(temp%19)
                    temp = temp //  19
                for x in string:
                    temp_list.append(x)
                temp_list.reverse()
                result = ""
                for y in temp_list:
                    result += y
                print("=============================")
                print("Your result is",result)
                print("=============================")
            elif o_base == 20:
                number = int(input("Enter the Decimal number: "))
                temp = number
                string = ""
                temp_list = []
                while temp > 0:
                    temp2 = temp%20
                    if temp2 == 10:
                        string += "A"
                    elif temp2 == 11:
                        string += "B"
                    elif temp2 == 12:
                        string += "C"
                    elif temp2 == 13:
                        string += "D"
                    elif temp2 == 14:
                        string += "E"
                    elif temp2 == 15:
                        string += "F"
                    elif temp2 == 16:
                        string += "G"
                    elif temp2 == 17:
                        string += "H"
                    elif temp2 == 18:
                        string += "I"
                    elif temp2 == 19:
                        string += "J"
                    else:
                        string += str(temp%20)
                    temp = temp //  20
                for x in string:
                    temp_list.append(x)
                temp_list.reverse()
                result = ""
                for y in temp_list:
                    result += y
                print("=============================")
                print("Your result is",result)
                print("=============================")
            elif o_base == 21:
                number = int(input("Enter the Decimal number: "))
                temp = number
                string = ""
                temp_list = []
                while temp > 0:
                    temp2 = temp%21
                    if temp2 == 10:
                        string += "A"
                    elif temp2 == 11:
                        string += "B"
                    elif temp2 == 12:
                        string += "C"
                    elif temp2 == 13:
                        string += "D"
                    elif temp2 == 14:
                        string += "E"
                    elif temp2 == 15:
                        string += "F"
                    elif temp2 == 16:
                        string += "G"
                    elif temp2 == 17:
                        string += "H"
                    elif temp2 == 18:
                        string += "I"
                    elif temp2 == 19:
                        string += "J"
                    elif temp2 == 20:
                        string += "K"
                    else:
                        string += str(temp%21)
                    temp = temp //  21
                for x in string:
                    temp_list.append(x)
                temp_list.reverse()
                result = ""
                for y in temp_list:
                    result += y
                print("=============================")
                print("Your result is",result)
                print("=============================")
            elif o_base == 22:
                number = int(input("Enter the Decimal number: "))
                temp = number
                string = ""
                temp_list = []
                while temp > 0:
                    temp2 = temp%22
                    if temp2 == 10:
                        string += "A"
                    elif temp2 == 11:
                        string += "B"
                    elif temp2 == 12:
                        string += "C"
                    elif temp2 == 13:
                        string += "D"
                    elif temp2 == 14:
                        string += "E"
                    elif temp2 == 15:
                        string += "F"
                    elif temp2 == 16:
                        string += "G"
                    elif temp2 == 17:
                        string += "H"
                    elif temp2 == 18:
                        string += "I"
                    elif temp2 == 19:
                        string += "J"
                    elif temp2 == 20:
                        string += "K"
                    elif temp2 == 21:
                        string += "L"
                    else:
                        string += str(temp%22)
                    temp = temp //  22
                for x in string:
                    temp_list.append(x)
                temp_list.reverse()
                result = ""
                for y in temp_list:
                    result += y
                print("=============================")
                print("Your result is",result)
                print("=============================")
            elif o_base == 23:
                number = int(input("Enter the Decimal number: "))
                temp = number
                string = ""
                temp_list = []
                while temp > 0:
                    temp2 = temp%23
                    if temp2 == 10:
                        string += "A"
                    elif temp2 == 11:
                        string += "B"
                    elif temp2 == 12:
                        string += "C"
                    elif temp2 == 13:
                        string += "D"
                    elif temp2 == 14:
                        string += "E"
                    elif temp2 == 15:
                        string += "F"
                    elif temp2 == 16:
                        string += "G"
                    elif temp2 == 17:
                        string += "H"
                    elif temp2 == 18:
                        string += "I"
                    elif temp2 == 19:
                        string += "J"
                    elif temp2 == 20:
                        string += "K"
                    elif temp2 == 21:
                        string += "L"
                    elif temp2 == 22:
                        string += "M"
                    else:
                        string += str(temp%23)
                    temp = temp //  23
                for x in string:
                    temp_list.append(x)
                temp_list.reverse()
                result = ""
                for y in temp_list:
                    result += y
                print("=============================")
                print("Your result is",result)
                print("=============================")
            elif o_base == 24:
                number = int(input("Enter the Decimal number: "))
                temp = number
                string = ""
                temp_list = []
                while temp > 0:
                    temp2 = temp%24
                    if temp2 == 10:
                        string += "A"
                    elif temp2 == 11:
                        string += "B"
                    elif temp2 == 12:
                        string += "C"
                    elif temp2 == 13:
                        string += "D"
                    elif temp2 == 14:
                        string += "E"
                    elif temp2 == 15:
                        string += "F"
                    elif temp2 == 16:
                        string += "G"
                    elif temp2 == 17:
                        string += "H"
                    elif temp2 == 18:
                        string += "I"
                    elif temp2 == 19:
                        string += "J"
                    elif temp2 == 20:
                        string += "K"
                    elif temp2 == 21:
                        string += "L"
                    elif temp2 == 22:
                        string += "M"
                    elif temp2 == 23:
                        string += "N"
                    else:
                        string += str(temp%24)
                    temp = temp //  24
                for x in string:
                    temp_list.append(x)
                temp_list.reverse()
                result = ""
                for y in temp_list:
                    result += y
                print("=============================")
                print("Your result is",result)
                print("=============================")
            elif o_base == 25:
                number = int(input("Enter the Decimal number: "))
                temp = number
                string = ""
                temp_list = []
                while temp > 0:
                    temp2 = temp%25
                    if temp2 == 10:
                        string += "A"
                    elif temp2 == 11:
                        string += "B"
                    elif temp2 == 12:
                        string += "C"
                    elif temp2 == 13:
                        string += "D"
                    elif temp2 == 14:
                        string += "E"
                    elif temp2 == 15:
                        string += "F"
                    elif temp2 == 16:
                        string += "G"
                    elif temp2 == 17:
                        string += "H"
                    elif temp2 == 18:
                        string += "I"
                    elif temp2 == 19:
                        string += "J"
                    elif temp2 == 20:
                        string += "K"
                    elif temp2 == 21:
                        string += "L"
                    elif temp2 == 22:
                        string += "M"
                    elif temp2 == 23:
                        string += "N"
                    elif temp2 == 24:
                        string += "O"
                    else:
                        string += str(temp%25)
                    temp = temp //  25
                for x in string:
                    temp_list.append(x)
                temp_list.reverse()
                result = ""
                for y in temp_list:
                    result += y
                print("=============================")
                print("Your result is",result)
                print("=============================")
            elif o_base == 26:
                number = int(input("Enter the Decimal number: "))
                temp = number
                string = ""
                temp_list = []
                while temp > 0:
                    temp2 = temp%26
                    if temp2 == 10:
                        string += "A"
                    elif temp2 == 11:
                        string += "B"
                    elif temp2 == 12:
                        string += "C"
                    elif temp2 == 13:
                        string += "D"
                    elif temp2 == 14:
                        string += "E"
                    elif temp2 == 15:
                        string += "F"
                    elif temp2 == 16:
                        string += "G"
                    elif temp2 == 17:
                        string += "H"
                    elif temp2 == 18:
                        string += "I"
                    elif temp2 == 19:
                        string += "J"
                    elif temp2 == 20:
                        string += "K"
                    elif temp2 == 21:
                        string += "L"
                    elif temp2 == 22:
                        string += "M"
                    elif temp2 == 23:
                        string += "N"
                    elif temp2 == 24:
                        string += "O"
                    elif temp2 == 25:
                        string += "P"
                    else:
                        string += str(temp%26)
                    temp = temp //  26
                for x in string:
                    temp_list.append(x)
                temp_list.reverse()
                result = ""
                for y in temp_list:
                    result += y
                print("=============================")
                print("Your result is",result)
                print("=============================")
            elif o_base == 27:
                number = int(input("Enter the Decimal number: "))
                temp = number
                string = ""
                temp_list = []
                while temp > 0:
                    temp2 = temp%27
                    if temp2 == 10:
                        string += "A"
                    elif temp2 == 11:
                        string += "B"
                    elif temp2 == 12:
                        string += "C"
                    elif temp2 == 13:
                        string += "D"
                    elif temp2 == 14:
                        string += "E"
                    elif temp2 == 15:
                        string += "F"
                    elif temp2 == 16:
                        string += "G"
                    elif temp2 == 17:
                        string += "H"
                    elif temp2 == 18:
                        string += "I"
                    elif temp2 == 19:
                        string += "J"
                    elif temp2 == 20:
                        string += "K"
                    elif temp2 == 21:
                        string += "L"
                    elif temp2 == 22:
                        string += "M"
                    elif temp2 == 23:
                        string += "N"
                    elif temp2 == 24:
                        string += "O"
                    elif temp2 == 25:
                        string += "P"
                    elif temp2 == 26:
                        string += "Q"
                    else:
                        string += str(temp%27)
                    temp = temp //  27
                for x in string:
                    temp_list.append(x)
                temp_list.reverse()
                result = ""
                for y in temp_list:
                    result += y
                print("=============================")
                print("Your result is",result)
                print("=============================")
            elif o_base == 28:
                number = int(input("Enter the Decimal number: "))
                temp = number
                string = ""
                temp_list = []
                while temp > 0:
                    temp2 = temp%28
                    if temp2 == 10:
                        string += "A"
                    elif temp2 == 11:
                        string += "B"
                    elif temp2 == 12:
                        string += "C"
                    elif temp2 == 13:
                        string += "D"
                    elif temp2 == 14:
                        string += "E"
                    elif temp2 == 15:
                        string += "F"
                    elif temp2 == 16:
                        string += "G"
                    elif temp2 == 17:
                        string += "H"
                    elif temp2 == 18:
                        string += "I"
                    elif temp2 == 19:
                        string += "J"
                    elif temp2 == 20:
                        string += "K"
                    elif temp2 == 21:
                        string += "L"
                    elif temp2 == 22:
                        string += "M"
                    elif temp2 == 23:
                        string += "N"
                    elif temp2 == 24:
                        string += "O"
                    elif temp2 == 25:
                        string += "P"
                    elif temp2 == 26:
                        string += "Q"
                    elif temp2 == 27:
                        string += "R"
                    else:
                        string += str(temp%28)
                    temp = temp //  28
                for x in string:
                    temp_list.append(x)
                temp_list.reverse()
                result = ""
                for y in temp_list:
                    result += y
                print("=============================")
                print("Your result is",result)
                print("=============================")
            elif o_base == 29:
                number = int(input("Enter the Decimal number: "))
                temp = number
                string = ""
                temp_list = []
                while temp > 0:
                    temp2 = temp%29
                    if temp2 == 10:
                        string += "A"
                    elif temp2 == 11:
                        string += "B"
                    elif temp2 == 12:
                        string += "C"
                    elif temp2 == 13:
                        string += "D"
                    elif temp2 == 14:
                        string += "E"
                    elif temp2 == 15:
                        string += "F"
                    elif temp2 == 16:
                        string += "G"
                    elif temp2 == 17:
                        string += "H"
                    elif temp2 == 18:
                        string += "I"
                    elif temp2 == 19:
                        string += "J"
                    elif temp2 == 20:
                        string += "K"
                    elif temp2 == 21:
                        string += "L"
                    elif temp2 == 22:
                        string += "M"
                    elif temp2 == 23:
                        string += "N"
                    elif temp2 == 24:
                        string += "O"
                    elif temp2 == 25:
                        string += "P"
                    elif temp2 == 26:
                        string += "Q"
                    elif temp2 == 27:
                        string += "R"
                    elif temp2 == 28:
                        string += "S"
                    else:
                        string += str(temp%29)
                    temp = temp //  29
                for x in string:
                    temp_list.append(x)
                temp_list.reverse()
                result = ""
                for y in temp_list:
                    result += y
                print("=============================")
                print("Your result is",result)
                print("=============================")
            elif o_base == 30:
                number = int(input("Enter the Decimal number: "))
                temp = number
                string = ""
                temp_list = []
                while temp > 0:
                    temp2 = temp%30
                    if temp2 == 10:
                        string += "A"
                    elif temp2 == 11:
                        string += "B"
                    elif temp2 == 12:
                        string += "C"
                    elif temp2 == 13:
                        string += "D"
                    elif temp2 == 14:
                        string += "E"
                    elif temp2 == 15:
                        string += "F"
                    elif temp2 == 16:
                        string += "G"
                    elif temp2 == 17:
                        string += "H"
                    elif temp2 == 18:
                        string += "I"
                    elif temp2 == 19:
                        string += "J"
                    elif temp2 == 20:
                        string += "K"
                    elif temp2 == 21:
                        string += "L"
                    elif temp2 == 22:
                        string += "M"
                    elif temp2 == 23:
                        string += "N"
                    elif temp2 == 24:
                        string += "O"
                    elif temp2 == 25:
                        string += "P"
                    elif temp2 == 26:
                        string += "Q"
                    elif temp2 == 27:
                        string += "R"
                    elif temp2 == 28:
                        string += "S"
                    elif temp2 == 29:
                        string += "T"
                    else:
                        string += str(temp%30)
                    temp = temp //  30
                for x in string:
                    temp_list.append(x)
                temp_list.reverse()
                result = ""
                for y in temp_list:
                    result += y
                print("=============================")
                print("Your result is",result)
                print("=============================")
            elif o_base == 31:
                number = int(input("Enter the Decimal number: "))
                temp = number
                string = ""
                temp_list = []
                while temp > 0:
                    temp2 = temp%31
                    if temp2 == 10:
                        string += "A"
                    elif temp2 == 11:
                        string += "B"
                    elif temp2 == 12:
                        string += "C"
                    elif temp2 == 13:
                        string += "D"
                    elif temp2 == 14:
                        string += "E"
                    elif temp2 == 15:
                        string += "F"
                    elif temp2 == 16:
                        string += "G"
                    elif temp2 == 17:
                        string += "H"
                    elif temp2 == 18:
                        string += "I"
                    elif temp2 == 19:
                        string += "J"
                    elif temp2 == 20:
                        string += "K"
                    elif temp2 == 21:
                        string += "L"
                    elif temp2 == 22:
                        string += "M"
                    elif temp2 == 23:
                        string += "N"
                    elif temp2 == 24:
                        string += "O"
                    elif temp2 == 25:
                        string += "P"
                    elif temp2 == 26:
                        string += "Q"
                    elif temp2 == 27:
                        string += "R"
                    elif temp2 == 28:
                        string += "S"
                    elif temp2 == 29:
                        string += "T"
                    elif temp2 == 30:
                        string += "U"
                    else:
                        string += str(temp%31)
                    temp = temp //  31
                for x in string:
                    temp_list.append(x)
                temp_list.reverse()
                result = ""
                for y in temp_list:
                    result += y
                print("=============================")
                print("Your result is",result)
                print("=============================")
            elif o_base == 32:
                number = int(input("Enter the Decimal number: "))
                temp = number
                string = ""
                temp_list = []
                while temp > 0:
                    temp2 = temp%32
                    if temp2 == 10:
                        string += "A"
                    elif temp2 == 11:
                        string += "B"
                    elif temp2 == 12:
                        string += "C"
                    elif temp2 == 13:
                        string += "D"
                    elif temp2 == 14:
                        string += "E"
                    elif temp2 == 15:
                        string += "F"
                    elif temp2 == 16:
                        string += "G"
                    elif temp2 == 17:
                        string += "H"
                    elif temp2 == 18:
                        string += "I"
                    elif temp2 == 19:
                        string += "J"
                    elif temp2 == 20:
                        string += "K"
                    elif temp2 == 21:
                        string += "L"
                    elif temp2 == 22:
                        string += "M"
                    elif temp2 == 23:
                        string += "N"
                    elif temp2 == 24:
                        string += "O"
                    elif temp2 == 25:
                        string += "P"
                    elif temp2 == 26:
                        string += "Q"
                    elif temp2 == 27:
                        string += "R"
                    elif temp2 == 28:
                        string += "S"
                    elif temp2 == 29:
                        string += "T"
                    elif temp2 == 30:
                        string += "U"
                    elif temp2 == 31:
                        string += "V"
                    else:
                        string += str(temp%32)
                    temp = temp //  32
                for x in string:
                    temp_list.append(x)
                temp_list.reverse()
                result = ""
                for y in temp_list:
                    result += y
                print("=============================")
                print("Your result is",result)
                print("=============================")
            elif o_base == 33:
                number = int(input("Enter the Decimal number: "))
                temp = number
                string = ""
                temp_list = []
                while temp > 0:
                    temp2 = temp%33
                    if temp2 == 10:
                        string += "A"
                    elif temp2 == 11:
                        string += "B"
                    elif temp2 == 12:
                        string += "C"
                    elif temp2 == 13:
                        string += "D"
                    elif temp2 == 14:
                        string += "E"
                    elif temp2 == 15:
                        string += "F"
                    elif temp2 == 16:
                        string += "G"
                    elif temp2 == 17:
                        string += "H"
                    elif temp2 == 18:
                        string += "I"
                    elif temp2 == 19:
                        string += "J"
                    elif temp2 == 20:
                        string += "K"
                    elif temp2 == 21:
                        string += "L"
                    elif temp2 == 22:
                        string += "M"
                    elif temp2 == 23:
                        string += "N"
                    elif temp2 == 24:
                        string += "O"
                    elif temp2 == 25:
                        string += "P"
                    elif temp2 == 26:
                        string += "Q"
                    elif temp2 == 27:
                        string += "R"
                    elif temp2 == 28:
                        string += "S"
                    elif temp2 == 29:
                        string += "T"
                    elif temp2 == 30:
                        string += "U"
                    elif temp2 == 31:
                        string += "V"
                    elif temp2 == 32:
                        string += "W"
                    else:
                        string += str(temp%33)
                    temp = temp //  33
                for x in string:
                    temp_list.append(x)
                temp_list.reverse()
                result = ""
                for y in temp_list:
                    result += y
                print("=============================")
                print("Your result is",result)
                print("=============================")
            elif o_base == 34:
                number = int(input("Enter the Decimal number: "))
                temp = number
                string = ""
                temp_list = []
                while temp > 0:
                    temp2 = temp%34
                    if temp2 == 10:
                        string += "A"
                    elif temp2 == 11:
                        string += "B"
                    elif temp2 == 12:
                        string += "C"
                    elif temp2 == 13:
                        string += "D"
                    elif temp2 == 14:
                        string += "E"
                    elif temp2 == 15:
                        string += "F"
                    elif temp2 == 16:
                        string += "G"
                    elif temp2 == 17:
                        string += "H"
                    elif temp2 == 18:
                        string += "I"
                    elif temp2 == 19:
                        string += "J"
                    elif temp2 == 20:
                        string += "K"
                    elif temp2 == 21:
                        string += "L"
                    elif temp2 == 22:
                        string += "M"
                    elif temp2 == 23:
                        string += "N"
                    elif temp2 == 24:
                        string += "O"
                    elif temp2 == 25:
                        string += "P"
                    elif temp2 == 26:
                        string += "Q"
                    elif temp2 == 27:
                        string += "R"
                    elif temp2 == 28:
                        string += "S"
                    elif temp2 == 29:
                        string += "T"
                    elif temp2 == 30:
                        string += "U"
                    elif temp2 == 31:
                        string += "V"
                    elif temp2 == 32:
                        string += "W"
                    elif temp2 == 33:
                        string += "X"
                    else:
                        string += str(temp%34)
                    temp = temp //  34
                for x in string:
                    temp_list.append(x)
                temp_list.reverse()
                result = ""
                for y in temp_list:
                    result += y
                print("=============================")
                print("Your result is",result)
                print("=============================")
            elif o_base == 35:
                number = int(input("Enter the Decimal number: "))
                temp = number
                string = ""
                temp_list = []
                while temp > 0:
                    temp2 = temp%35
                    if temp2 == 10:
                        string += "A"
                    elif temp2 == 11:
                        string += "B"
                    elif temp2 == 12:
                        string += "C"
                    elif temp2 == 13:
                        string += "D"
                    elif temp2 == 14:
                        string += "E"
                    elif temp2 == 15:
                        string += "F"
                    elif temp2 == 16:
                        string += "G"
                    elif temp2 == 17:
                        string += "H"
                    elif temp2 == 18:
                        string += "I"
                    elif temp2 == 19:
                        string += "J"
                    elif temp2 == 20:
                        string += "K"
                    elif temp2 == 21:
                        string += "L"
                    elif temp2 == 22:
                        string += "M"
                    elif temp2 == 23:
                        string += "N"
                    elif temp2 == 24:
                        string += "O"
                    elif temp2 == 25:
                        string += "P"
                    elif temp2 == 26:
                        string += "Q"
                    elif temp2 == 27:
                        string += "R"
                    elif temp2 == 28:
                        string += "S"
                    elif temp2 == 29:
                        string += "T"
                    elif temp2 == 30:
                        string += "U"
                    elif temp2 == 31:
                        string += "V"
                    elif temp2 == 32:
                        string += "W"
                    elif temp2 == 33:
                        string += "X"
                    elif temp2 == 34:
                        string += "Y"
                    else:
                        string += str(temp%35)
                    temp = temp //  35
                for x in string:
                    temp_list.append(x)
                temp_list.reverse()
                result = ""
                for y in temp_list:
                    result += y
                print("=============================")
                print("Your result is",result)
                print("=============================")
            elif o_base == 36:
                number = int(input("Enter the Decimal number: "))
                temp = number
                string = ""
                temp_list = []
                while temp > 0:
                    temp2 = temp%36
                    if temp2 == 10:
                        string += "A"
                    elif temp2 == 11:
                        string += "B"
                    elif temp2 == 12:
                        string += "C"
                    elif temp2 == 13:
                        string += "D"
                    elif temp2 == 14:
                        string += "E"
                    elif temp2 == 15:
                        string += "F"
                    elif temp2 == 16:
                        string += "G"
                    elif temp2 == 17:
                        string += "H"
                    elif temp2 == 18:
                        string += "I"
                    elif temp2 == 19:
                        string += "J"
                    elif temp2 == 20:
                        string += "K"
                    elif temp2 == 21:
                        string += "L"
                    elif temp2 == 22:
                        string += "M"
                    elif temp2 == 23:
                        string += "N"
                    elif temp2 == 24:
                        string += "O"
                    elif temp2 == 25:
                        string += "P"
                    elif temp2 == 26:
                        string += "Q"
                    elif temp2 == 27:
                        string += "R"
                    elif temp2 == 28:
                        string += "S"
                    elif temp2 == 29:
                        string += "T"
                    elif temp2 == 30:
                        string += "U"
                    elif temp2 == 31:
                        string += "V"
                    elif temp2 == 32:
                        string += "W"
                    elif temp2 == 33:
                        string += "X"
                    elif temp2 == 34:
                        string += "Y"
                    elif temp2 == 35:
                        string += "Z"
                    else:
                        string += str(temp%36)
                    temp = temp //  36
                for x in string:
                    temp_list.append(x)
                temp_list.reverse()
                result = ""
                for y in temp_list:
                    result += y
                print("=============================")
                print("Your result is",result)
                print("=============================")
    else:
        break


inp = input("Press Enter to close...")