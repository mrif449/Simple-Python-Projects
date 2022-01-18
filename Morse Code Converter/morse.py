print("Welcome to the Morse Code Converter")
print("The dot is represented as '•'")
print("The dash is represened as '-'")
command1 = input("Press Enter to start the program...")
while True:
    if command1 == "":
        print("1. Convert message to Morse Code")
        print("2. Decode Morse Code")
        command2 = input("Enter your choice (1/2): ")
        result1 = ""
        if command2 == "1":
            command3 = input("Enter your message: ")
            for x in command3:
                if x.lower() == "a":
                    result1 += "•- "
                elif x.lower() == "b":
                    result1 += "-••• "
                elif x.lower() == "c":
                    result1 += "-•-• "
                elif x.lower() == "d":
                    result1 += "-•• "
                elif x.lower() == "e":
                    result1 += "• "
                elif x.lower() == "f":
                    result1 += "••-• "
                elif x.lower() == "g":
                    result1 += "--• "
                elif x.lower() == "h":
                    result1 += "•••• "
                elif x.lower() == "i":
                    result1 += "•• "
                elif x.lower() == "j":
                    result1 += "•--- "
                elif x.lower() == "k":
                    result1 += "-•- "
                elif x.lower() == "l":
                    result1 += "•-•• "
                elif x.lower() == "m":
                    result1 += "-- "
                elif x.lower() == "n":
                    result1 += "-• "
                elif x.lower() == "o":
                    result1 += "--- "
                elif x.lower() == "p":
                    result1 += "•--• "
                elif x.lower() == "q":
                    result1 += "--•- "
                elif x.lower() == "r":
                    result1 += "•-• "
                elif x.lower() == "s":
                    result1 += "••• "
                elif x.lower() == "t":
                    result1 += "- "
                elif x.lower() == "u":
                    result1 += "••- "
                elif x.lower() == "v":
                    result1 += "•••- "
                elif x.lower() == "w":
                    result1 += "•-- "
                elif x.lower() == "x":
                    result1 += "-••- "
                elif x.lower() == "y":
                    result1 += "-•-- "
                elif x.lower() == "z":
                    result1 += "--•• "
                elif x == " ":
                    result1 += " / "
                elif x == "0":
                    result1 += "----- "
                elif x == "1":
                    result1 += "•---- "
                elif x == "2":
                    result1 += "••--- "
                elif x == "3":
                    result1 += "•••-- "
                elif x == "4":
                    result1 += "••••- "
                elif x == "5":
                    result1 += "••••• "
                elif x == "6":
                    result1 += "-•••• "
                elif x == "7":
                    result1 += "--••• "
                elif x == "8":
                    result1 += "---•• "
                elif x == "9":
                    result1 += "----• "
                elif x == ".":
                    result1 += "•-•-•- "
                elif x == ",":
                    result1 += "--••-- "
                elif x == "?":
                    result1 += "••--•• "
                elif x == "/":
                    result1 += "-••-• "
                elif x == "@":
                    result1 += "•••-•- "
                else:
                    result1 += "Invalid "
            print("The code is: ",result1)
        elif command2 == "2":
            command3 = input("Enter the Morse Code: ").split("/")
            for x in command3: 
                letter = x.split(" ")
                for y in letter:
                    if y == "•-":
                        result1 += "a"
                    elif y == "-•••":
                        result1 += "b"
                    elif y == "-•-•":
                        result1 += "c"
                    elif y == "-••":
                        result1 += "d"
                    elif y == "•":
                        result1 += "e"
                    elif y == "••-•":
                        result1 += "f"
                    elif y == "--•":
                        result1 += "g"
                    elif y == "••••":
                        result1 += "h"
                    elif y == "••":
                        result1 += "i"
                    elif y == "•---":
                        result1 += "j"
                    elif y == "-•-":
                        result1 += "k"
                    elif y == "•-••":
                        result1 += "l"
                    elif y == "--":
                        result1 += "m"
                    elif y == "-•":
                        result1 += "n"
                    elif y == "---":
                        result1 += "o"
                    elif y == "•--•":
                        result1 += "p"
                    elif y == "--•-":
                        result1 += "q"
                    elif y == "•-•":
                        result1 += "r"
                    elif y == "•••":
                        result1 += "s"
                    elif y == "-":
                        result1 += "t"
                    elif y == "••-":
                        result1 += "u"
                    elif y == "•••-":
                        result1 += "v"
                    elif y == "•--":
                        result1 += "w"
                    elif y == "-••-":
                        result1 += "x"
                    elif y == "-•--":
                        result1 += "y"
                    elif y == "--••":
                        result1 += "z"
                    elif y == "-----":
                        result1 += "0"
                    elif y == "•----":
                        result1 += "1"
                    elif y == "••---":
                        result1 += "2"
                    elif y == "•••-- ":
                        result1 += "3"
                    elif y == "••••-":
                        result1 += "4"
                    elif y == "•••••":
                        result1 += "5"
                    elif y == "-••••":
                        result1 += "6"
                    elif y == "--•••":
                        result1 += "7"
                    elif y == "---••":
                        result1 += "8"
                    elif y == "----•":
                        result1 += "9"
                    elif y == "•-•-•-":
                        result1 += "."
                    elif y == "--••--":
                        result1 += ","
                    elif y == "••--••":
                        result1 += "?"
                    elif y == "-••-•":
                        result1 += "/"
                    elif y == "•••-•-":
                        result1 += "@"
                result1 += " "
            print("The message is: ",result1)
    else:
        break
end = input()
