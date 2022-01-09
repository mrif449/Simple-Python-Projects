while True:
    print("Welcome to message Encryption and Decryption program")
    print("1. Encrypt a Message")
    print("2. Decrypt a message")
    command = (input("Enter your choice(1,2): "))

    if command == "1":
        imessage = input("Enter your message: ")
        omessage = ""
        for x in imessage:
            if x == "a":
                omessage += "!"
            elif x == "b":
                omessage += "@"
            elif x == "c":
                omessage += "#"
            elif x == "d":
                omessage += "$"
            elif x == "e":
                omessage += "%"
            elif x == "f":
                omessage += "^"
            elif x == "g":
                omessage += "&"
            elif x == "h":
                omessage += "*"
            elif x == "i":
                omessage += "("
            elif x == "j":
                omessage += ")"
            elif x == "k":
                omessage += "_"
            elif x == "l":
                omessage += "+"
            elif x == "m":
                omessage += "-"
            elif x == "n":
                omessage += "="
            elif x == "o":
                omessage += "`"
            elif x == "p":
                omessage += "~"
            elif x == "q":
                omessage += "a"
            elif x == "r":
                omessage += "q"
            elif x == "s":
                omessage += "z"
            elif x == "t":
                omessage += "w"
            elif x == "u":
                omessage += "s"
            elif x == "v":
                omessage += "x"
            elif x == "w":
                omessage += "e"
            elif x == "x":
                omessage += "d"
            elif x == "y":
                omessage += "c"
            elif x == "z":
                omessage += "r"
            elif x == "1":
                omessage += "f"
            elif x == "2":
                omessage += "v"
            elif x == "3":
                omessage += "t"
            elif x == "4":
                omessage += "g"
            elif x == "5":
                omessage += "b"
            elif x == "6":
                omessage += "y"
            elif x == "7":
                omessage += "h"
            elif x == "8":
                omessage += "n"
            elif x == "9":
                omessage += "u"
            elif x == "0":
                omessage += "j"
            elif x == "!":
                omessage += "m"
            elif x == "@":
                omessage += "i"
            elif x == "#":
                omessage += "k"
            elif x == "$":
                omessage += ","
            elif x == "%":
                omessage += "o"
            elif x == "^":
                omessage += "|"
            elif x == "&":
                omessage += "."
            elif x == "*":
                omessage += "p"
            elif x == "(":
                omessage += ";"
            elif x == ")":
                omessage += "["
            elif x == "-":
                omessage += "'"
            elif x == "Y":
                omessage += "A"
            elif x == "Z":
                omessage += "W"
            elif x == "[":
                omessage += "Z"
            elif x == "]":
                omessage += "S"
            elif x == ";":
                omessage += "X"
            elif x == "'":
                omessage += "E"
            elif x == ",":
                omessage += "D"
            elif x == ".":
                omessage += "R"
            elif x == "/":
                omessage += "F"
            elif x == "{":
                omessage += "V"
            elif x == "}":
                omessage += "T"
            elif x == ":":
                omessage += "G"
            elif x == "|":
                omessage += "Y"
            elif x == "<":
                omessage += "H"
            elif x == ">":
                omessage += "N"
            elif x == "?":
                omessage += "U"
            elif x == "`":
                omessage += "J"
            elif x == "~":
                omessage += "M"
            elif x == "A":
                omessage += "I"
            elif x == "B":
                omessage += "K"
            elif x == "C":
                omessage += "<"
            elif x == "D":
                omessage += "O"
            elif x == "E":
                omessage += "L"
            elif x == "F":
                omessage += ">"
            elif x == "G":
                omessage += "P"
            elif x == "H":
                omessage += ":"
            elif x == "I":
                omessage += "?"
            elif x == "J":
                omessage += "{"
            elif x == "K":
                omessage += "B"
            elif x == "L":
                omessage += "}"
            elif x == "M":
                omessage += "|"
            elif x == "N":
                omessage += "1"
            elif x == "O":
                omessage += "2"
            elif x == "P":
                omessage += "3"
            elif x == "Q":
                omessage += "4"
            elif x == "R":
                omessage += "5"
            elif x == "S":
                omessage += "6"
            elif x == "T":
                omessage += "7"
            elif x == "U":
                omessage += " "
            elif x == "V":
                omessage += "9"
            elif x == "W":
                omessage += "0"
            elif x == "X":
                omessage += "D"
            elif x == " ":
                omessage += "8"
            else:
                omessage += x
        print(omessage)
    elif command == "2":
        imessage = input("Enter your message: ")
        omessage = ""
        for x in imessage:
            if x == "!":
                omessage += "a"
            elif x == "@":
                omessage += "b"
            elif x == "#":
                omessage += "c"
            elif x == "$":
                omessage += "d"
            elif x == "%":
                omessage += "e"
            elif x == "^":
                omessage += "f"
            elif x == "&":
                omessage += "g"
            elif x == "*":
                omessage += "h"
            elif x == "(":
                omessage += "i"
            elif x == ")":
                omessage += "j"
            elif x == "_":
                omessage += "k"
            elif x == "+":
                omessage += "l"
            elif x == "-":
                omessage += "m"
            elif x == "=":
                omessage += "n"
            elif x == "`":
                omessage += "o"
            elif x == "~":
                omessage += "p"
            elif x == "a":
                omessage += "q"
            elif x == "q":
                omessage += "r"
            elif x == "z":
                omessage += "s"
            elif x == "w":
                omessage += "t"
            elif x == "s":
                omessage += "u"
            elif x == "x":
                omessage += "v"
            elif x == "e":
                omessage += "w"
            elif x == "d":
                omessage += "x"
            elif x == "c":
                omessage += "y"
            elif x == "r":
                omessage += "z"
            elif x == "f":
                omessage += "1"
            elif x == "v":
                omessage += "2"
            elif x == "t":
                omessage += "3"
            elif x == "g":
                omessage += "4"
            elif x == "b":
                omessage += "5"
            elif x == "y":
                omessage += "6"
            elif x == "h":
                omessage += "7"
            elif x == "n":
                omessage += "8"
            elif x == "u":
                omessage += "9"
            elif x == "j":
                omessage += "0"
            elif x == "m":
                omessage += "!"
            elif x == "i":
                omessage += "@"
            elif x == "k":
                omessage += "#"
            elif x == ",":
                omessage += "$"
            elif x == "o":
                omessage += "%"
            elif x == "l":
                omessage += "^"
            elif x == ".":
                omessage += "&"
            elif x == "p":
                omessage += "*"
            elif x == ";":
                omessage += "("
            elif x == "[":
                omessage += ")"
            elif x == "'":
                omessage += "-"
            elif x == "A":
                omessage += "Y"
            elif x == "W":
                omessage += "Z"
            elif x == "Z":
                omessage += "["
            elif x == "S":
                omessage += "]"
            elif x == "X":
                omessage += ";"
            elif x == "E":
                omessage += "'"
            elif x == "D":
                omessage += ","
            elif x == "R":
                omessage += "."
            elif x == "F":
                omessage += "/"
            elif x == "V":
                omessage += "{"
            elif x == "T":
                omessage += "}"
            elif x == "G":
                omessage += ":"
            elif x == "Y":
                omessage += "|"
            elif x == "H":
                omessage += "<"
            elif x == "N":
                omessage += ">"
            elif x == "U":
                omessage += "?"
            elif x == "J":
                omessage += "`"
            elif x == "M":
                omessage += "~"
            elif x == "I":
                omessage += "A"
            elif x == "K":
                omessage += "B"
            elif x == "<":
                omessage += "C"
            elif x == "O":
                omessage += "D"
            elif x == "L":
                omessage += "E"
            elif x == ">":
                omessage += "F"
            elif x == "P":
                omessage += "G"
            elif x == ":":
                omessage += "H"
            elif x == "?":
                omessage += "I"
            elif x == "{":
                omessage += "J"
            elif x == "B":
                omessage += "K"
            elif x == "}":
                omessage += "L"
            elif x == "|":
                omessage += "M"
            elif x == "1":
                omessage += "N"
            elif x == "2":
                omessage += "O"
            elif x == "3":
                omessage += "P"
            elif x == "4":
                omessage += "Q"
            elif x == "5":
                omessage += "R"
            elif x == "6":
                omessage += "S"
            elif x == "7":
                omessage += "T"
            elif x == " ":
                omessage += "U"
            elif x == "9":
                omessage += "V"
            elif x == "0":
                omessage += "W"
            elif x == "D":
                omessage += "X"
            elif x == "8":
                omessage += " "
            else:
                omessage += x
        print(omessage)
    else:
        break
end = input("Press Enter to Close...")